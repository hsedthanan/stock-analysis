import pandas as pd
import matplotlib.pyplot as plt

# อ่านข้อมูลจากไฟล์ stock_data.csv
data = pd.read_csv("stock_data.csv")

# กรองข้อมูลเฉพาะหุ้น AOT
aot_data = data[data["Stock"] == "AOT"]

# ตรวจสอบแนวโน้มราคาหุ้น AOT
aot_data["Date"] = pd.to_datetime(aot_data["Date"])
aot_data = aot_data.sort_values("Date")

# แสดงข้อมูลแนวโน้มราคาหุ้น AOT
plt.figure(figsize=(10, 6))
plt.plot(aot_data["Date"], aot_data["Price"], marker="o", label="AOT Price")
plt.title("AOT Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid()
plt.legend()
plt.show()

# บันทึกผลลัพธ์ลงในไฟล์ aot_analysis.txt
with open("aot_analysis.txt", "w") as file:
    file.write("AOT Stock Price Analysis\n")
    file.write(f"Maximum Price: {aot_data['Price'].max()}\n")
    file.write(f"Minimum Price: {aot_data['Price'].min()}\n")
    file.write(f"Average Price: {aot_data['Price'].mean()}\n")