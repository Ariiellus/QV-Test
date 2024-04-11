# BordaCount
This is a test in python for a Borda Count mechanism

# Notes on Solidity Contract

The Solidity smart contract has been obtained throught ChatGPT. DO NOT USE IN PROD!!!

It supposed to implement a simple voting system where participants can vote for projects, and based on the votes, a predetermined pool of funds is allocated among the projects.

## Key Points of the Contract

- **Data Storage**: The contract uses a `mapping` to store projects and a dynamic array to keep track of the list of projects. Each project is associated with a number of votes it received and an allocation from the fund.

- **Voting**: Participants can vote for projects by calling the `voteForProject` function. This function accumulates votes for projects and adds new projects to the list if they don't already exist.

- **Ending Voting and Calculating Allocations**: The `endVoting` function ends the voting period and calculates the fund allocation for each project based on the total votes received.

- **Allocation Retrieval**: After voting has ended, the `getAllocation` function allows anyone to query the final fund allocation for any project.

## Limitations and Considerations

- **Input Data**: Unlike implementations in languages such as Python, this Solidity contract cannot directly read from external files like a CSV. Votes must be submitted through Ethereum transactions.

- **Gas Costs**: Both voting and the process of ending the voting to calculate allocations incur gas costs, which are paid by the transaction sender.

- **Permissions**: This basic implementation does not manage permissions. In a real-world scenario, it might be necessary to restrict who can end the voting period and calculate allocations, typically to an administrator or the contract creator.

- **Optimization**: Depending on the requirements, further optimizations might be necessary, such as limiting the number of votes per address or implementing more sophisticated voting logic to accommodate complex strategies.
