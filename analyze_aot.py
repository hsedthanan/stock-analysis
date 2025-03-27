import pandas as pd

def analyze_aot_trend(file_path):
    """Analyze the trend of AOT stock prices from a CSV file."""
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Print columns in the CSV file
    print("Columns in the CSV file:", df.columns.tolist())

    # Check if required columns exist
    required_columns = {'Date', 'Stock', 'Price'}
    if not required_columns.issubset(df.columns):
        missing_columns = required_columns - set(df.columns)
        print(f"Error: The following required columns are missing from the CSV file: {missing_columns}.")
        print("Please ensure the file contains the columns: Date, Stock, Price.")
        print("Current columns in the file:", df.columns.tolist())
        return

    # Filter data for AOT stock
    aot_data = df[df['Stock'] == 'AOT']

    # Calculate daily price change (using Price as a proxy for Close - Open)
    aot_data['Price Change'] = aot_data['Price'].diff().fillna(0)

    # Determine trend
    aot_data['Trend'] = aot_data['Price Change'].apply(lambda x: 'Up' if x > 0 else 'Down' if x < 0 else 'No Change')

    # Print summary
    print(aot_data[['Date', 'Price', 'Price Change', 'Trend']])

    return aot_data

if __name__ == "__main__":
    # Example usage
    file_path = "stock_data.csv"
    analyze_aot_trend(file_path)