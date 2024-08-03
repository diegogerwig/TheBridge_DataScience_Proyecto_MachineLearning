import pandas as pd
import sys


def process_csv(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Perform some basic data processing

        # Display the first few rows of the DataFrame
        print("First 5 rows of the DataFrame:")
        print(df.head())

        # Display the statistical description of the DataFrame
        print("\nStatistical description of the DataFrame:")
        print(df.describe())
        
    except Exception as e:
        print(f"Error processing the CSV file: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python data_processing.py <csv_path>")
    else:
        file_path = sys.argv[1]
        process_csv(file_path)
