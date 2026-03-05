"""
DSC 20 Spring 2025 Homework 09
Name: Karina Lopez
PID: A18356687
Source: me
"""

# Question 1
def question_1():
    """
    1 if a method mutates an object 
	0 otherwise

	>>> answer = question_1()
	>>> len(answer) == 10
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer])
	False
    """
    return [0, 0, 0, 1, 1, 0, 0, 1, 0, 1]


# Question 2
def question_2():
    """
    1 if a method is in place
	0 otherwise

	>>> answer = question_2()
	>>> len(answer)==5
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer ])
	False
    """
    return [1, 1, 1, 1, 1]


# Question 3
def reverse_list(lst):
    """ 
    Reverses given list keeping it in-place (does not create new list)
    --
    Parameters:
    lst: list of objects
    --
    Returns:
    reversed version of the list without creating new list.\
    does not return anything

    >>> x = [3, 2, 4, 5]
    >>> reverse_list(x)
    >>> x
    [5, 4, 2, 3]
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE. #

    >>> x = ['karina', 'angel', 'ally', 'rick']
    >>> reverse_list(x)
    >>> x
    ['rick', 'ally', 'angel', 'karina']

    >>> x = ['un', 'even', 'list']
    >>> reverse_list(x)
    >>> x
    ['list', 'even', 'un']

    >>> x = ['karina']
    >>> reverse_list(x)
    >>> x
    ['karina']

    """
    for i in range(len(lst) // 2):
    # i only goes halfway so it can take one from back and one\
    #from front
        lst[i], lst[-1 - i] = lst[-1 - i], lst[i]


# Question 4
def swap_lists(alist1, alist2):
    """
    Takes two lists and swaps elements in place. Lists have same size
    --
    Parameters:
    alist1: list
    alist2: list
    --
    Returns:
    modifies list in place. Does not return anything

    >>> list1 = [1, 2]
    >>> list2 = [3, 4]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [3, 4]
    >>> print(list2)
    [1, 2]

    >>> list1 = [4, 2, 6, 8, 90, 45]
    >>> list2 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 41, 65, 43, 4, 17]
    >>> print(list2)
    [4, 2, 6, 8, 90, 45]

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE. #

    >>> list1 = ['karina', 'angel']
    >>> list2 = ['rick', 'ally']
    >>> swap_lists(list1, list2)
    >>> print(list1)
    ['rick', 'ally']
    >>> print(list2)
    ['karina', 'angel']

    >>> list1 = ['karina']
    >>> list2 = ['angel']
    >>> swap_lists(list1, list2)
    >>> print(list1)
    ['angel']
    >>> print(list2)
    ['karina']

    >>> list1 = ['karina', 'rick', 'ally']
    >>> list2 = ['angel', 'ally', 'karina']
    >>> swap_lists(list1, list2)
    >>> print(list1)
    ['angel', 'ally', 'karina']
    >>> print(list2)
    ['karina', 'rick', 'ally']
    """
    for i in range(len(alist1)):
        alist1[i], alist2[i] = alist2[i], alist1[i]