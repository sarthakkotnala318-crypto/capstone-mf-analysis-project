
# Mutual Fund Analytics — Data Dictionary

## Project Overview

This data dictionary documents the datasets, columns, data types,
business definitions, and source references used in the Mutual Fund
Analytics Capstone Project.

---

## 1. nav_history

**Source:** `nav_history.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identifier | nav_history.csv |
| date | DATE | NAV date | nav_history.csv |
| nav | REAL | Net Asset Value of the mutual fund on the given date | nav_history.csv |

---

## 2. investor_transactions

**Source:** `investor_transactions.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| investor_id | TEXT | Unique investor identifier | investor_transactions.csv |
| transaction_date | DATE | Date on which the transaction occurred | investor_transactions.csv |
| amfi_code | INTEGER | AMFI scheme identifier associated with the transaction | investor_transactions.csv |
| transaction_type | TEXT | Type of transaction: SIP, Lumpsum, or Redemption | investor_transactions.csv |
| amount_inr | REAL | Transaction amount in Indian Rupees | investor_transactions.csv |
| state | TEXT | State associated with the investor | investor_transactions.csv |
| city | TEXT | City associated with the investor | investor_transactions.csv |
| city_tier | TEXT | Classification of the investor's city by tier | investor_transactions.csv |
| age_group | TEXT | Age-group category of the investor | investor_transactions.csv |
| gender | TEXT | Gender category of the investor | investor_transactions.csv |
| annual_income_lakh | REAL | Investor annual income in lakh INR | investor_transactions.csv |
| payment_mode | TEXT | Mode used to make the transaction | investor_transactions.csv |
| kyc_status | TEXT | KYC verification status of the investor | investor_transactions.csv |

---

## 3. scheme_performance

**Source:** `scheme_performance.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identifier | scheme_performance.csv |
| scheme_name | TEXT | Name of the mutual fund scheme | scheme_performance.csv |
| fund_house | TEXT | Mutual fund company/asset management company | scheme_performance.csv |
| category | TEXT | Broad mutual fund category | scheme_performance.csv |
| plan | TEXT | Fund plan type | scheme_performance.csv |
| return_1yr_pct | REAL | One-year return percentage | scheme_performance.csv |
| return_3yr_pct | REAL | Three-year return percentage | scheme_performance.csv |
| return_5yr_pct | REAL | Five-year return percentage | scheme_performance.csv |
| benchmark_3yr_pct | REAL | Three-year benchmark return percentage | scheme_performance.csv |
| alpha | REAL | Alpha measure of fund performance | scheme_performance.csv |
| beta | REAL | Beta measure of market sensitivity | scheme_performance.csv |
| sharpe_ratio | REAL | Sharpe ratio measuring risk-adjusted return | scheme_performance.csv |
| sortino_ratio | REAL | Sortino ratio measuring downside-risk-adjusted return | scheme_performance.csv |
| std_dev_ann_pct | REAL | Annualized standard deviation percentage | scheme_performance.csv |
| max_drawdown_pct | REAL | Maximum observed drawdown percentage | scheme_performance.csv |
| aum_crore | REAL | Assets under management in crore INR | scheme_performance.csv |
| expense_ratio_pct | REAL | Fund expense ratio percentage | scheme_performance.csv |
| morningstar_rating | INTEGER | Morningstar rating assigned to the scheme | scheme_performance.csv |
| risk_grade | TEXT | Risk classification of the mutual fund scheme | scheme_performance.csv |

---

## 4. fund_master

**Source:** `fund_master.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identifier | fund_master.csv |
| fund_house | TEXT | Mutual fund company/asset management company | fund_master.csv |
| scheme_name | TEXT | Name of the mutual fund scheme | fund_master.csv |
| category | TEXT | Broad mutual fund category | fund_master.csv |
| sub_category | TEXT | More specific fund classification | fund_master.csv |
| plan | TEXT | Fund plan type | fund_master.csv |
| launch_date | DATE | Scheme launch date | fund_master.csv |
| benchmark | TEXT | Benchmark associated with the scheme | fund_master.csv |
| expense_ratio_pct | REAL | Expense ratio percentage | fund_master.csv |
| exit_load_pct | REAL | Exit load percentage | fund_master.csv |
| min_sip_amount | REAL | Minimum SIP investment amount | fund_master.csv |
| min_lumpsum_amount | REAL | Minimum lumpsum investment amount | fund_master.csv |
| fund_manager | TEXT | Fund manager associated with the scheme | fund_master.csv |
| risk_category | TEXT | Risk classification of the scheme | fund_master.csv |
| sebi_category_code | TEXT | SEBI category code | fund_master.csv |

