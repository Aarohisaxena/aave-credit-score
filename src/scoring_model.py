import numpy as np

def extract_features(transactions):
    # Example features: counts, volumes, ratios, etc.
    actions = [tx["action"].lower() for tx in transactions]
    amounts = [float(tx.get("amount", 0)) for tx in transactions]

    features = {
        "n_total": len(transactions),
        "n_deposit": actions.count("deposit"),
        "n_borrow": actions.count("borrow"),
        "n_repay": actions.count("repay"),
        "n_liquidation": actions.count("liquidationcall"),
        "total_amount": sum(amounts),
        "avg_amount": np.mean(amounts) if amounts else 0,
        "max_amount": max(amounts) if amounts else 0,
        "min_amount": min(amounts) if amounts else 0,
        "repay_borrow_ratio": (
            actions.count("repay") / actions.count("borrow") if actions.count("borrow") else 0
        ),
        "liquidation_borrow_ratio": (
            actions.count("liquidationcall") / actions.count("borrow") if actions.count("borrow") else 0
        ),
    }
    return features

def compute_score(features):
    # Example: weighted sum, then scaled to 0-1000
    score = 500  # base

    # Reward positive behavior
    score += 50 * features["repay_borrow_ratio"]
    score += 0.1 * features["n_repay"]
    score += 0.05 * features["n_deposit"]

    # Penalize risky behavior
    score -= 100 * features["liquidation_borrow_ratio"]
    score -= 0.1 * features["n_liquidation"]

    # Clamp to 0-1000
    score = max(0, min(1000, int(score)))
    return score