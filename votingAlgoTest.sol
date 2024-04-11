// SPDX-License-Identifier: MIT

// Code obtained via ChatGPT. DO NOT USE in prod!!!
pragma solidity ^0.8.24;

contract VotingSystem {
    struct Candidate {
        uint id;
        string name;
        uint score;
    }

    Candidate[] public candidates;
    mapping(uint => uint) public ranksGiven; // CandidateID to score
    uint public totalCandidates;
    uint public totalRanks;

    function addCandidate(string memory name) public {
        candidates.push(Candidate(totalCandidates, name, 0));
        totalCandidates++;
    }

    function vote(uint[] memory candidateIds, uint[] memory points) public {
        require(candidateIds.length == points.length, "Each candidate must have corresponding points.");
        require(candidateIds.length <= totalRanks, "Cannot assign more ranks than available.");

        for(uint i = 0; i < candidateIds.length; i++) {
            uint candidateId = candidateIds[i];
            uint point = points[i];
            
            // Ensure valid candidateId and points are not assigned more than once to the same candidate
            require(candidateId < totalCandidates, "Invalid candidate ID.");
            require(ranksGiven[candidateId] == 0, "Points already assigned to this candidate.");

            candidates[candidateId].score += point;
            ranksGiven[candidateId] = point;
        }
    }

    // A placeholder for setting total ranks available, which could be based on some logic or input
    function setTotalRanks(uint _totalRanks) public {
        totalRanks = _totalRanks;
    }
}

// Code obtained via ChatGPT. DO NOT USE in prod!!!
// NOTES:
// Solidity can't handle external data, every voter should make a TX to add their votes to the "database".