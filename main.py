import pandas as pd
import json

# Load CSV
df_google = pd.read_csv("google_forms.csv")

# Load Excel
df_email = pd.read_excel("email_submissions.xlsx")

# Load JSON
with open("website_feedback.json", "r") as f:
    website_data = json.load(f)
df_website = pd.DataFrame(website_data)

df_master = pd.concat([df_google, df_email, df_website], ignore_index=True)

# Hapus duplikat
df_master.drop_duplicates(inplace=True)

# Standarisasi kolom
df_master = df_master[['Name', 'Email', 'Date', 'Feedback']]

# Simpan file master CSV
df_master.to_csv("master_feedback.csv", index=False, encoding='utf-8')
print("Master CSV berhasil dibuat! Total entri:", len(df_master))