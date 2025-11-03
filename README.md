# ☀️ SolarShift — Week 1: Data Gathering & Cleaning

## 📘 Project Overview

**SolarShift** is a data-driven project focused on analyzing the gap between **solar energy generation** and **energy demand**.
The goal is to estimate how much additional solar capacity is needed to make a region **fully dependent on solar energy**.

This repository contains the work for **Week 1**, which includes **data gathering, preprocessing, and cleaning** of raw energy datasets.

---

## 🗂️ Week 1 Tasks

### 1. Data Gathering

* Collected hourly-level data of **energy demand** and **solar generation**.
* Merged data from multiple sources into a single structured dataset.
* Verified consistency in timestamps and measurement units (kWh).

### 2. Data Cleaning

* Removed irrelevant or duplicate columns (like ID, name, etc.).
* Handled missing values using interpolation and forward/backward filling.
* Converted timestamps into proper `datetime` format.
* Aggregated hourly data to **daily energy totals** for further analysis.
* Filtered data between **2018 to 2022** for uniformity.

---

## 🧹 Cleaned Data Description

| Column             | Description                            |
| ------------------ | -------------------------------------- |
| `date`             | Date of measurement (daily aggregated) |
| `kWh`              | Total energy generated per day         |
| `Demand`           | Total daily energy demand              |
| `Solar_Generation` | Total daily solar energy generated     |

---

## ⚙️ Tools & Libraries Used

* **Python**
* **Pandas**, **NumPy**
* **Matplotlib / Seaborn** (for visualization - upcoming)
* **GitHub** (for version control)

---

## 📅 Next Steps (Week 2)

* Perform **solar vs demand comparison**.
* Calculate **solar deficit or surplus**.
* Build an analytical model to predict **required solar generation** for 100% coverage.
* Visualize energy dependency trends.

---

## 🧑‍💻 Author

**Rajnish Yadav**
B.Tech CSE | Gurukul Kangri University
*Intern — Edunet Foundation | Shell (Green Energy Initiative)*

