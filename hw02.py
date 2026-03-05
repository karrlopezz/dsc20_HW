"""
DSC 20 Spring 2025 Homework 02
Name: Karina Lopez
PID: A18356687
"""

# Question 1
def name_mapping(given_names, preferred_names):
    """
    Creates list of tuples containing persons given name and their preffered
    name
    -- 
    Parameters:
    given_names: list of given names of team
    preffered_names: list of preffered names of team
    --
    Returns:
    List of tuples with team members' given name 
    (if provided; if not, 'NO NAME PROVIDED' is used instead)
    and their preferred name

    >>> given_names = ['Amanda', 'Jeffrey', 'Richard']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('Richard', 'Rick')]

    >>> given_names = ['Amanda', 'Jeffrey']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('NO NAME PROVIDED', 'Rick')]

    >>> given_names = []
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('NO NAME PROVIDED', 'Mandy'), ('NO NAME PROVIDED', 'Jeff'), \
('NO NAME PROVIDED', 'Rick')]

    >>> given_names = ['Karina']
    >>> preferred_names = ['Kari', 'Kate']
    >>> name_mapping(given_names, preferred_names)
    [('Karina', 'Kari'), ('NO NAME PROVIDED', 'Kate')]

    >>> given_names = ['Angel', 'Ricardo', 'Brandon']
    >>> preferred_names = ['Angelito', 'Rick', 'Brandon']
    >>> name_mapping(given_names, preferred_names)
    [('Angel', 'Angelito'), ('Ricardo', 'Rick'), ('Brandon', 'Brandon')]

    >>> given_names = ['Abigail']
    >>> preferred_names = ['Abby', 'Monse']
    >>> name_mapping(given_names, preferred_names)
    [('Abigail', 'Abby'), ('NO NAME PROVIDED', 'Monse')]
    """
    names_tuple = []
    if len(given_names) < len(preferred_names):
        for i in range(len(preferred_names) - len(given_names)):
            given_names.append('NO NAME PROVIDED')

    for i in range(len(given_names)):
        names_tuple.append((given_names[i], preferred_names[i]))
    return names_tuple


# Question 2
def valid_pairs(keys, values):
    """
    Pairs a valid key with a value in a tuple in a list
    --
    Parameters:
    keys: list of dictionary keys (if valid)
    values: list of values what will go with each valid key
    -- 
    Returns:
    List of tuples with each valid key paired with its 
    respective value. If key is not valid; 'not valid' will
    return in a single tuple.

    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = [1, "fun", [2], (1,), {}]
    >>> values = [1, {}, (1,), "island", [2]]
    >>> valid_pairs(keys, values)
    [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), ('not valid',)]

    >>> keys =[]
    >>> values =[]
    >>> valid_pairs(keys, values)
    []

    >>> keys = [[1], {2: 3}]
    >>> values = ["list", "dict"]
    >>> valid_pairs(keys, values)
    [('not valid',), ('not valid',)]

    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = ["karina", ["lopez"], 'doing too much']
    >>> values = [("slays",), 6, ['not true']]
    >>> valid_pairs(keys, values)
    [('karina', ('slays',)), ('not valid',), ('doing too much', \
['not true'])]
    """
    updated_keys = []
    for key in keys:
        if type(key) == list or type(key) == dict:
            updated_keys.append('not valid')
        else:
            updated_keys.append(key)
    
    tupleeee = []
    for i in range(len(updated_keys)):
        if updated_keys[i] == 'not valid':
            tupleeee.append(((updated_keys[i]),))
        else:
            tupleeee.append((updated_keys[i], values[i]))
    return tupleeee


