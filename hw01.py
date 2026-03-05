"""
DSC 20 Spring 2025 Homework 01
Name: Karina Lopez
PID: A18356687
sources: ChatGPT for "\n" for question 6 
"""

# Question 1
def login(fname, lname):
    """
    # Creates logins for each team member using their first and last name 

    >>> login("Marina", "Langlois")
    'aiaLgi'
    >>> login("", "")
    ''
    >>> login("San", "Diego")
    'nSDg'

    >>> login("Karina", "Lopez")
    'aiaLe'

    >>> login("Ash", "Lee")
    'hAL'

    >>> login("Crystal", "Castellanos-Antes")
    'ltyCCtloAe'
    """
    reversed_fname = fname[::-1]
    finished_login = ''
    for i in range(len(reversed_fname)):
        if i % 2 == 0:
            finished_login += reversed_fname[i]

    for i in range(len(lname)):
        if i % 3 == 0:
            finished_login += lname[i]
    return finished_login


# Question 2
def ages(age1, age2):
    """
    Sees if both people wanting to rent an office are over 23. If not, the age 
    of the person who is closest to 23. 

    >>> ages(19, 21)
    21
    >>> ages(26, 21)
    21
    >>> ages(26, 27)
    'You both can rent!'
    >>> ages(19, 23)
    19

    >>> ages(40, 23)
    'You both can rent!'

    >>> ages(22, 21)
    22

    >>> ages(24, 19)
    19
    """

    if age1 >= 23 and age2 >= 23:
        return 'You both can rent!'
    
    if age1 < 23 and age2 < 23:
        agediff1 = abs(age1 - 23)
        agediff2 = abs(age2 - 23)

        if agediff1 < agediff2:
            return age1
        else:
            return age2
    
    if age1 < 23:
        return age1

    if age2 < 23:
        return age2


# Question 3
def renter(name1, name2, name3):
    """
    the person with the longest name decides who will handle the contract. 
    if they share the same length of name, the person who was called
    last will handle the contract

    >>> renter("K", "BB", "Joy")
    'Joy'
    >>> renter("Joy", "K", "BB")
    'Joy'
    >>> renter("BB", "Joy", "K")
    'Joy'
    >>> renter("BB", "K", "Jo")
    'Jo'
    >>> renter("BB", "Jo", "Su")
    'Su'

    >>> renter("Karina", "Kate", "Chailyn")
    'Chailyn'

    >>> renter("Jade", "Ava", "Ally")
    'Ally'

    >>> renter("Angel", "Karina", "Emilio")
    'Emilio'
    """
    longest_name = name1
    if len(longest_name) <= len(name2):
        longest_name = name2
    if len(longest_name) <= len(name3):
        longest_name = name3
    return longest_name


# Question 4.1
def helper_distance(lst, x2, y2):
    """
    #Calculates the Euclidean distance between the two given points.
    
    >>> helper_distance([0, 0], 3, 4)
    5.0
    >>> helper_distance([-3, -4], 3, 4)
    10.0
    >>> helper_distance ([100, 100], 100.5, 100)
    0.5

    >>> helper_distance([312, 432], 350, 450)
    42.05

    >>> helper_distance([2, 2], 2, 2)
    0.0

    >>> helper_distance([2, 1], 12, 12)
    14.87
    """
    #euclidean_disctance_formula = ((x2-x1)**2 + (y1-y2)**2) ** (1/2)

    return round(((x2 - lst[0]) ** 2 + (y2 - lst[1]) ** 2) ** (1/2), 2)


# Question 4.2
def lunch(lunch_places, office_x, office_y, threshold):
    """
    Returns list of lunch place coordinates that are within the 
    walking threshold

    >>> lunch([[0, 0], [30.5, 20.7]], 3.2, 4, 6)
    [[0, 0]]
    >>> lunch([[-3, -4], [6, 7]], 3, 4, 10)
    [[-3, -4], [6, 7]]
    >>> lunch ([[100, 100]], 100.5, 100, 0.2)
    []

    >>> lunch([[5, 4], [3, 8]], 6, 2, 8)
    [[5, 4], [3, 8]]

    >>> lunch([[8, 3], [7, 2], [4, 3]], 7, 3, 4)
    [[8, 3], [7, 2], [4, 3]]

    >>> lunch([[5, 2], [74, 2], [7, 21], [3, 31]], 1, 8, 10)
    [[5, 2]]
    """
    kept_index = []
    kept_coordinates = []
    for i in range(len(lunch_places)):
        if helper_distance(lunch_places[i], office_x, office_y) <= threshold:
            kept_index.append(i)

    for i in kept_index:
        kept_coordinates.append(lunch_places[i])
    return kept_coordinates


