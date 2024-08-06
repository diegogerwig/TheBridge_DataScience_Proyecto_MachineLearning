import pandas as pd
import os
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

        # Construct the output file path
        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)
        output_file_name = f"{name}_proc{ext}"

        # Define the processed directory path
        processed_dir = '../data/processed'
        os.makedirs(processed_dir, exist_ok=True)
        output_path = os.path.join(processed_dir, output_file_name)

        df.to_csv(output_path, index=False)
        print(f"\n✅ The processed DataFrame has been saved to {output_path}")
        
    except Exception as e:
        print(f"❌ Error processing the CSV file: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("💥 Usage: python data_processing.py <csv_path>")
    else:
        file_path = sys.argv[1]
        process_csv(file_path)
