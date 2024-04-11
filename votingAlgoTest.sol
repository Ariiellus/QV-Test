// Code obtained via ChatGPT. DO NOT USE in prod!!!

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract Voting {

    struct Project {
        uint votes;
        uint allocation;
    }

    mapping(string => Project) public projects;
    string[] public projectList;
    uint public totalVotes = 0;
    uint public matchingPool = 10000; // Amount of funds to be distributed
    bool public votingEnded = false;

    // Function to vote for projects
    function voteForProject(string memory projectName, uint votes) public {
        require(!votingEnded, "Voting has ended.");
        if(projects[projectName].votes == 0) {
            projectList.push(projectName);
        }
        projects[projectName].votes += votes;
        totalVotes += votes;
    }

    // End the voting period and calculate allocations
    function endVoting() public {
        require(!votingEnded, "Voting has already ended.");
        votingEnded = true;
        for(uint i = 0; i < projectList.length; i++) {
            string memory projectName = projectList[i];
            Project storage project = projects[projectName];
            project.allocation = (project.votes * matchingPool) / totalVotes;
        }
    }

    // Get the allocation for a project
    function getAllocation(string memory projectName) public view returns (uint) {
        require(votingEnded, "Voting has not ended yet.");
        return projects[projectName].allocation;
    }
}


// Code obtained via ChatGPT. DO NOT USE in prod!!!

// NOTES:
// Solidity can't handle external data, every voter should make a TX to add their votes to the "database".
// Details given by ChatGPT can be found in README.md