"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata.
    """
    limit = 1
    for candidate in args:
        if candidate in candidates:
            return "Candidate has already been registered!!"
        else:
            candidates[candidate] = {"votes": 0, **kwargs}


def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before.
        after all the vote logic is completeted sucessfully,
        return: Vote casted for {candidate}.
    """
    if candidate not in candidates:
        return f"Candidate '{candidate}' is not a registered candidate"
    
    elif candidate in candidates and voter_id not in voters:
        candidates[candidate]['votes'] += 1
        voters.add(voter_id)
        return f"Vote Casted successful for '{candidate}'"
    elif voter_id in voters:
         return f"Voter '{voter_id}' has already voted."

def election_result():
    """Return the winner(s)."""
    # max_votes = #add logic
    if not candidates:
        return "No candidates registered for this election"
    else:
        max_votes = 0
        for details in candidates.values():
            if details["votes"] > max_votes:
                max_votes= details["votes"]
    
    # winners = #add logic
    winners = []
    for candidate in candidates:
        if candidates[candidate]["votes"] == max_votes:
            winner=candidate

    return {"winners": winner, "candidates": candidates}


# calling of functions

# Register candidates
register_candidates("Jerry", "Mimi", "TK", party="APC", region="North")

# Cast votes
print(cast_vote("V1", "Jerry"))
print(cast_vote("V2", "Mimi"))
print(cast_vote("V4", "TK"))  
print(cast_vote("V3", "Jerry"))

# Show result
print(election_result())
