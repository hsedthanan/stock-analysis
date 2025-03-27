import pandas as pd

def analyze_aot_trend(file_path, output_file="aot_analysis.txt"):
    """Analyze the trend of AOT stock prices from a CSV file and save the analysis to a file."""
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Print columns in the CSV file
    print("Columns in the CSV file:", df.columns.tolist())

    # Check if required columns exist
    required_columns = {'Date', 'Stock', 'Price'}
    if not required_columns.issubset(df.columns):
        missing_columns = required_columns - set(df.columns)
        error_message = f"Error: The following required columns are missing from the CSV file: {missing_columns}.\n"
        error_message += "Please ensure the file contains the columns: Date, Stock, Price.\n"
        error_message += f"Current columns in the file: {df.columns.tolist()}\n"

        # Save error to file
        with open(output_file, "w") as file:
            file.write(error_message)

        print(error_message)
        return

    # Filter data for AOT stock
    aot_data = df[df['Stock'] == 'AOT'].copy()

    # Convert 'Date' column to datetime
    aot_data['Date'] = pd.to_datetime(aot_data['Date'])
    aot_data = aot_data.sort_values('Date')

    # Calculate daily price change
    aot_data['Price Change'] = aot_data['Price'].diff().fillna(0)

    # Determine trend
    aot_data['Trend'] = aot_data['Price Change'].apply(lambda x: 'Up' if x > 0 else 'Down' if x < 0 else 'No Change')

    # Save the analysis to a file
    with open(output_file, "w") as file:
        file.write("AOT Stock Price Analysis\n")
        file.write(f"Maximum Price: {aot_data['Price'].max():.2f}\n")
        file.write(f"Minimum Price: {aot_data['Price'].min():.2f}\n")
        file.write(f"Average Price: {aot_data['Price'].mean():.2f}\n")
        file.write("\nTrend Analysis:\n")
        file.write(aot_data[['Date', 'Price', 'Price Change', 'Trend']].to_string(index=False))

    print(f"Analysis saved to {output_file}")

    return aot_data


if __name__ == "__main__":
    # Example usage
    file_path = "stock_data.csv"
    analyze_aot_trend(file_path)
