"""
DSC 20 Spring 2025 Homework 06
Name: Karina Lopez
PID: A18356687
"""

#Question 1
def randomize(*args):
    """ 
    returns a dictionary where the keys are the data types
     and the values are lists of items
    --
    Parameters:
    *args: series of arguments 
    --
    Returns:
    dictionary where the keys are the data types and
    the values are lists of items, organized according to the rules below.

    If the type is a:
    string: keep the characters at the even indices of the string,
     i.e. (0th, 2nd, 4th, 6th index and so on…)

    int: if even cast to True, if odd cast to False.

    float: if negative, convert to equivalent positive value,
     if non-negative, change it into int by cutting off
      everything after the decimal.

    list: use its length as a value for a corresponding
     dictionary list.

    Anything else: key is 'garbage', and use unchanged
     arguments as values for a corresponding dictionary list.

    >>> randomize(1, 2.3, False, 'DSC20')
    {'int': [False], 'float': [2], 'garbage': [False], 'str': ['DC0']}
    >>> randomize(True, 4, 'ABC', -9.8, [1,2,3], 'a', False)
    {'garbage': [True, False], 'int': [True], 'str': ['AC', 'a']\
, 'float': [9.8], 'list': [3]}
    >>> randomize(False, True, 'DS', True, 'abc', -3.2, 5, {'a': 1}, -2, ' .')
    {'garbage': [False, True, True, {'a': 1}], 'str': ['D', 'ac', ' ']\
, 'float': [3.2], 'int': [False, True]}
    >>> randomize()
    {}
    >>> randomize(True)
    {'garbage': [True]}

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> randomize(3.21, 'garbage', 'karina', 0)
    {'float': [3], 'str': ['grae', 'krn'], 'int': [True]}

    >>> randomize('Karina Lopez', 312.3, 'hi', '3.2')
    {'str': ['Krn oe', 'h', '32'], 'float': [312]}

    >>> randomize('Karina', 15, 3.14, [1, 2, 3, 4], 'hello', True)
    {'str': ['Krn', 'hlo'], 'int': [False], 'float': [3],\
 'list': [4], 'garbage': [True]}
    """
    result = {}
    for arg in args:
        if isinstance(arg, bool):
            key = 'garbage'
            value = arg
        elif isinstance(arg, str):
            key = 'str'
            value = arg[::2]
        elif isinstance(arg, int):
            key = 'int'
            value = (arg % 2 == 0)
        elif isinstance(arg, float):
            key = 'float'
            value = abs(arg) if arg < 0 else int(arg)
        elif isinstance(arg, list):
            key = 'list'
            value = len(arg)
        else:
            key = 'garbage'
            value = arg

        if key not in result:
            result[key] = []
        result[key].append(value)

    return result 

#Question 2
def rearrange_args(*args, **kwargs):
    """
    combines the positional arguments (*args) and
     keyword arguments (**kwargs) into a list of tuples
    --
    Parameters:
    *args: positional arguments
    **kwargs: keyword arguments
    --
    Returns:
    A list of tuples where each tuple contains:
    - the type of the argument ('positional' or 'keyword')
    - the index of the argument within *args or **kwargs
     (using 0-based indexing)
    - the value of the argument.

    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> rearrange_args(25, 30, karina='dragon',\
 player1='hero', carla='villain')
    [('positional_0', 25), ('positional_1', 30),\
 ('keyword_0_karina', 'dragon'), ('keyword_1_player1', 'hero'),\
 ('keyword_2_carla', 'villain')]

    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False),\
 ('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]

    >>> rearrange_args(3.14, True, karina='chocolate', carla=[1,2,3])
    [('positional_0', 3.14), ('positional_1', True),\
 ('keyword_0_karina', 'chocolate'), ('keyword_1_carla', [1, 2, 3])]
    """
  
    def positional(i, args):
        """creates tuples froom positional arguments"""
        if i == len(args):
            return []
        return [(f'positional_{i}', args[i])]\
         + positional(i + 1, args)

    def keyword(i, keys):
        """creates tuples from keyword arguments"""
        if i == len(keys):
            return []
        key = keys[i]
        return [(f'keyword_{i}_{key}', kwargs[key])]\
         + keyword(i + 1, keys)

    return positional(0, args) + keyword(0, list(kwargs))

#Question 3.1
def count_the_password(lst, password):
    """
    compute the number of times the password appears in the list
    --
    Parameters:
    lst: list of strings
    password: string
    --
    Returns:
    number of times the password appears in the list

    >>> count_the_password(["cooldragon", "dragon", "gold"], "dragon")
    1
    >>> count_the_password(["DRAGON", "dragon!!"], "dragon")
    0
    >>> count_the_password([], "dragon")
    0
    >>> count_the_password(["dragon "], "dragon")
    0
    >>> count_the_password(["dragon", "likes", "recursions", "right", \
"dragon", "?"], "dragon")
    2

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> count_the_password(["Karina", "the", "DRAGON"], "dragon")
    0

    >>> count_the_password(["Karina loves dragons",\
 "dragon", "Karina", "dragon"], "dragon")
    2

    >>> count_the_password(["Karina", "dragon.", "gold"], "dragon")
    0
    """
    if len(lst) == 0:
        return 0
    if lst[0] == password:
        count = 1
    else:
        count = 0
    return count + count_the_password(lst[1:], password)

