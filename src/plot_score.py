import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wallet_scores.csv")
plt.hist(df['score'], bins=range(0, 1001, 100), edgecolor='black')
plt.xlabel('Score')
plt.ylabel('Number of Wallets')
plt.title('Wallet Score Distribution')
plt.savefig("score_distribution.png")
plt.show()