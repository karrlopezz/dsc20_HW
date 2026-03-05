"""
DSC 20 Spring 2025 Homework 05
Name: Karina Lopez
PID: A18356687
Source: TODO
"""

# Question 1

def get_qualified_customers(data, max_avg, min_range):
    """
    Returns a list of all customer IDs that mmet criteria
    --
    Parameters:
    data: dictionary of customers data where the keys are the customers
    ID's, the values are a list of integers representing numeric scores
    max_avg: positive integer
    min_range: positive integer
    --
    Returns:
    List of all customer ID's based on criteria:
    avg score should be less than or equal to max_avg
    range should be greater than or equal to min_range
    no duplicate scores

    >>> data = { \
        "Jayden": [10, 10, 10, 10, 10], \
        "Terry": [1, 2, 3, 4, 5, 6, 7, 8], \
        "Austin": [10, 11, 12, 13, 14], \
        "Noah": [2, 3, 4, 5] \
    }
    >>> get_qualified_customers(data, 11, 5)
    ['Terry']

    >>> data = { \
        "Caleb": [0, 1, 2, 3, 4, 5], \
        "Keenan": [8, 9, 10], \
        "Rome": [7, 8, 9], \
        "Khalil": [] \
    }
    >>> get_qualified_customers(data, 9, 2)
    ['Caleb', 'Keenan', 'Rome']

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #

    >>> data = { \
        "karina": [5, 6, 7], \
        "kate": [10, 10, 10], \
        "chailyn": [1, 2, 3, 4, 5] \
    }
    >>> get_qualified_customers(data, 10, 1)
    ['karina', 'chailyn']

    >>> data = { \
        "angel": [100], \
        "rick": [], \
        "alejandro": [4, 4, 4] \
    }
    >>> get_qualified_customers(data, 5, 2)
    []

    >>> data = { \
        "ally": [1, 5, 10, 15] \
    }
    >>> get_qualified_customers(data, 10, 10)
    ['ally']
    """
    assert isinstance(data, dict)
    assert isinstance(max_avg, int) and max_avg > 0
    assert isinstance(min_range, int) and min_range > 0
    assert all(isinstance(key, str) for key in data.keys())
    assert all(isinstance(vals, list) and all(isinstance(v, int)
 for v in vals) for vals in data.values())

    calc_avg = lambda lst: sum(lst) / len(lst) if lst else 0
    calc_range = lambda lst: max(lst) - min(lst) if lst else 0

    return [key for key, vals in data.items()
     if calc_avg(vals) <= max_avg and
      calc_range(vals) >= min_range and
      len(set(vals)) == len(vals)]


# Question 2

def message_to_customers(customer_file, decision, message):
    """
    Returns a list of messages to customers based on the decision
    --
    Parameters:
    customer_file: text file that contains cutomer info in format:
                    company_name, person_in_charge, email, decision
    decision: string either 's' or 'w'
    message: string to send
    --
    Returns:
    list of messages to customers based on whether decision is
    's' (staying) or 'w' (waitlisted).

    >>> msg = "unfortunately we cannot work with you."
    >>> message_to_customers("files/customers.txt", "w", msg)
    ['(to: steve@apple.com) Dear Steve at Apple, \
unfortunately we cannot work with you.', \
'(to: jensen@nvidia.com) Dear Jensen at NVIDIA, \
unfortunately we cannot work with you.']

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers.txt", "s", msg)
    ['(to: jeff@amazon.com) Dear Jeff at Amazon, \
we are excited to work with you!', \
'(to: mark@fb.com) Dear Mark at Facebook, \
we are excited to work with you!']

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers1.txt", "s", msg)
    ['(to: kari@amazon.com) Dear Karina at Amazon, \
we are excited to work with you!', \
'(to: angel@apple.com) Dear Angel at Apple, \
we are excited to work with you!', \
'(to: ally@marshalls.com) Dear Ally at Marshalls, \
we are excited to work with you!']

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers2.txt", "s", msg)
    []

    >>> msg = "we are excited to not work with you!"
    >>> message_to_customers("files/customers3.txt", "w", msg)
    ['(to: rick@ross.com) Dear Rick at Ross, \
we are excited to not work with you!']
    """
    assert isinstance(customer_file, str)
    assert isinstance(decision, str) and decision in ['s', 'w']
    assert isinstance(message, str)

    messages = []

    with open(customer_file, 'r') as f:
        for line in f:
            company_name, person_in_charge, email, customer_decision\
             = line.strip().split(',')
            assert isinstance(company_name, str)
            assert isinstance(person_in_charge, str)
            assert isinstance(email, str)
            assert isinstance(customer_decision, str)\
             and customer_decision in ['s', 'w']

            if customer_decision == decision:
                msg = f"(to: {email}) Dear {person_in_charge}\
 at {company_name}, {message}"
                messages.append(msg)

    return messages

# Question 3

def forge_votes(vote_file):
    """
    Updates a file with forged votes so that majority favors Snoozer
    and Snacker
    --
    Parameters:
    vote_file: file with votes
    --
    Returns:
    file with forged or kept votes that favor majority

    >>> forge_votes("files/vote1.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Patrick,1
    Travis,0
    Clyde,1
    Andy,1

    >>> forge_votes("files/vote2.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,0

    >>> forge_votes("files/vote3.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Andy,1

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #

    >>> forge_votes("files/vote4.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Karina,1
    Angel,1
    Rick,0

    >>> forge_votes("files/vote5.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Ally,1
    Karina,1
    Kate,0

    >>> forge_votes("files/vote6.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Angel,1
    Karina,1
    Ally,1
    Kate,1
    Chailyn,1
    Rick,0
    Maria,0
    Emilio,0
    """
    with open(vote_file, 'r') as f:
        lines = f.readlines()

    entries = [line.strip() for line in lines]
    votes = [line.strip().split(',')[1] for line in lines]
    yes_total = votes.count('1')
    total_votes = len(votes)
    majority_needed = (total_votes // 2) + 1
    votes_needed = max(0, majority_needed - yes_total)

    full_text = '\n'.join(entries)
    while votes_needed > 0:
        full_text = full_text.replace(',0', ',1', 1)
        votes_needed -= 1

    with open('files/forged.txt', 'w') as f_out:
        f_out.write(full_text)

# Question 4

def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function. No new doctests required.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (True/False) #
    return [False, True, False, True, True, True, True, \
True, False, False]