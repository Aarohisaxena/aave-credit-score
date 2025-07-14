import json
import pandas as pd
from tqdm import tqdm
from feature_engineering import extract_features
from scoring_model import compute_score

INPUT_JSON = "data/user-wallet-transactions.json"
OUTPUT_CSV = "wallet_scores.csv"

def main():
    # Load data
    with open(INPUT_JSON, "r") as f:
        data = json.load(f)

    # Group transactions by userWallet
    from collections import defaultdict
    wallet_dict = defaultdict(list)
    for tx in data:
        wallet = tx.get("userWallet")
        if wallet:
            wallet_dict[wallet].append(tx)

    results = []
    for wallet, txs in tqdm(wallet_dict.items(), desc="Scoring wallets"):
        features = extract_features(txs)
        score = compute_score(features)
        results.append({"wallet": wallet, "score": score, **features})

    # Save to CSV
    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved scores to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()