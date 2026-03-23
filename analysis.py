import pandas as pd
import matplotlib.pyplot as plt
import os

# LOAD DATA
df = pd.read_csv('sales_data.csv')

# CLEAN DATA
df['order_date'] = pd.to_datetime(df['order_date'])
df['revenue'] = df['quantity'] * df['unit_price']
df_completed = df[df['status'] == 'Completed']

# ANALYSIS 1: Total Revenue by Sales Rep
rep_revenue = df_completed.groupby('sales_rep')['revenue'].sum().sort_values(ascending=False)
print("=== TOTAL REVENUE BY SALES REP ===")
print(rep_revenue)
print()

# ANALYSIS 2: Revenue by Region
region_revenue = df_completed.groupby('region')['revenue'].sum().sort_values(ascending=False)
print("=== REVENUE BY REGION ===")
print(region_revenue)
print()

# ANALYSIS 3: Best Selling Product
product_revenue = df_completed.groupby('product')['revenue'].sum().sort_values(ascending=False)
print("=== REVENUE BY PRODUCT ===")
print(product_revenue)
print()

# ANALYSIS 4: Monthly Revenue Trend
df_completed['month'] = df_completed['order_date'].dt.to_period('M')
monthly_revenue = df_completed.groupby('month')['revenue'].sum()
print("=== MONTHLY REVENUE TREND ===")
print(monthly_revenue)
print()

# ANALYSIS 5: Order Status Breakdown
status_counts = df['status'].value_counts()
print("=== ORDER STATUS BREAKDOWN ===")
print(status_counts)
print()

# CREATE CHARTS FOLDER
os.makedirs('charts', exist_ok=True)

# Chart 1: Revenue by Sales Rep
plt.figure(figsize=(10, 5))
rep_revenue.plot(kind='bar', color=['#C85A1E','#3D3830','#8A8278','#2D6A4F','#C2CDFF'])
plt.title('Total Revenue by Sales Rep', fontsize=14, fontweight='bold')
plt.xlabel('Sales Rep')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/revenue_by_rep.png')
plt.close()
print("Chart 1 saved.")

# Chart 2: Revenue by Region
plt.figure(figsize=(8, 5))
region_revenue.plot(kind='bar', color=['#C85A1E','#2D6A4F','#3A5FCD','#8A8278'])
plt.title('Revenue by Region', fontsize=14, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/revenue_by_region.png')
plt.close()
print("Chart 2 saved.")

# Chart 3: Monthly Revenue Trend
plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind='line', marker='o', color='#C85A1E', linewidth=2.5, markersize=7)
plt.title('Monthly Revenue Trend', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/monthly_trend.png')
plt.close()
print("Chart 3 saved.")

# Chart 4: Order Status Pie
plt.figure(figsize=(7, 7))
status_counts.plot(kind='pie', autopct='%1.1f%%', colors=['#2D6A4F','#C85A1E','#8A8278'], startangle=90)
plt.title('Order Status Breakdown', fontsize=14, fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.savefig('charts/order_status.png')
plt.close()
print("Chart 4 saved.")

print()
print("All done! Check your charts folder.")
