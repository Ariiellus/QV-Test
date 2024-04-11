import pandas as pd
import numpy as np

# Define the number of voters and projects
num_voters = 650
num_projects = 20
num_ranks = 20

# Create random distribution of ranks for each voter
# np.random.choice ensures no project is chosen more than once per voter
voter_data = {
    f"Voter_{i+1}": np.random.choice([f"P{j+1}" for j in range(num_projects)], num_ranks, replace=False)
    for i in range(num_voters)
}

# Create a DataFrame
df_voters = pd.DataFrame(voter_data)

# Transpose the DataFrame to align it to the desired format (voters as rows, projects as columns)
df_voters = df_voters.transpose()

# Reset index to get voters as a column
df_voters.reset_index(inplace=True)
df_voters.rename(columns={"index": "ID"}, inplace=True)

# Adjust columns to match the rank columns R1, R2, ..., R20
rank_columns = {i: f"R{i+1}" for i in range(num_ranks)}
df_voters.rename(columns=rank_columns, inplace=True)

# Show the created DataFrame
df_voters.head(num_voters)

# Export the DataFrame to a CSV file
df_voters.to_csv('TestingPGF.csv', index=True)