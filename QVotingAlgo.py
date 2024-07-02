import pandas as pd
import numpy as np
from collections import defaultdict

df = pd.read_csv('TestingPGF.csv')
vote_cols = df.columns[1:]

for col in vote_cols:
    df[col] = df[col].map(np.sqrt)

scores = defaultdict(float)
for col in vote_cols:
    for value in df[col]:
        scores[col] += value

ranking = sorted(scores.items(), key=lambda i: i[1], reverse=True)
scores_df = pd.DataFrame(ranking, columns=["Project", "Score"])

matching_pool = 10000
total_score = sum(scores.values())

allocation_data = []
for project, score in ranking:
    allocation = (score / total_score) * 100
    allocation_project = (allocation / 100) * matching_pool
    allocation_data.append((project, allocation_project, allocation))

allocation_df = pd.DataFrame(allocation_data, columns=["Project", "Allocation (USD)", "Allocation (%)"])

total_funds = 10000
min_allocation_percent = 3
max_allocation_percent = 8

score_spread = ranking[0][1] - ranking[-1][1]
allocation_spread = max_allocation_percent - min_allocation_percent

fund_allocations = {}
adjusted_allocation_data = []
for project, score in ranking:
    if score_spread > 0:
        score_normalized = (score - ranking[-1][1]) / score_spread
        allocation_percent = min_allocation_percent + (score_normalized * allocation_spread)
    else:
        allocation_percent = (min_allocation_percent + max_allocation_percent) / 2

    funds_for_project = (allocation_percent / 100) * total_funds
    fund_allocations[project] = funds_for_project
    adjusted_allocation_data.append((project, funds_for_project, allocation_percent))

adjusted_allocation_df = pd.DataFrame(adjusted_allocation_data, columns=["Project", "Adjusted Allocation (USD)", "Adjusted Allocation (%)"])

final_df = scores_df.merge(allocation_df, on="Project").merge(adjusted_allocation_df, on="Project")
final_df.to_csv('QV_Results.csv', index=False)
print(final_df)
