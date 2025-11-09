# ☀️ SolarShift — Project Overview

SolarShift is a project we’ve been working on to understand the gap between **solar energy generation** and **electricity demand**.  
The main idea is to figure out how much extra solar capacity a region would need to run entirely on solar power.

This repo contains our work from **Week 1** and **Week 2**, covering everything from raw data collection to building predictive models.

---

## 🗂️ Week 1: Data Gathering & Cleaning

### 📘 What We Did
In the first week, our focus was mostly on **getting the data ready**.  
We collected hourly data for both energy demand and solar generation, cleaned it, and aggregated it to daily totals.

### ⚙️ Key Tasks

**Data Gathering**
- Pulled hourly datasets from multiple sources.  
- Ensured timestamps and units (kWh) were consistent.  
- Combined everything into a single dataset.  

**Data Cleaning**
- Dropped irrelevant columns like IDs and names.  
- Handled missing values using interpolation and forward/backward filling.  
- Converted timestamps to proper datetime format.  
- Aggregated hourly data into **daily totals** for analysis.  
- Filtered the dataset for **2018–2022** to make it uniform.

### 🧹 Cleaned Data Columns

| Column | Description |
|--------|------------|
| date | Date of measurement (daily total) |
| kWh | Total energy generated per day |
| Demand | Total daily energy demand |
| Solar_Generation | Daily solar energy generated |

### ⚙️ Tools We Used
Python, Pandas, NumPy, Matplotlib/Seaborn, GitHub (version control)

---

## 🗂️ Week 2: Forecasting & Model Evaluation

### 📘 What We Did
In Week 2, we focused on **forecasting**.  
We built models to predict solar energy generation and electricity demand on a daily basis.  
The goal was to capture patterns in both datasets using tree-based models.

### ⚙️ Tasks

**Feature Engineering**
- Extracted temporal features: `hour`, `month`, `dayofyear`, `season`, `timeofday`.  
- Added lag features: previous day, previous week, two-week lag.  
- Added rolling statistics (mean and standard deviation).  
- For demand, included `Temperature`, `Humidity`, and `is_weekend`.

**Model Training**
- Trained **Random Forest** and **XGBoost** models for both solar generation and demand.  
- Tuned parameters like tree depth, number of estimators, and learning rate.

**Model Evaluation**

| Model | MAE | RMSE | R² |
|-------|----:|----:|----:|
| Solar Generation | 93.04 | 149.03 | 0.805 |
| Electricity Demand | 150.11 | 205.61 | 0.979 |

**Observations**
- Solar forecasting did a good job but still shows **natural variability** (weather influence).  
- Demand forecasting is almost perfect — **daily usage is predictable**.

**Visualization**
- Feature importance plots to see which factors mattered most.  
- Actual vs Predicted plots to check model fit.  
- Residual/error distributions to identify where models were slightly off.  
- Compared trends across hours, months, and seasons.

---

### 🧠 Takeaways
- Lag and rolling features captured most temporal patterns.  
- Random Forest and XGBoost performed similarly — features dominate predictive power.  
- Demand forecasting is highly consistent; solar forecasting is influenced by external factors like weather.

---

### 🧭 Next Steps (Week 3)
- Combine solar and demand forecasts to calculate **daily deficit or surplus**.  
- Estimate additional **solar capacity** needed for 100% solar dependency.  
- Build dashboards to visualize **solar vs demand trends** and highlight peak deficit periods.

---

### 🧑‍💻 Author
**Rajnish Yadav**  
B.Tech CSE | Gurukul Kangri University  
Intern — Edunet Foundation | Shell (Green Energy Initiative)

