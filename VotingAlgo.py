#region VotingAlgo

import pandas as pd
from collections import defaultdict

# Load the exported Google Form CSV
df = pd.read_csv('TestingPGF.csv')

# Extract only the ranking columns
vote_cols = df.columns[2:]
df = df[vote_cols]

# Calculate total number of projects
projects = set()
for i, col in enumerate(df.columns):
    for project in df[col]:
        projects.add(project)
n_projects = len(projects)
print(n_projects, 'projects')

# Get how many ranks were available to give
n_ranks = len(vote_cols)
print(n_ranks, 'ranks')

print('='*50)

for label, base_points in [('ranks', n_ranks)]:
    print('Using {} as base points:'.format(label))
    # Assuming first column is highest rank
    scores = defaultdict(int)
    for i, col in enumerate(df.columns):
        points = base_points - i
        for projects in df[col]:
            scores[projects] += points

    # Sort projects by score, descending
    ranking = sorted(scores.items(), key=lambda i: i[1], reverse=True)
    for cand, score in ranking:
        print(cand, score)
    print('='*50)

# Distributing n amount of $$$
matching_pool = 10000
total_score = sum(scores.values())

print(f"Total Points: {total_score:.2f}")
print("Final Allocation:")
for project, score in ranking:
    allocation = (score / total_score) * 100
    allocation_project = (allocation / 100) * matching_pool
    print(f"{project}: ${allocation_project:.2f} ({allocation:.2f}%)")
print('='*50)

#region AdjustedAllocation

# Assuming the sorted_scores list and matching_pool from before are correctly set

# First, prepare the min and max percentages for distribution
total_funds = 10000  # Total pool of funds to distribute
min_allocation_percent = 3
max_allocation_percent = 8

# Prepare to calculate percentages
score_spread = ranking[0][1] - ranking[-1][1]  # Difference between highest and lowest score
allocation_spread = max_allocation_percent - min_allocation_percent

# Calculate percentage of total funds for each project
fund_allocations = {}
for project, score in ranking:
    if score_spread > 0:
        # Linear interpolation for score to percentage mapping
        score_normalized = (score - ranking[-1][1]) / score_spread
        allocation_percent = min_allocation_percent + (score_normalized * allocation_spread)
    else:
        # If all projects have the same score, distribute funds equally
        allocation_percent = (min_allocation_percent + max_allocation_percent) / 2

    # Calculate the amount of funds based on the percentage
    funds_for_project = (allocation_percent / 100) * total_funds
    fund_allocations[project] = funds_for_project

# Now, print the allocations
for project, funds in fund_allocations.items():
    print(f"{project}: ${funds:.2f} ({(funds / total_funds) * 100:.2f}%)")
