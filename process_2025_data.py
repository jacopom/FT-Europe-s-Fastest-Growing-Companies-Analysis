#!/usr/bin/env python3
"""
Process FT1000 2025 data from manually collected source.

Usage:
    python3 process_2025_data.py <input_file.csv>
    
The script will:
1. Read the raw data
2. Clean and standardize column names
3. Handle missing values
4. Save processed data to data/ft1000_2025.csv
"""

import pandas as pd
import sys
import os

def clean_column_names(df):
    """Standardize column names based on FT1000 format."""
    # Common variations of column names
    column_mapping = {
        'rank': 'Rank',
        'company name': 'Company',
        'company': 'Company',
        'country': 'Country',
        'industry': 'Category',
        'category': 'Category',
        'sector': 'Category',
        'absolute growth rate': 'AbsoluteGrowthRate',
        'absolute growth rate (%)': 'AbsoluteGrowthRate',
        'growth rate': 'AbsoluteGrowthRate',
        'revenue': 'Revenue2023',
        'revenue 2023': 'Revenue2023',
        'revenue (€m)': 'Revenue2023',
        'employees': 'Employees',
        'number of employees': 'Employees',
        'cagr': 'CAGR',
        'compound annual growth rate': 'CAGR',
        'cagr (%)': 'CAGR',
    }
    
    # Rename columns
    df.columns = df.columns.str.lower().str.strip()
    df.rename(columns=column_mapping, inplace=True)
    
    return df

def clean_numeric_values(df):
    """Clean numeric columns by removing % signs, commas, etc."""
    numeric_columns = ['Rank', 'AbsoluteGrowthRate', 'Revenue2023', 'Employees', 'CAGR']
    
    for col in numeric_columns:
        if col in df.columns:
            # Convert to string first, handle None/NaN
            df[col] = df[col].astype(str)
            
            # Remove % signs and commas
            df[col] = df[col].str.replace('%', '').str.replace(',', '').str.strip()
            
            # Replace 'n/a', 'nan', empty strings with NaN
            df[col] = df[col].replace(['n/a', 'nan', '', 'None'], pd.NA)
            
            # Convert to numeric
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df

def process_data(input_file):
    """Main processing function."""
    print(f"Reading data from: {input_file}")
    
    # Read the data
    df = pd.read_csv(input_file)
    print(f"Initial shape: {df.shape}")
    print(f"Initial columns: {df.columns.tolist()}")
    
    # Clean column names
    df = clean_column_names(df)
    print(f"\nStandardized columns: {df.columns.tolist()}")
    
    # Clean numeric values
    df = clean_numeric_values(df)
    
    # Check for required columns
    required_columns = ['Rank', 'Company', 'Country', 'Category']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"\nWARNING: Missing required columns: {missing_columns}")
        print("Please check your data format.")
        return None
    
    # Display summary statistics
    print(f"\nProcessed shape: {df.shape}")
    print(f"\nSummary statistics:")
    print(df.describe())
    
    print(f"\nTop 10 companies by growth rate:")
    if 'AbsoluteGrowthRate' in df.columns:
        print(df.nlargest(10, 'AbsoluteGrowthRate')[['Rank', 'Company', 'Country', 'Category', 'AbsoluteGrowthRate']])
    
    # Save processed data
    output_file = 'data/ft1000_2025.csv'
    df.to_csv(output_file, index=False)
    print(f"\n✓ Processed data saved to: {output_file}")
    
    return df

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 process_2025_data.py <input_file.csv>")
        print("\nExample: python3 process_2025_data.py data/ft1000_raw_2025.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    df = process_data(input_file)
    
    if df is not None:
        print("\n✓ Processing complete!")
        print("\nNext steps:")
        print("  1. Review the processed data: data/ft1000_2025.csv")
        print("  2. Run the analysis notebook: jupyter notebook EuropesFastestGrowingCompanies2025.ipynb")
