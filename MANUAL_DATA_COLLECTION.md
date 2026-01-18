# Manual Data Collection Instructions for FT 2025

## Issue
The FT website (https://www.ft.com/content/cb3e317e-e3cc-4e4a-a506-b755b2f94bb1) has JavaScript-based protection that prevents automated scraping.

## Solution Options

### Option 1: Manual Browser Access
1. Open the FT article in a browser: https://www.ft.com/content/cb3e317e-e3cc-4e4a-a506-b755b2f94bb1
2. If you have FT subscription access, log in
3. Look for a "Download" or "Export" option for the company data
4. Save as CSV or copy the table data

### Option 2: FT1000 Listing Page
1. Try accessing: https://www.ft.com/ft1000-2025
2. Look for the full company ranking table
3. Use browser developer tools (F12) to inspect network requests
4. Look for API calls or data files (JSON/CSV) that contain the company data

### Option 3: Copy Table from Browser
1. Access the article/listing page in browser
2. Select and copy the full company table
3. Paste into a spreadsheet (Excel/Google Sheets)
4. Export as CSV to: `~/Projects/FT-Europe-Analysis-2025/data/ft1000_2025_raw.csv`

## Required Data Fields
Based on existing notebooks, we need:
- Rank
- Company Name
- Country
- Industry/Category
- Absolute Growth Rate (%)
- Revenue (2023 or latest year)
- Number of Employees
- Compound Annual Growth Rate (CAGR)

## Once Data is Collected
Run: `python3 process_2025_data.py` (to be created)
