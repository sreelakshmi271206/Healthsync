try:
    import pandas as pd
except ImportError:
    print("Error: pandas is not installed. Install it with: pip install pandas")
    exit()
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        df = pd.read_csv(path)

        print("\n" + "=" * 50)
        print("FILE:", file)
        print("Rows:", df.shape[0])
        print("Columns:", df.shape[1])

        print("\nMissing values:")
        print(df.isnull().sum())

        print("\nDuplicate rows:", df.duplicated().sum())