# Question 5
def lunch_names(lunch_places, office_x, office_y, threshold, names):
    """
    Returns a list of the restaurants within the walking distance we want.
    ---

    >>> lunch_names([[0, 0], [30, 20], [5, 9]], 3.2, 4, 6, \
    ['place1', 'place2', 'place3'])
    ['place1', 'place3']
    >>> lunch_names([[-3, -4], [6, 7]], 3, 4, 10, \
    ['place1', 'place2'])
    ['place1', 'place2']
    >>> lunch_names ([[100, 100]], 100.5, 100, 0.2, ['place1'])
    []

    >>> lunch_names([[4, 2], [8, 4], [2, 7]], 6, 2, 8, \
    ['place1', 'place2', 'place3'])
    ['place1', 'place2', 'place3']

    >>> lunch_names([[-3, -4]], 3, 4, 10, ['place1'])
    ['place1']

    >>> lunch_names([[-7, 2], [5, 3]], 8, 2, 5, ['place1', 'place2'])
    ['place2']
    """
    kept_index_positions = []
    kept_names = []
    for i in range(len(lunch_places)):
        if helper_distance(lunch_places[i], office_x, office_y) <= threshold:
            kept_index_positions.append(i)

    for i in kept_index_positions:
        kept_names.append(names[i])
    return kept_names


# Question 6
def meeting_message(i_name, time, place, s_name):
    """
    Creates an invitation that includes the recipients name, 
    the time of the event, its location, and the sender of 
    the invite. 
    ---
    Parameters: 
        i_name: name of recipient
        time: time of the event
        place: place of the event
        s_name: name of person sending invitation
    ---
    Returns: returns an invitation including the information as a string
    ---

    >>> print(meeting_message("Penny", "3:15pm", "Cheesecake Factory", \
        "Sheldon"))
    Dear Penny,
    Please join our meeting at 3:15pm, at the Cheesecake Factory.
    <BLANKLINE>
    See you soon: Sheldon

    >>> print(meeting_message("Freya", "", "Dog Park", "Marina"))
    Dear Freya,
    Please join our meeting at , at the Dog Park.
    <BLANKLINE>
    See you soon: Marina

    >>> print(meeting_message("Karina", "1:30pm", "Chilis", "Crystal"))
    Dear Karina,
    Please join our meeting at 1:30pm, at the Chilis.
    <BLANKLINE>
    See you soon: Crystal

    >>> print(meeting_message("", "2:00pm", "University", "Kate"))
    Dear ,
    Please join our meeting at 2:00pm, at the University.
    <BLANKLINE>
    See you soon: Kate

    >>> print(meeting_message("Chailyn", "3:45pm", "tree", ""))
    Dear Chailyn,
    Please join our meeting at 3:45pm, at the tree.
    <BLANKLINE>
    See you soon: 
    """
    return ('Dear' + ' ' + i_name + ',\n' + 'Please join our meeting at' 
        + ' ' + time + ',' + ' ' + 'at the' + ' ' + place + '.\n' + 
        '\nSee you soon:' + ' ' + s_name)