# Question 3
def dict_of_names(name_tuples):
    """
    Dictionary containing given names of team and all their preffered
    names.
    --
    Parameters:
    name_tuples: tuples containing team members given name and their 
    preffered name. May contain tuple with the same given name.
    --
    Returns:
    Dictionary containing the unique given name keys and their values
    being all of the preffered names given to that key/given name.
    --

    >>> dict_of_names([('Richard', 'Rick'),
    ... ('Roxanne', 'Rose'), ('Roxanne', 'Ann'),
    ... ('Richard', 'Ricky'), ('Roxanne', 'Roxie'),
    ... ('Mitchell', 'Mitch')])
    {'Richard': ['Rick', 'Ricky'], 'Roxanne': ['Rose', 'Ann', 'Roxie'], \
'Mitchell': ['Mitch']}

    >>> dict_of_names([('Melissa', 'Lisa'),
    ... ('Isabel', 'Bella'), ('NO NAME PROVIDED', 'Faith')])
    {'Melissa': ['Lisa'], 'Isabel': ['Bella'], \
'NO NAME PROVIDED': ['Faith']}

    >>> dict_of_names([('NO NAME PROVIDED', 'Derrick'), \
    ('NO NAME PROVIDED', 'Jacob')])
    {'NO NAME PROVIDED': ['Derrick', 'Jacob']}

    >>> dict_of_names([('Karina', 'Kari'), \
    ('NO NAME PROVIDED', 'Angel')])
    {'Karina': ['Kari'], 'NO NAME PROVIDED': ['Angel']}

    >>> dict_of_names([('NO NAME PROVIDED', 'Ale'), \
    ('NO NAME PROVIDED', 'Jacob'), ('no name provided', 'Kari')])
    {'NO NAME PROVIDED': ['Ale', 'Jacob'], 'no name provided': ['Kari']}

    >>> dict_of_names([('No NAME PROVIDED', 'Casey'), \
    ('NO NAME PROVIDED', 'Jacob'), ('Katelyn', 'Kate')])
    {'No NAME PROVIDED': ['Casey'], 'NO NAME PROVIDED': ['Jacob'], \
'Katelyn': ['Kate']}
    """
    new_dict = dict()
    for name, prefname in name_tuples:
        if name in new_dict:
            new_dict[name].append(prefname)
        else:
            new_dict[name] = [prefname]
    return new_dict


# Question 4.1
def contractor_payment(suggestions):
    """
    Calculates the average of all the pay suggestions for each contractor.
    --
    Parameters:
    suggestions: list of lists containing suggested pay for each contractor
    --
    Returns:
    Dictionary containing each contractor as its keys and each
    value assigned to contractor being the avg of all suggested
    pay put in the list, suggestions.

    magic number (indices): used to get key values in dictionary
    magic number (2): used to round to nearest hundredth

    >>> contractor_payment([[10, 20, 30], [0, 20, 10]])
    {'1': 5.0, '2': 20.0, '3': 20.0}

    >>> contractor_payment([[10, 20, 30], [30, 20, 10], [5, 10, 15]])
    {'1': 15.0, '2': 16.67, '3': 18.33}

    >>> contractor_payment([[-5, -10, -4], [-20, 15, 40]])
    {'1': -12.5, '2': 2.5, '3': 18.0}

    >>> contractor_payment([])
    {'1': 0, '2': 0, '3': 0}

    >>> contractor_payment([[0, 0, 0], [0, 0, 0]])
    {'1': 0.0, '2': 0.0, '3': 0.0}

    >>> contractor_payment([[100, 47, 2], [34, 2, 7]])
    {'1': 67.0, '2': 24.5, '3': 4.5}

    """
    pay_dict = dict()
    cont1 = 0
    cont2 = 0
    cont3 = 0

    if len(suggestions) == 0:
        return {'1': 0, '2': 0, '3': 0}

    for lst in suggestions:
        cont1 += lst[0]
        cont2 += lst[1]
        cont3 += lst[2]
    pay_dict['1'] = round((cont1 / len(suggestions)), 2)
    pay_dict['2'] = round((cont2 / len(suggestions)), 2)
    pay_dict['3'] = round((cont3 / len(suggestions)), 2)
    return pay_dict

# Question 4.2
def new_pay(hours):
    """
    Calculates if team deserves bonus based on whether they pass
    the expected hours
    --
    Parameters:
    hours: dictionary of hours each contractor worked
    --
    Returns:
    Creates updated dictionary with tuple containing if they get the bonus
    or not. Returns bonus pay based off equation

    magic number (return -10): requirement if required hours not met

    >>> case1 = {'1': 200, '2': 138, '3': 172}
    >>> round(new_pay(case1), 2)
    0.51
    >>> case1
    {'1': 200, '2': 138, '3': 172, 'pay': 'Bonus'}

    >>> case2 = {'1': 130, '2': 84, '3': -14}
    >>> new_pay(case2)
    -10
    >>> case2
    {'1': 130, '2': 84, '3': -14, 'pay': 'Penalty'}

    >>> case3 = {'1': 42, '2': 96, '3': 63}
    >>> round(new_pay(case3), 1)
    -2.4
    >>> case3
    {'1': 42, '2': 96, '3': 63, 'pay': 'Penalty'}

    """
    for hour in hours.values():
        if hour < 0:
            hours['pay'] = 'Penalty'
            return -10

    bonus_pay = (
        0.01 * hours['1'] + 
        0.015 * hours['2'] + 
        min(0.02 * abs(100 - hours['3']), 0.025 * hours['3']) - 5
    )

    if bonus_pay > 0:
        hours['pay'] = 'Bonus'
    elif bonus_pay == 0:
        hours['pay'] = 'No'
    else:
        hours['pay'] = 'Penalty'

    return bonus_pay

# Question 5
def potential_ideas_for_business(items):
    """
    Creates a list of unique products provided by suppliers
    --
    Parameters:
    items: dictionary containing tuples of suppliers and products they
    provide
    --
    Returns:
    List of unique products from all suppliers

    >>> items = {'supplier 1': ['Tea', 'Peaches'], \
    'supplier 2': ['Peaches', 'Apples', 'Cups']}
    >>> potential_ideas_for_business(items)
    ['Apples', 'Cups', 'Peaches', 'Tea']

    >>> items = {'supplier 1': ['Flour', 'Eggs', 'Chocolate', 'Milk'], \
    'supplier 2': ['Milk', 'Eggs', 'Vanilla', 'Butter'], \
    'supplier 3': ['Butter', 'Sugar']}
    >>> potential_ideas_for_business(items)
    ['Butter', 'Chocolate', 'Eggs', 'Flour', 'Milk', 'Sugar', 'Vanilla']

    >>> items = {'supplier 1': [], 'supplier 2': []}
    >>> potential_ideas_for_business(items)
    []

    >>> items = {'supplier 1': ['Chairs'], 'supplier 2': ['Tables'], \
'supplier 3': ['Chairs', 'Tables'], 'supplier 4': []}
    >>> potential_ideas_for_business(items)
    ['Chairs', 'Tables']

    >>> items = {'supplier 1': ['Mangoes', 'Bananas'], \
'supplier 2': ['Pineapple', 'Bananas'], 'supplier 3': ['Mangoes', 'Papaya']}
    >>> potential_ideas_for_business(items)
    ['Bananas', 'Mangoes', 'Papaya', 'Pineapple']

    >>> items = {}
    >>> potential_ideas_for_business(items)
    []
    """
    unique_items = []
    for item in items.values():
        for item1 in item:
            if item1 not in unique_items:
                unique_items.append(item1)
    return sorted(unique_items)

# Question 6.1
def count_lines_1(filepath):
    """
    Counts number of lines in a file in filepath using for keyword
    --
    Parameters:
    filepath: non-empty file 
    --
    Returns:
    count of number of lines in file from filepath 

    >>> count_lines_1('files/test1.txt')
    6
    >>> count_lines_1('files/test2.txt')
    24

    >>> count_lines_1('files/offices2.txt')
    4

    >>> count_lines_1('files/ings1.txt')
    3

    >>> count_lines_1('files/empty_trip.txt')
    0
    """
    line_count = 0
    with open(filepath, 'r') as f:
        for line in f:
            line_count += 1
    return line_count


