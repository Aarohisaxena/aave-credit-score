# Aave V2 Wallet Credit Scoring by Aarohi

## Method

- **Features:** Transaction counts, volumes, repayment/borrow ratios, liquidation events.
- **Scoring:** Rule-based, transparent, weights positive/negative behaviors.

## Architecture

- `feature_engineering.py`: Extracts features from raw transactions.
- `scoring_model.py`: Assigns a score (0-1000) based on features.
- `score_wallets.py`: One-step script to process input and output scores.
## Data

  The raw transaction data is too large for GitHub.  
  Please download it manually from [this link](https://drive.google.com/file/d/1ISFbAXxadMrt7Zl96rmzzZmEKZnyW7FS/view?usp=sharing) and place it in the `data/` folder as `user-wallet-transactions.json`.

  

## Usage

1. Place your `user-wallet-transactions.json` in the `data/` folder.
2. From the project root, run:
   ```
   python src/score_wallets.py
   ```
3. Results will be saved in `wallet_scores.csv` in the project root.

## Analysis

- To visualize the score distribution, run:
  ```
  python src/plot_score_distribution.py
  ```
- The resulting plot can be found as `score_distribution.png` and should be included in `analysis.md`.

## Extensibility

- Add new features in `feature_engineering.py`.
- Adjust scoring logic in `scoring_model.py`.

## Requirements

Install dependencies with:
