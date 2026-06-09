import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

funds = pd.read_csv(
    BASE_DIR / "data" / "processed" / "fund_scorecard.csv"
)

print("Columns in dataset:")
print(funds.columns.tolist())

def recommend(risk_level):

    risk_col = "risk_grade"

    if "sharpe_ratio" in funds.columns:
        sharpe_col = "sharpe_ratio"
    elif "sharpe_ratio_y" in funds.columns:
        sharpe_col = "sharpe_ratio_y"
    else:
        raise ValueError("Sharpe Ratio column not found!")

    recommendations = (
        funds[
            funds[risk_col]
            .astype(str)
            .str.lower()
            ==
            risk_level.lower()
        ]
        .sort_values(
            sharpe_col,
            ascending=False
        )
        .head(3)
    )

    cols_to_show = [
    "scheme_name",
    "fund_house",
    "category",
    "risk_grade",
    "return_3yr_pct",
    "sharpe_ratio_y",
    "fund_score"
]

    print("\nRecommended Funds:\n")
    print(
        recommendations[
            cols_to_show
        ]
    )

    return recommendations

recommend("High")