# Question 6.2
def count_lines_2(filepath):
    """
    Counts number of lines in a file in filepath using read() function
    --
    Parameters:
    filepath: non-empty file 
    --
    Returns:
    count of number of lines in file from filepath 

    >>> count_lines_2('files/test1.txt')
    6
    >>> count_lines_2('files/test2.txt')
    24

    >>> count_lines_2('files/AlErNaTiNg.txt')
    2

    >>> count_lines_2('files/another_test.txt')
    2

    >>> count_lines_2('files/ings2.txt')
    4
    """
    with open(filepath, 'r') as f:
        str_lines = f.read()
    return len(str_lines.split('\n'))


# Question 6.3
def count_lines_3(filepath):
    """
    Counts number of lines in a file in filepath using readlines() 
    function
    --
    Parameters:
    filepath: non-empty file 
    --
    Returns:
    count of number of lines in file from filepath 

    >>> count_lines_3('files/test1.txt')
    6
    >>> count_lines_3('files/test2.txt')
    24
    >>> count_lines_2('files/ings2.txt')
    4
    >>> count_lines_2('files/another_test.txt')
    2
    >>> count_lines_2('files/offices1.txt')
    3
    """
    with open(filepath, 'r') as f:
        lst_lines = f.readlines()
    return len(lst_lines)


# Question 7
def collected_items(filepath):
    """
    Creates a list of items given from a file in filepath
    --
    Parameters:
    filepath: non-empty file 
    --
    Returns:
    list of items given in each line of a file from filepath

    magic number (<2): used to check if length is sufficient
    magic number (-2): using -2 to find the second to last item
     which is the object we want 

    >>> collected_items('files/ings1.txt')
    ['ice-cream', 'boba tea', 'fish']
    >>> collected_items('files/ings2.txt')
    ['shovel', 'headphones', 'bird', 'brownies']
    >>> collected_items('files/empty_trip.txt')
    []

    >>> collected_items('files/another_test.txt')
    []

    >>> collected_items('files/offices1.txt')
    []
    """
    item_lst = []
    with open(filepath, 'r') as f:
        for line in f:
            line_lst = line.strip().split(',')
            if len(line_lst) < 2:
                return []
            else:
                item_lst.append(line_lst[-2])
    return item_lst


# Question 8
def case_letters(filepath):
    """
    Outputs count of upper and lowercase letters in the filepath's name
    --
    Parameters:
    filepath: filepath as a string
    --
    Returns:
    Count of upper and lowercase letters in the filepath as a string

    comment: doctests kept returning what was inside the file even 
    though i copied and pasted the format of the doctest.

    >>> case_letters('files/AlErNaTiNg.txt')
    >>> with open('files/AlErNaTiNg.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    5
    13
    >>> case_letters('files/another_test.txt')
    >>> with open('files/another_test.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    19

    """

    upper_count = 0
    lower_count = 0

    for character in filepath:
        if character.isupper():
            upper_count += 1
        if character.islower():
            lower_count += 1
    
    upper_count
    lower_count
    return 

# Question 9
def map_office(filepath):
    """
    Checks if office number is valid and then maps all valid 
    numbers to a floor level. 
    --
    Parameters:
    filepath: contains n lines with office number on each line
    --
    Returns sum of all valid office numbers

    magic numbers: requirements in the directions. checks floor numbers

    >>> map_office('files/offices1.txt')
    259
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    not a valid office number
    second floor

    >>> map_office('files/offices2.txt')
    734
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    third floor and above
    not a valid office number
    second floor
    ground floor

    >>> map_office('files/offices3.txt')
    590
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    not a valid office number
    third floor and above
    ground floor

    >>> map_office('files/offices4.txt')
    32
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    not a valid office number

    >>> map_office('files/offices5.txt')
    0
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    not a valid office number
    not a valid office number
    not a valid office number
    """
    total = 0
    floors_lst = []
    with open(filepath, 'r') as f:
        for line in f:
            potential_num = int(line.strip())

            if potential_num < 1:
                floors_lst.append('not a valid office number')
            elif potential_num <= 199:
                floors_lst.append('ground floor')
                total += potential_num
            elif potential_num <= 299:
                floors_lst.append('second floor')
                total += potential_num
            else:
                floors_lst.append('third floor and above')
                total += potential_num

    with open('files/floors.txt', 'w') as output:
        for floor in floors_lst:
            output.write(floor + '\n')
    return total



