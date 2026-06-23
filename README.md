# E-Commerce Sales Performance & Analytics

An end-to-end data analytics project transforming 128k+ records into actionable business insights. This repository features an automated data cleaning pipeline built in Python and an interactive Power BI executive dashboard tracking key retail metrics.

## Project Architecture
1. **Data Cleaning (Python):** Developed an automated script using `Pandas` to handle operational anomalies, impute missing values, drop structural noise, and optimize data types.
2. **Business Intelligence (Power BI):** Engineered an interactive data model to track key performance indicators (KPIs), geographical distributions, and categorical purchasing trends.

## Data Source Note
> **Note on Datasets:** Due to GitHub's browser file size limitations (>25MB), the raw and cleaned CSV datasets (`E-Commerce Dataset.csv` and `E-Commerce Cleaned Dataset.csv`) are hosted externally. 
> 
> The source data can be downloaded directly from Kaggle: [Unlock Profits with E-Commerce Sales Data](https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data)

## Repository Contents
* `Cleaning.py`: The production Python script executing data manipulation, handling null fields, dropping metadata columns, and parsing dates.
* `E-Commerce Data Dashboard.pbix`: The compiled Power BI dashboard file including data relationships, DAX measures, and visual layouts.

## Data Quality & ETL Enhancements
Using Python, the following pipeline operations were systematically executed:
* Removed redundant tracking columns (`index` and `Unnamed: 22`).
* Handled missing target fields (imputed missing financial fields to `0` and missing categorical strings to `'Unknown'`).
* Formatted chronological string values safely into standardized datetime objects.

## Tools & Technologies Used
* **Data Engineering & Pipeline:** Python 3.x, Pandas
* **Business Intelligence (BI):** Microsoft Power BI (DAX, Data Modeling, Data Visualization)
