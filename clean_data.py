import pandas as pd
import os

# Input and output folders
raw_folder = "data/raw"
processed_folder = "data/processed"

# Create processed folder if it doesn't exist
os.makedirs(processed_folder, exist_ok=True)

# Clean every CSV file in data/raw
for file in os.listdir(raw_folder):

    if file.endswith(".csv"):

        input_path = os.path.join(raw_folder, file)
        output_path = os.path.join(processed_folder, file)

        # Read CSV
        df = pd.read_csv(input_path)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove extra spaces from column names
        df.columns = df.columns.str.strip()

        # Remove extra spaces from text values
        for column in df.select_dtypes(include="object").columns:
            df[column] = df[column].str.strip()

        # Save cleaned CSV
        df.to_csv(output_path, index=False)

        print(f"Cleaned: {file}")

print("\nAll CSV files cleaned successfully!")