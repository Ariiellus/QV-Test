import pandas as pd
import numpy as np

num_voters = 1200
num_projects = 20
total_points = 100

projects = [f"P{j+1}" for j in range(num_projects)]

def allocate_points(total_points, num_projects):
    points = np.zeros(num_projects, dtype=int)
    for _ in range(total_points):
        points[np.random.randint(0, num_projects)] += 1
    return points

voter_data = {
    f"Voter_{i+1}": allocate_points(total_points, num_projects).tolist()
    for i in range(num_voters)
}

df_voters = pd.DataFrame(voter_data).transpose()
df_voters.columns = projects

df_voters.reset_index(inplace=True)
df_voters.rename(columns={"index": "ID"}, inplace=True)

df_voters.to_csv('TestingPGF.csv', index=False)