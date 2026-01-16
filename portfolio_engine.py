import pandas as pd
import numpy as np
from datetime import datetime


# STEP 1: Load survey data

df = pd.read_csv("survey_raw.csv")


# STEP 2: Clean column names

df.columns = (
    df.columns
    .str.strip()
    .str.replace("  ", " ")
)


# STEP 3: Fix ₹ encoding issue

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = (
            df[col]
            .str.replace("â‚¹", "₹", regex=False)
            .str.replace("â€“", "–", regex=False)
        )


# STEP 4: Rename columns (simplify)

df = df.rename(columns={
    "How much amount are you willing to invest?": "Investment_Range",
    "How do you feel if your investment value fluctuates in the short term?": "Risk_Tolerance",
    "What is your primary investment goal?": "Investment_Goal"
})


# STEP 5: Map investment ranges to numbers

amount_map = {
    "₹1,00,000 – ₹3,00,000": 200000,
    "₹3,00,001 – ₹6,00,000": 450000,
    "₹6,00,001 – ₹10,00,000": 800000,
    "Above ₹10,00,000": 1200000
}

df["Investment_Amount"] = df["Investment_Range"].map(amount_map)


# STEP 6: Assign Risk Profile

risk_map = {
    "I prefer stable returns even if growth is low": "Low",
    "I can tolerate moderate ups and downs": "Medium",
    "I am comfortable with high fluctuations for higher returns": "High"
}

df["Risk_Profile"] = df["Risk_Tolerance"].map(risk_map)


# STEP 7: Generate Investor ID

df["Investor_ID"] = ["INV" + str(i+1).zfill(3) for i in range(len(df))]


# STEP 8: Investment Date

df["Investment_Date"] = pd.to_datetime(df["Timestamp"])


# STEP 9: Market Assumptions (CORE LOGIC)

market_data = pd.DataFrame({
    "Asset_Class": ["Equity", "Govt Bonds", "Gold"],
    "Expected_Return": [0.12, 0.07, 0.06],
    "Risk_Level": ["High", "Low", "Low"]
})

# Allocation rules by risk
allocation_rules = {
    "Low": {"Equity": 0.2, "Govt Bonds": 0.6, "Gold": 0.2},
    "Medium": {"Equity": 0.4, "Govt Bonds": 0.4, "Gold": 0.2},
    "High": {"Equity": 0.6, "Govt Bonds": 0.2, "Gold": 0.2}
}


# STEP 10: Build final portfolio rows

portfolio_rows = []

for _, row in df.iterrows():
    allocations = allocation_rules[row["Risk_Profile"]]
    for asset, pct in allocations.items():
        invest_amt = row["Investment_Amount"] * pct
        expected_return = market_data.loc[
            market_data["Asset_Class"] == asset, "Expected_Return"
        ].values[0]

        portfolio_rows.append({
            "Investor_ID": row["Investor_ID"],
            "Name": row["Name"],
            "Risk_Profile": row["Risk_Profile"],
            "Asset_Class": asset,
            "Allocation_%": pct * 100,
            "Investment_Amount": round(invest_amt, 0),
            "Expected_Return_%": expected_return * 100,
            "Expected_Profit": round(invest_amt * expected_return, 0),
            "Investment_Date": row["Investment_Date"]
        })


# STEP 11: Export FINAL dataset

final_df = pd.DataFrame(portfolio_rows)
final_df.to_csv("final_portfolio.csv", index=False)

print(" FINAL PORTFOLIO GENERATED SUCCESSFULLY")
