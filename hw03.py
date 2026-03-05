"""
DSC 20 Spring 2025 Homework 03
Name: Karina Lopez
PID: A18356687
Source: ChatGPT further explanation on .join()
"""
# Question 1.1
def operate_nums(lst):
    """
    Doubles odd numbers, tripples even numbers in list
    --
    Parameters:
    lst: list of integers
    --
    Returns:
    if all numbers in list are integers, returns a list of original
    odd numbers doubled and original even numbers trippled

    >>> operate_nums([1, 2, 3, 's'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3.1, -2, 0, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3, -2, 0, 5])
    [6, 6, -6, 0, 10]

    >>> operate_nums([4, 2, 5, 1.0])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> operate_nums([4, 2, 6, -12])
    [12, 6, 18, -36]

    >>> operate_nums([0, 0, 0, 0])
    [0, 0, 0, 0]
    """
    assert isinstance(lst, list)
    assert all([isinstance(num, int) for num in lst])
    return [num * 2 if num % 2 != 0 else num * 3 for num in lst]

# Question 1.2
def string_lengths(text, nums):
    """
    Creates list of booleans. True if number of characters in
    first string in text is greater than first number in nums and
    so on
    --
    Parameters:
    text: list of non-empty strings
    nums: list of positive integers
    --
    Returns:
    list of boolean values depending on if the len of a string in
    text is greater than an integer in nums

    >>> string_lengths(['a', 'b', 'c'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['', 'abc'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['a', 'b'], [-1, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['abc', 'abcd', 'abcde'], [2, 5, 5])
    [True, False, False]

    >>> string_lengths(['Karina', 'Lopez', 'Kari'], [6, 3, 8])
    [False, True, False]

    >>> string_lengths([''], [1, 5])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> string_lengths(['Karina', 'Lopez', 'Kari'], [6, 5, 4])
    [False, False, False]
    """
    assert isinstance(text, list)
    assert isinstance(nums, list)
    assert all([isinstance(tex, str) and len(tex) > 0 for tex in text])
    assert all([isinstance(num, int) and num > 0 for num in nums])
    assert len(text) == len(nums)
    return [True if len(text[i]) > nums[i] else False for i in 
    range(len(text))]

# Question 1.3
def process_dict(input_dict):
    """
    takes dictionary where keys are tuples and values are lists of strings,
    and returns list of integers where each integer is a sum of
    the length of the key and the total length of all the strings
    in the value list
    --
    Parameters:
    input_dict: dictionary where keys are tuples and values are lists
    of strings
    -- 
    Returns:
    list of integers where each integer is length of key and 
    length of all strings in the values list.
    
    >>> process_dict({1: ['a', 'b', 'c'], (1, 2): ['a']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['a', 0], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['dsc', 'dsc20', 'dsc30'], (2,): \
    ['b']})
    [15, 2]

    >>> process_dict({(1, 2, 5): ['Karina', 'lol', 'Kari'], (15,): \
    ['astrophysicist']})
    [16, 15]

    >>> process_dict({(1, 2): ['a', 0]})
    Traceback (most recent call last):
    ...
    AssertionError

    >>> process_dict({(1,): ['hi', 'there'], (2, 3, 4): ['maria']})
    [8, 8]
    """
    assert isinstance(input_dict, dict)
    assert all([isinstance(tup, tuple) for tup in input_dict.keys()])
    assert all([isinstance(val, list) and all(isinstance(string, str)\
 for string in val) for val in input_dict.values()])
    return [len(key) + sum(len(strings) for strings in val)\
 for key, val in input_dict.items()] 