---

## 5. portfolio_holdings

**Source:** `portfolio_holdings.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| amfi_code | INTEGER | AMFI scheme identifier | portfolio_holdings.csv |
| scheme_name | TEXT | Mutual fund scheme name | portfolio_holdings.csv |
| holding_date | DATE | Portfolio holding date | portfolio_holdings.csv |
| company_name | TEXT | Company/security held by the fund | portfolio_holdings.csv |
| sector | TEXT | Sector of the holding | portfolio_holdings.csv |
| holding_pct | REAL | Percentage of portfolio invested in the holding | portfolio_holdings.csv |
| market_value_crore | REAL | Market value of the holding in crore INR | portfolio_holdings.csv |
| rank | INTEGER | Rank of the holding within the portfolio | portfolio_holdings.csv |

---

## 6. benchmark_indices

**Source:** `benchmark_indices.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| index_name | TEXT | Name of the benchmark index | benchmark_indices.csv |
| date | DATE | Index observation date | benchmark_indices.csv |
| index_value | REAL | Benchmark index value on the given date | benchmark_indices.csv |

---

## 7. aum_by_fund_house

**Source:** `aum_by_fund_house.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| date | DATE | Reporting date | aum_by_fund_house.csv |
| fund_house | TEXT | Mutual fund company/asset management company | aum_by_fund_house.csv |
| aum_lakh_crore | REAL | Assets under management in lakh crore INR | aum_by_fund_house.csv |
| aum_crore | REAL | Assets under management in crore INR | aum_by_fund_house.csv |
| num_schemes | INTEGER | Number of schemes managed by the fund house | aum_by_fund_house.csv |

---

## 8. monthly_sip_inflows

**Source:** `monthly_sip_inflows.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| month | DATE | Month of SIP inflow | monthly_sip_inflows.csv |
| sip_inflow_crore | REAL | SIP inflow amount in crore INR | monthly_sip_inflows.csv |
| sip_accounts_lakh | REAL | Number of SIP accounts in lakh | monthly_sip_inflows.csv |
| average_sip_amount | REAL | Average SIP amount | monthly_sip_inflows.csv |
| yoy_growth_pct | REAL | Year-over-year SIP growth percentage | monthly_sip_inflows.csv |
| contribution_pct | REAL | SIP contribution percentage | monthly_sip_inflows.csv |

---

## 9. category_inflows

**Source:** `category_inflows.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| month | DATE | Month of reported inflow | category_inflows.csv |
| category | TEXT | Mutual fund category | category_inflows.csv |
| inflow_crore | REAL | Inflow amount in crore INR | category_inflows.csv |

---

## 10. industry_folio_count

**Source:** `industry_folio_count.csv`

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| month | DATE | Reporting month | industry_folio_count.csv |
| category | TEXT | Mutual fund category | industry_folio_count.csv |
| folios_lakh | REAL | Number of folios in lakh | industry_folio_count.csv |
| net_change_lakh | REAL | Net change in folios in lakh | industry_folio_count.csv |
| growth_pct | REAL | Growth percentage | industry_folio_count.csv |
| share_pct | REAL | Category share percentage | industry_folio_count.csv |

---

# SQL Star Schema Reference

The SQLite database contains the following tables:

- `dim_fund` — Fund/scheme master dimension
- `dim_date` — Date dimension
- `fact_nav` — Historical NAV observations
- `fact_transactions` — Investor transactions
- `fact_performance` — Fund performance metrics
- `fact_aum` — Fund-house AUM information

## Primary Relationships

- `dim_fund.amfi_code` → fund identifier
- `dim_date.date` → date identifier
- `fact_nav.amfi_code` → `dim_fund.amfi_code`
- `fact_nav.date` → `dim_date.date`
- `fact_transactions.amfi_code` → `dim_fund.amfi_code`
- `fact_transactions.transaction_date` → `dim_date.date`
- `fact_performance.amfi_code` → `dim_fund.amfi_code`
- `fact_aum.date` → `dim_date.date`

---

## Data Cleaning Reference

The following datasets received detailed cleaning and validation during Day 2:

1. `nav_history.csv`
2. `investor_transactions.csv`
3. `scheme_performance.csv`

Cleaning included date parsing, duplicate checks, numeric validation, transaction-type validation, KYC validation, and expense-ratio validation as applicable.

