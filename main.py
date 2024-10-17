import os
import pandas as pd

filename = "file.csv"
file_path = os.path.join(os.getcwd(), filename)

HIGH_MATCH = "HIGH"
MEDIUM_MATCH = "MEDIUM"
LOW_MATCH = "LOW"

data = pd.read_csv(file_path)
data["email"] = data["email"].astype(str)
data["address"] = data["address"].astype(str)

def find_duplicates(df):
    results = []
    num_rows = len(df)

    for i in range(num_rows - 1):
      row1 = df.iloc[i]

      for j in range(i + 1, num_rows):
          row2 = df.iloc[j]

          print(f"Comparing rows {i + 1} - {j + 1}", end="\r")
    
          email_match = row1['email'].strip().lower() == row2['email'].strip().lower() and row1['email']
          name_match = row1['name'].strip().lower() == row2['name'].strip().lower() and row1['name']
          last_name_match = row1['name1'].strip().lower() == row2['name1'].strip().lower() and row1['name1']
          zip_match = row1['postalZip'] == row2['postalZip'] and pd.notna(row1['postalZip'])
          address_match = row1['address'].strip().lower() == row2['address'].strip().lower() and row1['address'] != "nan"

          if email_match:
              accuracy = HIGH_MATCH
          elif name_match and last_name_match and (zip_match or address_match):
              accuracy = MEDIUM_MATCH
          elif name_match and address_match:
              accuracy = LOW_MATCH
          else:
              continue
          
          results.append({
              'ContactID Source': row1['contactID'],
              'ContactID Match': row2['contactID'],
              'Accuracy': accuracy
          })
    
    print("Finished comparisons       ")
    return pd.DataFrame(results)

duplicate_matches = find_duplicates(data)
output_file = os.path.join(os.getcwd(), "duplicate_matches.csv")
duplicate_matches.to_csv(output_file, index=False)
