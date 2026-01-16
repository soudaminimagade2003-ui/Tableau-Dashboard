## 1️. Project Title

**Investment Portfolio Intelligence Dashboard**
*A role-based, data-driven portfolio analysis system combining Python automation and advanced Tableau visualization*

---

## 2️. Problem Statement

In traditional investment advisory processes, investor decisions are often based on:

* Gut feeling
* Generic asset allocation advice
* Static return assumptions

This creates multiple real-world problems:

> Investors do not clearly understand how **risk tolerance impacts returns**
> Wealth managers lack a **central view** of portfolio risk vs performance
> Market assumptions are rarely transparent to clients
> Dashboards often mix investor insights and manager insights, causing confusion

As a result, both **clients and advisors struggle to make confident, data-backed decisions**.

---

## 3️. Objective

The objective of this project is to build an **end-to-end portfolio intelligence system** that:

* Converts raw investor inputs into **structured investment portfolios**
* Applies **market assumptions & risk-based allocation logic**
* Provides **two clearly separated dashboards**:

  * One for **investors**
  * One for **wealth managers**
* Enables **risk vs return analysis**, allocation transparency, and decision clarity

---

## 4️. Dataset Overview

### Data Sources Used

This project uses **three logical data layers**:

#### 1. Investor Input Data (Survey-based)

Collected through an external official investment input link (Google Forms), containing:

* Investor name & email
* Investment amount range
* Risk tolerance
* Investment goal
* Timestamp

#### 2. Market Assumptions (Static Reference Data)

Defined manually to simulate real-world expected returns:

* Equity
* Government Bonds
* Gold

Each asset class includes:

* Expected return
* Risk category

#### 3. Final Portfolio Dataset (Generated via Python)

A transformed, analytics-ready dataset containing:

* Investor-level portfolio breakup
* Asset-wise allocation
* Expected return & expected profit
* Risk profiling

📁 **Final output file:** `final_portfolio.csv`

---

## 5️. Tools & Technologies Used

### Programming & Data Processing

* **Python**
* Pandas
* NumPy
* Datetime module

### Visualization & BI

*  Tableau Public
* Dual-axis & donut charts
* Parameter-driven analysis

### Supporting Tools

* CSV-based live data replacement (no broken connections)
* Official financial websites embedded for market reference

---

## 6️.Workflow / Architecture

### End-to-End Architecture Flow

```
Investor Inputs
      ↓
Raw Survey CSV
      ↓
Python Data Cleaning & Transformation
      ↓
Risk Profiling Logic
      ↓
Asset Allocation Rules
      ↓
Expected Return & Profit Calculation
      ↓
Final Portfolio CSV
      ↓
Tableau Dashboards (2 Pages)
```

###  Key Architectural Decisions

* Python handles **all business logic**
* Tableau focuses only on **analytics & storytelling**
* CSV connection remains intact even when data updates
* Clear separation between **data layer** and **visual layer**

---

## 7️. Dashboard Design Logic 

### 📄 Page 1 — Investor Portfolio View

**Target User:** Individual Investor
**Purpose:** Transparency, clarity, confidence

#### What this page answers:

* How is my money allocated?
* What return can I expect?
* How risky is my portfolio?
* Which asset contributes the most?

#### Key Visuals:

* Portfolio KPIs (Investment, Expected Return, Expected Profit)
* Asset Allocation Donut Chart
* Asset-wise Expected Profit
* Risk Profile Indicator
* Portfolio Breakdown
  
🔹 **Design Principle:**
Simple, clean, explanatory.

---

### 📄 Page 2 — Wealth Manager View

**Target User:** Wealth Manager / Advisor
**Purpose:** Analysis, comparison, decision support

#### What this page answers:

* Which investors carry higher risk?
* How balanced are portfolios across asset classes?
* Where does rebalancing make sense?

#### Key Visuals:

* Asset Class Exposure
* Investor Comparison Filters
* Market reference links embedded

🔹 **Design Principle:**
Analytical, comparative, insight-heavy — built for professionals.

---

## 8️. Key Insights Generated

* High-risk portfolios show higher expected returns but increased volatility
* Asset diversification significantly stabilizes expected profit
* Investors often underestimate how allocation impacts outcomes

---

## 9️. Screenshots

📸 Dashboard previews are included below:

* **Dashboard Page 1 — Investor View**
* **Dashboard Page 2 — Wealth Manager View**

*(Screenshots attached in the repository for visual reference)*

---

## 10.  Future Enhancements

* Integrate live market data via APIs
* Add CAPM-based expected return calculations
* Automate daily portfolio refresh
* Extend to mutual funds & ETFs
* Deploy dashboards via Tableau Server

---

## 11. Conclusion

This project demonstrates:

* Practical application of **risk-based allocation**
* Clean **Python-to-Tableau integration**
* Thoughtful **dashboard storytelling**
* Real-world **wealth management use case**

It is not just a dashboard —
it is a **complete analytics system**.

---

⭐ *If you find this project insightful, feel free to star the repository!*
📩 *Open to feedback, collaboration, and opportunities.*

---

