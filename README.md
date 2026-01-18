# Financial Times - Europe's fastest-growing companies

Europe's fastest-growing companies [report](https://www.ft.com/ft1000-2023) lists the European companies that achieved the highest compound annual growth rate in revenue.

I was curious to explore better some aspects of these reports, like the possible correlation between growth and employees number, or industrial categories that have grown more in my country.

## Analysis by Year

Python notebook with my analysis is available here:
- [2020](https://github.com/jacopom/FT-Europe-s-Fastest-Growing-Companies-Analysis/blob/master/EuropesFastestGrowingCompanies2020.ipynb)
- [2021](https://github.com/jacopom/FT-Europe-s-Fastest-Growing-Companies-Analysis/blob/master/EuropesFastestGrowingCompanies2021.ipynb)
- [2024](https://github.com/jacopom/FT-Europe-s-Fastest-Growing-Companies-Analysis/blob/master/EuropesFastestGrowingCompanies2024.ipynb)
- [2025](https://github.com/jacopom/FT-Europe-s-Fastest-Growing-Companies-Analysis/blob/master/EuropesFastestGrowingCompanies2025.ipynb)

## 2025 Key Findings

**1,000 companies analyzed** | **Average CAGR: 84.6%** | **Data source:** [FT 2025 Report](https://www.ft.com/content/cb3e317e-e3cc-4e4a-a506-b755b2f94bb1)

### 🏆 Top Countries
1. 🇮🇹 **Italy** - 338 companies (33.8%)
2. 🇩🇪 Germany - 158 companies (15.8%)
3. 🇫🇷 France - 145 companies (14.5%)
4. 🇬🇧 UK - 133 companies (13.3%)
5. 🇳🇱 Netherlands - 53 companies (5.3%)

### 🏢 Top Sectors
1. IT & Software - 200 companies
2. Construction & Engineering - 117 companies
3. Energy & Utilities - 74 companies

### 🇮🇹 Italy Highlights
- **#1 in Europe** with 338 companies (33.8% of total)
- Average CAGR: 82.0%
- Top sector: Construction & Engineering (81 companies)
- **4 Italian companies in Top 10** overall rankings

📊 **Full analysis with charts:** [ANALYSIS_SUMMARY_2025.md](ANALYSIS_SUMMARY_2025.md)

![Number of italian companies by category](/italianCompaniesByCategory.png)

## Repository Structure

```
├── data/
│   ├── ft1000_2020.csv
│   ├── ft1000_2021.csv
│   ├── ft1000_2024.csv
│   └── ft1000_2025.csv          # Latest
├── output/
│   ├── countries_distribution_2025.png
│   ├── sectors_distribution_2025.png
│   ├── italy_sectors_2025.png
│   └── cagr_distribution_2025.png
├── EuropesFastestGrowingCompanies2020.ipynb
├── EuropesFastestGrowingCompanies2021.ipynb
├── EuropesFastestGrowingCompanies2024.ipynb
├── EuropesFastestGrowingCompanies2025.ipynb
└── ANALYSIS_SUMMARY_2025.md     # Detailed findings
```

## Technical Stack

Website table data is scraped using BeautifulSoup (2020-2024) or manually collected (2025).
Pandas, Matplotlib and Seaborn are used for data analysis and visualization.

###### The full report featuring case studies and analysis from this year's ranking is available [here](https://www.ft.com/reports/europes-fastest-growing-companies).
