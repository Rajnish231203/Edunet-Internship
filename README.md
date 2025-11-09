☀️ SolarShift — Project Overview

SolarShift is a project we’ve been working on to understand the gap between solar energy generation and electricity demand.
The main idea is to figure out how much extra solar capacity a region would need to run entirely on solar power.

This repo contains our work from Week 1 and Week 2, covering everything from raw data collection to building predictive models.

🗂️ Week 1: Data Gathering & Cleaning
📘 What We Did

In the first week, our focus was mostly on getting the data ready.
We collected hourly data for both energy demand and solar generation, cleaned it up, and aggregated it to daily totals.

⚙️ Key Tasks

Data Gathering:

Pulled hourly datasets from multiple sources.

Made sure timestamps and units (kWh) were consistent.

Combined everything into a single dataset.

Data Cleaning:

Dropped irrelevant columns like IDs and names.

Handled missing values using interpolation and forward/backward filling.

Converted timestamps to proper datetime format.

Aggregated hourly data into daily totals for analysis.

Filtered the dataset for 2018–2022 to make it uniform.

🧹 Cleaned Data Columns
Column	Description
date	Date of measurement (daily total)
kWh	Total energy generated per day
Demand	Total daily energy demand
Solar_Generation	Daily solar energy generated
⚙️ Tools We Used

Python, Pandas, NumPy, Matplotlib/Seaborn (for visualization), GitHub for version control.

🗂️ Week 2: Forecasting & Model Evaluation
📘 What We Did

In Week 2, we jumped into forecasting.
We built models to predict solar energy generation and electricity demand on a daily basis.
The idea was to see how well we could capture patterns in both datasets using tree-based models.

⚙️ Tasks

Feature Engineering:

Extracted temporal features: hour, month, dayofyear, season, timeofday.

Added lag features (previous day, previous week, two-week lag).

Added rolling statistics (mean and standard deviation over past day).

For demand, we also included Temperature, Humidity, and is_weekend, which seemed important.

Model Training:

Trained Random Forest and XGBoost models for both solar generation and demand.

Tuned parameters like tree depth, number of estimators, and learning rate for better performance.

Model Evaluation:

Model	MAE	RMSE	R²
Solar Generation	93.04	149.03	0.805
Electricity Demand	150.11	205.61	0.979

What We Observed:

Solar forecasting did a good job overall but still shows natural variability — probably because solar depends on weather.

Demand forecasting was almost perfect — daily usage patterns are very predictable.

Visualization:

Plotted feature importance to see which factors mattered most.

Created Actual vs Predicted plots to check how well the models tracked reality.

Looked at residual/error distributions to see where models were slightly off.

Compared trends across hours, months, and seasons for deeper insights.

🧠 Takeaways

Our lag and rolling features really helped capture patterns — without them, performance drops a lot.

Random Forest and XGBoost gave very similar results, which shows that the features themselves already explain most of the signal.

Demand forecasting is solid; solar forecasting is more affected by external factors like weather.

🧭 Next Steps (Week 3)

Combine solar and demand forecasts to calculate daily deficit or surplus.

Figure out how much extra solar capacity is needed for 100% solar dependency.

Create dashboards to visualize solar vs demand trends over time, highlighting peak deficit periods.

## 🧑‍💻 Author

**Rajnish Yadav**
B.Tech CSE | Gurukul Kangri University
*Intern — Edunet Foundation | Shell (Green Energy Initiative)*

