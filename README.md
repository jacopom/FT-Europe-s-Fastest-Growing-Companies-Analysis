# Financial Times - Europe’s fastest-growing companies

Europe’s fastest-growing companies [report](https://www.ft.com/ft1000-2023) lists the European companies that achieved the highest compound annual growth rate in revenue.

I was curious to explore better some aspects of this reports, like the possible correlation between growth and employees number, or industrial categories that have grown more in my country.

Python notebook with my analysis is available here:
- [2020](https://github.com/jacopom/FT-Europe-s-Fastest-Growing-Companies-Analysis/blob/master/EuropesFastestGrowingCompanies2020.ipynb)
- [2021](https://github.com/jacopom/FT-Europe-s-Fastest-Growing-Companies-Analysis/blob/master/EuropesFastestGrowingCompanies2021.ipynb)
- [2024](https://github.com/jacopom/FT-Europe-s-Fastest-Growing-Companies-Analysis/blob/master/EuropesFastestGrowingCompanies2024.ipynb)
- [2025](https://github.com/jacopom/FT-Europe-s-Fastest-Growing-Companies-Analysis/blob/master/EuropesFastestGrowingCompanies2025.ipynb) - *In Progress* (see STATUS_REPORT.md)

![Number of italian companies by category](/italianCompaniesByCategory.png)

## 2025 Update
The 2025 analysis framework is prepared and ready. Due to FT website access restrictions (JavaScript protection/paywall), data must be collected manually. See [MANUAL_DATA_COLLECTION.md](MANUAL_DATA_COLLECTION.md) for instructions and [STATUS_REPORT.md](STATUS_REPORT.md) for current status.

Website table data is scraped using BeautifulSoup (2020-2024). 
Pandas, Matplotlib and Seaborn are used data visualization.

###### The full report featuring case studies and analysis from this year’s ranking is available [here](https://www.ft.com/reports/europes-fastest-growing-companies).
