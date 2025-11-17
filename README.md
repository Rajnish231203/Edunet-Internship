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

Here you go — **Week 3 updated with the exact insights you mentioned**, written in the same format, tone, structure, and style as your Week 1 & Week 2 sections.
Nothing else has been touched.

---

## 🗂️ Week 3: Gap Analysis & Solar Capacity Insights

### 📘 What We Did

Week 3 focused on combining both forecasting outputs and understanding the **actual gap** between predicted solar generation and predicted electricity demand.
This allowed us to quantify how much solar capacity the region truly needs.

### ⚙️ Key Tasks

**1. Forecast Integration**

* Merged solar and demand predictions into a single dataset.
* Calculated daily surplus/deficit using:
  `Gap = Predicted_Solar_Generation – Predicted_Demand`

**2. Gap Analysis**

* Identified deficit days, surplus days, and seasonal imbalance.
* Computed cumulative unmet energy across the entire period.
* Highlighted months where solar consistently fails to meet demand.

**3. Capacity Requirement Estimation**

* Converted total deficit into required additional solar kWh.
* Estimated the **MW of solar capacity** needed to bridge the gap.
* Simulated multiple capacity scenarios (10%, 25%, 50% increase).

**4. Dashboard Integration**

* Added deficit/surplus indicators to the Streamlit app.
* Added a comparison graph showing predicted solar vs predicted demand.
* Displayed estimated capacity requirement as a final summary output.

---

### 🔍 Key Insights

* Solar generation is extremely low compared to consumption — **only 4–5% of total daily demand is met through solar energy**.
* This gap remains consistent across most months, even during high solar periods.
* Demand peaks in evenings, while solar peaks midday, creating time-based mismatch.
* Winter and monsoon months show the **highest deficits**, with solar dropping sharply.
* Even on best-performing days, solar generation never reaches close to demand levels.
* To achieve full solar dependency, **a significant increase in installed solar capacity** is required, far beyond the current baseline.

---

### 📊 Performance Summary

| Task                           | Best Model | RMSE   | R²    |
| ------------------------------ | ---------- | ------ | ----- |
| Solar Energy Forecasting       | XGBoost    | 149.03 | 0.805 |
| Electricity Demand Forecasting | XGBoost    | 205.61 | 0.979 |

---

### 🧑‍💻 Author
**Rajnish Yadav**  
B.Tech CSE | Gurukul Kangri University  
Intern — Edunet Foundation | Shell (Green Energy Initiative)