# Question 7
def seat_number(lst):
    """
    Takes name on list and assigns their seat number based on the length
    of the name on the list. If the seat number is already taken, we keep
    it reserved for the first person who took it.
    ---
    Parameters:
        lst: contains list of names
    ---
    Returns:
    List of assigned seat numbers respective to the order of names on
    the lst. If seat number was already used once, 'taken' is assigned
    to them.

    >>> seat_number(["Marina", "Tom", "B"])
    [6, 3, 1]
    >>> seat_number(["Marina", "Sue", "Ben", "Freya"])
    [6, 3, 'taken', 5]
    >>> seat_number(["Marina", "Sue", "Ben", ""])
    [6, 3, 'taken', 0]

    >>> seat_number(["Karina", "Kate", "Chailyn"])
    [6, 4, 7]
    >>> seat_number(["Karina", "Marina", "Calina"])
    [6, 'taken', 'taken']
    >>> seat_number(["Angel", "Alejandro", "B"])
    [5, 9, 1]
    """
    name_lengths = []
    for i in lst:
        name_length = len(i)
        if name_length in name_lengths:
            name_lengths.append('taken')
        else:
            name_lengths.append(name_length)
    return name_lengths


# Question 8
def computers(choices):
    """
    Counts the occurrences of DESKtop and LAPtop in the choices made
    by everyone in the office and tells us whether or not DESKtop got
    more votes than LAPtop.

    ---
    Parameters:
        choices: votes casted by the people in the office
    ---
    Returns:
        True if DESKtop was counted more often than LAPtop. (case-sensitive)

    >>> computers(["DESKtop", "LAPtop", "DESKtop"])
    True
    >>> computers(["LAPtop", "LAPtop"])
    False
    >>> computers(["DESKtop", "Pager", "Tablet", "LAPtop"])
    False

    >>> computers(["DESKtop", "Pager", "DESKtop", "LAPtop"])
    True
    >>> computers(["DESKtop", "LAPtop", "LAPtop", "LAPtop"])
    False
    >>> computers(["Pager", "Pager", "Tablet", "Pager"])
    False
    """
    desktop_count = choices.count('DESKtop')
    laptop_count = choices.count('LAPtop')

    if desktop_count > laptop_count:
        return True
    else:
        return False


# Question 9
def age_average(lst):
    """
    Calculates the average age of the members on the team who were willing to
    share their age.
    ---
    Parameters:
        lst: list of the team members ages, those who didnt want to participate
        recieved a negative number
    ---
    Returns:
        average of the combined ages of the members who provided a valid age

    >>> age_average(["20", "21", "22"])
    '21.0'
    >>> age_average(["50", "25", "30"])
    '35.0'
    >>> age_average(["40", "-999", "45"])
    '42.5'
    >>> age_average([])
    '0.0'

    >>> age_average(["-999", "-999", "-999"])
    '0.0'
    >>> age_average(["40", "-999", "-999"])
    '40.0'
    >>> age_average(["40", "45", "45"])
    '43.3'
    """
    age_tracker = []
    for i in lst:
        if int(i) > 0:
            age_tracker.append(int(i))

    if len(age_tracker) == 0:
        return '0.0'

    return str(round(sum(age_tracker) / len(age_tracker), 1))


# Question 10
def supervision_teams(team, company_name):
    """
    Creating two teams based on their position on the team list. Even positions
    create the first team and odd positions create the second team.
    ---
    Parameters:
        team: list of painters
        company_name: name of the company, added to the beginning list of the 
        first time and to the end of the second teams list
    ---
    Returns:
        two lists created by whether the employees position was even or odd in
        the list

    >>> supervision_teams(["p1", "p2", "p3"], "Marina")
    (['Marina', 'p1', 'p3'], ['p2', 'Marina'])
    >>> supervision_teams(["p1"], "Marina")
    (['Marina', 'p1'], ['Marina'])
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "Marina")
    (['Marina', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'Marina'])

    >>> supervision_teams(["p1", "p2", "p3", "p4"], "Karina")
    (['Karina', 'p1', 'p3'], ['p2', 'p4', 'Karina'])
    
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6", "p7"], \
    "WEPAINT")
    (['WEPAINT', 'p1', 'p3', 'p5', 'p7'], ['p2', 'p4', 'p6', 'WEPAINT'])

    >>> supervision_teams(["p1", "p2"], "Kate")
    (['Kate', 'p1'], ['p2', 'Kate'])
    """

    first_team = [company_name] + team[0::2]
    second_team = team[1::2] + [company_name]
    return (first_team, second_team)
# #     