#Question 3.2  
def corrupt_password(input, to_insert):
    """
    takes in a single string, a character to_insert and
    returns a corrupted new string where each character
    is followed by a to_insert character. 
    --
    Parameters:
    input: single string
    to_insert: character
    --
    Returns:
    corrupted new string where each character is followed by
     a to_insert character

    >>> corrupt_password('dragon', '#')
    'd#r#a#g#o#n#'
    >>> corrupt_password('', '@')
    ''
    >>> corrupt_password('I can help', '-')
    'I- -c-a-n- -h-e-l-p-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> corrupt_password('Karina loves dragons', '*')
    'K*a*r*i*n*a* *l*o*v*e*s* *d*r*a*g*o*n*s*'

    >>> corrupt_password('I am the dragon', '!')
    'I! !a!m! !t!h!e! !d!r!a!g!o!n!'

    >>> corrupt_password('Karina', ' ')
    'K a r i n a '
    """
    if input == '':
        return ''
    first = input[0]
    """ first means first char in remaining string"""
    rest = input[1:]
    return first + to_insert + corrupt_password(rest, to_insert) 

# Question 3.3
def outsmart_dragon(lst, password, to_insert):
    """
    corrupts all strings except ones that match the password
    --
    Parameters:
    lst: list of strings
    password: password to look for (string)
    to_insert: element to insert
    --
    Returns:
    corrupts string that is not the password where each
     character is followed by a to_insert character

    >>> outsmart_dragon(['dragon'], 'dragon','#')
    ['dragon']
    >>> outsmart_dragon([], 'dragon','@')
    []
    >>> outsmart_dragon(['help me', 'dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'dragon']
    >>> outsmart_dragon(['help me', 'dear dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'd-e-a-r- -d-r-a-g-o-n-']
    >>> outsmart_dragon(['DrAgOn', 'Dragon'], 'dragon','-')
    ['D-r-A-g-O-n-', 'D-r-a-g-o-n-']

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> outsmart_dragon(['Karina', 'likes dragons'], 'dragon', '*')
    ['K*a*r*i*n*a*', 'l*i*k*e*s* *d*r*a*g*o*n*s*']

    >>> outsmart_dragon(['Karina loves dragons', 'Dragon'],\
 'dragon', '$')
    ['K$a$r$i$n$a$ $l$o$v$e$s$ $d$r$a$g$o$n$s$', 'D$r$a$g$o$n$']

    >>> outsmart_dragon(['dragon', 'DRAGON', 'karina',\
 'DRaGoN'], 'karina', '-')
    ['d-r-a-g-o-n-', 'D-R-A-G-O-N-', 'karina', 'D-R-a-G-o-N-']
    """
    if len(lst) == 0:
        return []
    first = lst[0]
    """ first means first in lst """
    rest = outsmart_dragon(lst[1:], password, to_insert)
    if first == password:
        return [first] + rest
    else:
        return [corrupt_password(first, to_insert)] + rest 

#Question4
def corrupt_with_vowels(input):
    """
    removes vowels from an input string
    --
    Parameters:
    input: string
    --
    Returns:
    string without the vowels. not case-sensitive

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> corrupt_with_vowels('DRAGON is coming for you')
    'DRGN s cmng fr y'

    >>> corrupt_with_vowels('AEIOUaeiou')
    ''

    >>> corrupt_with_vowels('Karina and the dragon')
    'Krn nd th drgn'
    """
    vowels = 'aeiouAEIOU'
    if len(input) == 0:
        return ''
    first_char = '' if input[0] in vowels else input[0]
    return first_char + corrupt_with_vowels(input[1:])

#Question 5
def where_to_go(point1, point2, separator):
    """
    returns a string with all integers between point1 and point2
     (both ends are included) separated by a third parameter.
    --
    Parameters:
    point1: integer (starting point)
    point2: integer (ending point)
    seperator: string
    --
    Returns:
    string with all integers between point1 and point2
    (both ends are included) separated by a third parameter.

    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> where_to_go(5, 10, '')
    '5678910'

    >>> where_to_go(-3, 2, '|')
    '-3|-2|-1|0|1|2'

    >>> where_to_go(-2, 2, '_Karina_')
    '-2_Karina_-1_Karina_0_Karina_1_Karina_2'
    """
    if point1 == point2:
        return str(point1)
    elif point1 < point2:
        return str(point1) + separator\
 + where_to_go(point1 + 1, point2, separator)
    else:
        return str(point1) + separator\
 + where_to_go(point1 - 1, point2, separator)
