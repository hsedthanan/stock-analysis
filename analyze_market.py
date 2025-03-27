import pandas as pd

def analyze_market_trend(file_path, output_file="market_analysis.txt"):
    """Analyze overall market trend from a CSV file and save the result."""
    # อ่านไฟล์ CSV
    df = pd.read_csv(file_path)
    
    # ตรวจสอบว่ามีคอลัมน์ที่จำเป็นหรือไม่
    required_columns = {'Date', 'Stock', 'Price'}
    if not required_columns.issubset(df.columns):
        missing_columns = required_columns - set(df.columns)
        print(f"Error: Missing columns: {missing_columns}")
        return
    
    # คำนวณการเปลี่ยนแปลงของราคาหุ้นรายวัน
    df['Price Change'] = df.groupby('Stock')['Price'].diff().fillna(0)
    
    # กำหนดแนวโน้มของหุ้นแต่ละตัว
    df['Trend'] = df['Price Change'].apply(lambda x: 'Up' if x > 0 else 'Down' if x < 0 else 'No Change')
    
    # สรุปแนวโน้มของตลาด
    trend_summary = df.groupby('Trend').size()
    
    # บันทึกผลลงไฟล์
    with open(output_file, 'w') as f:
        f.write("Market Trend Analysis\n")
        f.write("======================\n")
        f.write(trend_summary.to_string())
    
    print(f"Analysis saved to {output_file}")
    
if __name__ == "__main__":
    file_path = "stock_data.csv"
    analyze_market_trend(file_path)