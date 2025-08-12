# Compile the stock-wise relevant information based on search results for easy analysis
stocks_info = {
    "Goldman Sachs": {
        "market_cap": "Not explicitly stated in sources",
        "EPS": 10.91,
        "ROE": "12.8% (Q2 2025)",
        "price_to_book": "Book value per share $349.74",
        "revenue": "$14.58 billion (Q2 2025)",
        "earnings_YoY_growth": "EPS up from $8.62 (Q2 2024) to $10.91 (Q2 2025)",
        "stock_performance": "Up 22% in 2025 year to date but stock fluctuated after earnings",
        "analyst_note": "Shares appear expensive, valuation pressure anticipated, risks from trade policy and inflation"
    },
    "Johnson & Johnson": {
        "market_cap": "Approx. $450 billion (commonly known figure as of 2025)",
        "EPS": 2.29,
        "price_to_earning_ratio": "Not explicitly stated, estimated approx ~25 based on price & EPS",
        "sales": "$23.7 billion quarterly sales",
        "earnings_growth": "18.7% EPS increase over prior year quarter",
        "debt_to_equity": "Long term debt approx $38.4B",
        "ROE": "Not explicitly reported",
        "investment_highlight": "Boosted outlook despite tariff talk, $55B investment in US manufacturing",
        "stock_movement": "Shares up 5.5% after earnings beat and raise",
        "valuation_note": "Resilient due to diversified portfolio and robust pipeline"
    },
    "Morgan Stanley": {
        "EPS": 2.13,
        "ROE": "ROTCE 18.2%",
        "revenue": "$16.8 billion Q2 2025",
        "stock_performance": "Up about 10% in 2025, fell 3.3% after earnings release",
        "strategy_note": "Strong trading revenue, inorganic growth discussed with M&A potential",
        "analyst_observation": "Six sequential quarters of steady earnings despite volatile market"
    },
    "Bank of America": {
        "EPS": 0.89,
        "revenue": "$26.5 billion Q2 2025",
        "stock_performance": "Shares slightly up pre-market after slightly better than feared results",
        "financial_note": "Record net interest income, stable operational efficiency despite lower NII",
        "analyst_view": "Buy recommendation with price target of $56"
    },
    "Nvidia": {
        "market_cap": "$4 trillion approx",
        "P/E": "Approximately 52.5",
        "EPS": "Not explicitly in search, known strong earnings",
        "stock_performance": "Surged with AI demand, up over 20% in 2025",
        "strategic_note": "Resuming H20 chip sales to China, new compliant chip model released, potential major growth in China",
        "risk_note": "Valuation high, competition rising, regulatory uncertainties"
    },
    "ASML": {
        "stock_movement": "Shares dropped 6.5% or more after earnings due to cautious guidance",
        "reason_decline": "Uncertainty about growth outlook in 2026, geopolitical tensions, tariff threats",
        "revenue": "$6.4 billion bookings in Q2 but cautious outlook for growth",
        "market_value_loss": "$30 billion market value wiped out in early trading"
    },
    "MP Materials": {
        "stock_movement": "Surging close to 300% YTD, 2.9% rise after Apple deal",
        "reason_rise": "Pentagon backing with major supply contracts, strategic positioning in rare earths",
        "revenue_growth": "25% revenue increase year over year Q1 2025",
        "strategic_note": "US focus on securing rare earths supply chain amid China tensions"
    },
    "Global Payments": {
        "stock_movement": "Rising on news of activist investor Elliott Management building sizable stake",
        "strategy_note": "Activism and potential M&A activity fueling stock interest",
        "deal_note": "Acquisition of Worldpay earlier in year"
    },
    "Palantir": {
        "stock_movement": "Upgraded by Mizuho on strong AI adoption",
        "strategy_note": "Growth story intact due to AI demand surge"
    },
}

import pandas as pd

# Convert to DataFrame for tabular display
df = pd.DataFrame(stocks_info).T

# Fill missing common fundamentals with N/A for clarity
common_fundamentals = ["market_cap", "price_to_earning_ratio", "average_volume", "EPS", "earning_per_share", "projected_earning_growth", "debt_to_equity", "ROE", "price_to_book", "free_cash_flow", "price_to_sales_ratio"]

for col in common_fundamentals:
    if col not in df.columns:
        df[col] = 'N/A'

# Select and reorder columns for final analysis output
cols_to_display = ["market_cap", "price_to_earning_ratio", "average_volume", "EPS", "projected_earning_growth", "debt_to_equity", "ROE", "price_to_book", "free_cash_flow", "price_to_sales_ratio"]

final_df = df[cols_to_display]

final_df.head()