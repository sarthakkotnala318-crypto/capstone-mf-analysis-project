\# Bluestock Mutual Fund Analytics Capstone



\## Project Overview



This project analyzes Indian mutual fund data to understand fund performance, investor behavior, SIP trends, market trends, and portfolio risk.



The project covers data ingestion, data cleaning, SQL database design, exploratory data analysis, performance analytics, Power BI dashboard development, and advanced risk analytics.



\## Objectives



\- Build an ETL pipeline for mutual fund data.

\- Clean and validate financial datasets.

\- Store structured data in a SQLite database.

\- Perform exploratory data analysis.

\- Calculate fund performance and risk metrics.

\- Analyze investor and SIP behavior.

\- Build an interactive Power BI dashboard.

\- Develop advanced analytics including VaR, CVaR, rolling Sharpe, cohort analysis, SIP continuity, recommender logic, and HHI.



\## Data Sources



The project uses mutual fund datasets covering:



\- Fund master information

\- NAV history

\- Investor transactions

\- Portfolio holdings

\- Scheme performance

\- AUM by fund house

\- Monthly SIP inflows

\- Category inflows

\- Industry folio counts

\- Benchmark indices



Live NAV data for selected schemes was also retrieved from the MFAPI service.



\## Project Structure



```text

capstone-mf-analysis-project/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── notebooks/

│   ├── Day 1 data ingestion

│   ├── Data cleaning and SQL analysis

│   ├── EDA

│   ├── Performance analytics

│   └── Advanced analytics

│

├── dashboard/

│   ├── bluestock\_mf\_dashboard.pbix

│   ├── bluestock\_mf\_dashboard.pdf

│   └── screenshots/

│

├── reports/

│   ├── Final\_Report.pdf

│   ├── Presentation.pptx

│   └── analysis charts

│

├── sql/

│   └── SQLite database and SQL files

│

├── data\_ingestion.py

├── data\_quality\_check.py

├── fund\_master\_exploration.py

├── live\_nav\_fetch.py

├── run\_pipeline.py

├── requirements.txt

└── README.md

