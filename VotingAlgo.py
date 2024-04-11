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
