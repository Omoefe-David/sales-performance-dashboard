# Sales Performance Dashboard

A complete end-to-end data analysis project analyzing sales performance across reps, regions, and products using SQL, Python, and data visualization.

---

## Project Overview

This project analyzes 30 sales transactions across 5 sales representatives and 4 Nigerian regions (Lagos, Abuja, Enugu, Port Harcourt) over a 5-month period (January–May 2024). The goal was to identify top performers, revenue trends, and areas for improvement.

---

## Tools Used

- **Python** (Pandas, Matplotlib) — data cleaning and chart generation
- **SQL** (SQLite) — business queries and aggregations
- **Excel / CSV** — raw data storage

---

## Key Findings

| Metric | Result |
|---|---|
| Top Sales Rep | David Omoefe — 16,650 in revenue |
| Top Region | Lagos — 16,650 in revenue |
| Best Product | Software License — 22,950 total revenue |
| Completion Rate | 76.7% of orders completed |
| Cancellation Rate | 13.3% of orders cancelled |
| Revenue Growth | January (6,750) → April (10,450) — 55% growth |

---

## SQL Analysis

Four business queries were written to answer key questions:

1. **Who are the top performing sales reps?**
2. **Which region generates the most revenue?**
3. **Which product sells the most?**
4. **What is the order completion vs cancellation rate?**

See `queries.sql` for full query code.

---

## Python Analysis

The `analysis.py` script:
- Loads and cleans the raw CSV data
- Calculates revenue per rep, region, and product
- Generates 4 charts saved in the `/charts` folder

---

## Charts Generated

- `revenue_by_rep.png` — Bar chart of revenue per sales rep
- `revenue_by_region.png` — Bar chart of revenue per region
- `monthly_trend.png` — Line chart of monthly revenue growth
- `order_status.png` — Pie chart of order status breakdown

---

## Project Structure

```
sales-dashboard/
├── sales_data.csv        # Raw dataset (30 records)
├── analysis.py           # Python analysis script
├── queries.sql           # SQL business queries
├── README.md             # Project documentation
└── charts/
    ├── revenue_by_rep.png
    ├── revenue_by_region.png
    ├── monthly_trend.png
    └── order_status.png
```

---

## About

Built by **David Omoefe** — Data Analyst with expertise in SQL, Python, Power BI, and Excel.

- Portfolio: https://omoefe-david.github.io/David_Omoefe.github.io/
- LinkedIn: https://www.linkedin.com/in/david-omoefe-051b70282?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
- Email: othukeomoefe@gmail.com