# Question 2
def unusual_sort(indices, items):
    """
    Reorders items based on given indices and returns list of tuples
    --
    Parameters:
    indices: list of integers
    items: list of items
    --
    Returns:
    list of tuples. each containing its new reordered item, its original
    index and its new index

    >>> unusual_sort([0, 4, 2, 3, 1], \
        ["zero", "four", "two", "three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), \
('three', 3, 3), ('four', 1, 4)]

    >>> unusual_sort([0.0, 4.0, 2.0, 3.0, 1.0], \
    ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3, 0], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 1, 2, 7], \
    ['apple', 'karina', 'maria', 'adrian'])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 1, 2, 3], \
        ['apple', 'carrot', 'karina', 'banana'])
    [('apple', 0, 0), ('carrot', 1, 1), ('karina', 2, 2),\
 ('banana', 3, 3)]

    >>> unusual_sort([0, 4, 2, 3, 0], \
        ["zero", "four", "two"])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(indices, list)
    assert isinstance(items, list)
    assert len(indices) == len(items)
    assert all(isinstance(num, int) for num in indices)
    assert sorted(indices) == list(range(len(indices)))
    return [(items[indices[i]], indices[i], i) for i in range(len(items))]

# Question 3
def change_input(strange_list):
    """
    For each string in list, doubles the digits and capitalizes
    letters that are lowercase
    --
    Parameters:
    strange_list: list of strings
    --
    Returns:
    new list of modified strings

    >>> change_input(["3.14IS PIE", "11My aGe iS"])
    ['6.28IS PIE', '22My AGE IS']
    >>> change_input(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO t12O slEEp At ', '10I lIkE tO stArt wOrk bEfOrE ']
    >>> change_input("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError

    >>> change_input(['Karins389', 'KArinA'])
    ['KArIns61618', 'KArInA']

    >>> change_input("karina")
    Traceback (most recent call last):
    ...
    AssertionError

    >>> change_input(["karina", 12122005])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(strange_list, list)
    assert all([isinstance(string, str) for string in strange_list])
    return [''.join([str(int(char)*2) if char.isdigit() \
else char.upper() if char in 'aeiou' else char for char in string])\
 for string in strange_list]

# Question 4
def change_input_even_more(strange_list):
    """
    For each string in list, doubles the digits, puts them at the end
    and capitalizes letters that are lowercase
    --
    Parameters:
    strange_list: list of strings using digits and letters
    --
    Returns:
    new list of modified strings

    >>> change_input_even_more(["3.14IS PIE", "11My aGe iS"])
    ['.IS PIE628', 'My AGE IS22']
    >>> change_input_even_more(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO tO slEEp At 12', 'I lIkE tO stArt wOrk bEfOrE 10']
    >>> change_input_even_more("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError

    >>> change_input_even_more("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError

    >>> change_input_even_more(["11My aGe iS"])
    ['My AGE IS22']

    >>> change_input_even_more(['aeiou99'])
    ['AEIOU1818']

    >>> change_input_even_more(['00'])
    ['00']
    """
    assert isinstance(strange_list, list)
    assert all(isinstance(string, str) for string in strange_list)
    return [
    ''.join([char.upper() if char in 'aeiou' else char for char in 
        string if not char.isdigit()]) + ''.join([str(int(char) * 2) 
        for char in string if char.isdigit()
        ]) for string in strange_list]

# Question 5.1
def cheapest_gas(gas_stations, mileage):
    """
    Finds brand name with lowest price among reachable station
    -- 
    Parameters:
    gas_stations: dictionary where keys are gas brand names and
    values are list of 2-tuples
    mileage: non-negative integer representing mileage
    --
    Returns:
    gas station name with lowest price in a reachable distance

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.3), (10, 5.4)] \
    }
    >>> cheapest_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_gas(gas_stations, 20)
    'Shell'

    >>> cheapest_gas(gas_stations, 100)
    'Shell'

    >>> cheapest_gas(gas_stations, 10)
    'Arco'

    >>> cheapest_gas(gas_stations, 30)
    'Shell'
    """
    return min([(price, company) for company in gas_stations\
 for dist, price in gas_stations[company] if dist <= mileage])[1]

# Question 6
def new_orders(orders, action, dish_name, amount):
    """
    Creates dictionary with updated values for dishes
    --
    Parameters:
    order: dictionary where keys are strings and values are positive
    integers
    action: string of either 'add' or 'remove'
    dish_name: dish name that need to be updated (string)
    amount: amount dish needs to be updated (non-negative integer)
    --
    Returns:
    updated dictionary with new amount for given dish name in paremeter

    >>> orders = {'pizza': 10, 'burger': 5}
    >>> new_orders(orders, 'add', 'pizza', 5)
    {'pizza': 15, 'burger': 5}

    >>> new_orders(orders, 'remove', 'burger', 3)
    {'pizza': 10, 'burger': 2}

    >>> new_orders(orders, 'remove', 'pizza', 15)
    {'pizza': 0, 'burger': 5}

    >>> new_orders([], 'remove', 'burger', 3)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> new_orders(orders, 'add', 'burger', 20)
    {'pizza': 10, 'burger': 25}

    >>> new_orders(orders, 'remove', 'fries', 3)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> new_orders(orders, 'add', 'pizza', -5)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(orders, dict)
    assert all(isinstance(keys, str) for keys in orders.keys())
    assert all(isinstance(vals, int) for vals in orders.values())
    assert dish_name in orders.keys() 
    assert amount >= 0
    return {dish: (val + amount if dish == dish_name and
     action == 'add' else max(0, val - amount) if dish == dish_name
      and action == 'remove' else val) for dish, val in orders.items()}