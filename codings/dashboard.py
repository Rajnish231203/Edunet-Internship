import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load datasets ---
df_demand = pd.read_csv('DemandEnergy.csv', parse_dates=['Timestamp'])
df_energy = pd.read_csv('SolarEnergy.csv', parse_dates=['date'])
df_combined = pd.read_csv('Demand&supply.csv', parse_dates=['date'])

st.title("Comprehensive Energy & Demand Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("Filters")

years = st.sidebar.multiselect(
    "Select Year(s):", 
    options=sorted(df_combined['year'].unique()), 
    default=sorted(df_combined['year'].unique())
)
months = st.sidebar.multiselect(
    "Select Month(s):", 
    options=sorted(df_combined['month'].unique()), 
    default=sorted(df_combined['month'].unique())
)
seasons = st.sidebar.multiselect(
    "Select Season(s):", 
    options=df_combined['season'].unique(), 
    default=df_combined['season'].unique()
)

# Map numeric timeofday to label
timeofday_map = {0: 'Night', 1: 'Morning', 2: 'Afternoon', 3: 'Evening'}
df_energy['timeofday_label'] = df_energy['timeofday'].map(timeofday_map)

timeofday_selected = st.sidebar.multiselect(
    "Select Time of Day:",
    options=df_energy['timeofday_label'].unique(),
    default=df_energy['timeofday_label'].unique()
)

# --- Filtering data ---
filtered_combined = df_combined[
    (df_combined['year'].isin(years)) &
    (df_combined['month'].isin(months)) &
    (df_combined['season'].isin(seasons))
]

filtered_energy = df_energy[
    (df_energy['year'].isin(years)) &
    (df_energy['month'].isin(months)) &
    (df_energy['timeofday_label'].isin(timeofday_selected))
]

# --- KPIs in two rows ---
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Energy Generated", f"{filtered_combined['EnergyMWh'].sum():,.0f} MW")
col2.metric("Total Demand", f"{filtered_combined['DemandMW'].sum():,.0f} MW")
col3.metric("Total Deficit", f"{filtered_combined['DeficitMW'].sum():,.0f} MW")

col4, col5 = st.columns(2)
col4.metric("Peak Demand", f"{filtered_combined['DemandMW'].max():,.0f} MW")
col5.metric("Peak Energy", f"{filtered_combined['EnergyMWh'].max():,.0f} MW")

# --- Time Series ---
st.subheader("Time Series: Demand, Energy & Deficit")
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(filtered_combined['date'], filtered_combined['DemandMW'], label='DemandMW', color='blue')
ax.plot(filtered_combined['date'], filtered_combined['EnergyMWh'], label='EnergyMWh', color='orange')
ax.plot(filtered_combined['date'], filtered_combined['DeficitMW'], label='DeficitMW', color='red')
ax.fill_between(filtered_combined['date'], filtered_combined['EnergyMWh'], filtered_combined['DemandMW'], color='red', alpha=0.2)
ax.set_xlabel('Date')
ax.set_ylabel('MW')
ax.legend()
st.pyplot(fig)

# --- Monthly Averages ---
st.subheader("Monthly Average Energy vs Demand vs Deficit")
monthly_avg = filtered_combined.groupby('month')[['EnergyMWh','DemandMW','DeficitMW']].mean().reset_index()
fig, ax = plt.subplots(figsize=(12,5))
bar_width = 0.25
x = range(len(monthly_avg))
ax.bar([i - bar_width for i in x], monthly_avg['EnergyMWh'], width=bar_width, color='orange', label='EnergyMWh')
ax.bar(x, monthly_avg['DemandMW'], width=bar_width, color='blue', label='DemandMW')
ax.bar([i + bar_width for i in x], monthly_avg['DeficitMW'], width=bar_width, color='red', label='DeficitMW')
ax.set_xticks(x)
ax.set_xticklabels(monthly_avg['month'])
ax.set_xlabel('Month')
ax.set_ylabel('MW')
ax.legend()
st.pyplot(fig)

# --- Yearly Averages ---
st.subheader("Yearly Average Energy vs Demand vs Deficit")
yearly_avg = filtered_combined.groupby('year')[['EnergyMWh','DemandMW','DeficitMW']].mean().reset_index()
fig, ax = plt.subplots(figsize=(12,5))
x = range(len(yearly_avg))
ax.bar([i - bar_width for i in x], yearly_avg['EnergyMWh'], width=bar_width, color='orange', label='EnergyMWh')
ax.bar(x, yearly_avg['DemandMW'], width=bar_width, color='blue', label='DemandMW')
ax.bar([i + bar_width for i in x], yearly_avg['DeficitMW'], width=bar_width, color='red', label='DeficitMW')
ax.set_xticks(x)
ax.set_xticklabels(yearly_avg['year'])
ax.set_xlabel('Year')
ax.set_ylabel('MW')
ax.legend()
st.pyplot(fig)

# --- Seasonal Boxplots ---
st.subheader("Seasonal Distribution of Deficit & Energy")
fig, ax = plt.subplots(figsize=(12,5))
sns.boxplot(x='season', y='DeficitMW', data=filtered_combined, order=['Winter','Summer','Monsoon'], ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12,5))
sns.boxplot(x='season', y='EnergyMWh', data=filtered_combined, order=['Winter','Summer','Monsoon'], ax=ax)
st.pyplot(fig)

# --- Time of Day Energy Analysis ---
st.subheader("Average Energy Generation by Time of Day")
timeofday_avg = filtered_energy.groupby('timeofday_label')['energy_Generated'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x='timeofday_label', y='energy_Generated', data=timeofday_avg, palette='viridis', ax=ax)
ax.set_ylabel("Average Energy Generated (MW)")
ax.set_xlabel("Time of Day")
st.pyplot(fig)
