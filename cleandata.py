import pandas as pd


df = pd.read_csv("KaggleV2-May-2016.csv")

print("Original shape:", df.shape)

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print("\nMissing values:\n", df.isnull().sum())

df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)

df['scheduledday'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

df['no_show'] = df['no-show'].str.strip().str.upper()

print("\nData types:\n", df.dtypes)

df.to_csv("medical_appointments_cleaned.csv", index=False)
print("\n Cleaned data saved as 'medical_appointments_cleaned.csv'")
