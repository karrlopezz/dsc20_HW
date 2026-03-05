"""
DSC 20 Spring 2025 Homework 04
Name: Karina Lopez
PID: A18356687
"""

# Question 1
def place_of_birth(file_in):
    """
    Creates dictionary with keys as city names and values as people
    born there
    --
    Parameters:
    file_in: file containing player' information
    --
    Returns:
    Dictionary with keys as city names and values as people
    born there recieved from the file inputted into the function

    >>> place_of_birth('files/info_1.txt')
    {'Chicago': ['Rob'], 'New York': ['Ella'], 'New York.': ['Mary']}
    >>> place_of_birth('files/info_2.txt')
    {'Chicago': ['Rob'], 'London': ['Ezra'], 'Paris': \
['Mary'], 'paris': ['Ron', 'Harry']}
    >>> place_of_birth('files/header.txt')
    {}

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    
    >>> place_of_birth('files/info_3.txt')
    {'San Diego': ['Sue'], 'London': ['Ben']}

    >>> place_of_birth('files/info_4.txt')
    {'Paris': ['Kate']}

    >>> place_of_birth('files/info_5.txt')
    {'Oxnard': ['Karina', 'Angel'], 'El Paso': ['Rick']}
    """
    with open(file_in, 'r') as f:
        birth_dct = dict()
        next(f)
        for line in f:
            splt_lns = line.strip().split(', ')
            name = splt_lns[0].strip()
            city = splt_lns[1].strip()
            if city not in birth_dct:
                birth_dct[city] = []
            birth_dct[city].append(name)
        return birth_dct


# Question 2
def age_groups(file_in, file_out):
    """
    Inputs name and a number next to it depending on if they are
    older (1), younger (-1) or exactly 35 (0) into the file_out. 
    --
    Parameters:
    file_in: file where name, city, dob information is contained
    file_out: file we want the name and indicator to be shown
    --
    Returns:
    file with imported data 

    >>> age_groups('files/info_1.txt', 'files/age_1_out.txt')
    >>> with open('files/age_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ella,1
    Mary,-1
    
    >>> age_groups('files/info_2.txt', 'files/age_2_out.txt')
    >>> with open('files/age_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ezra,1
    Mary,1
    Ron,0
    Harry,0

    >>> age_groups('files/header.txt', 'files/empty_out.txt')
    >>> with open('files/empty_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #

    >>> age_groups('files/info_3.txt', 'files/empty.txt')
    >>> with open('files/empty.txt', 'r') as outfile3:
    ...    for line in outfile3:
    ...       print(line.strip())
    name,older than 35
    Sue,-1
    Ben,1

    >>> age_groups('files/info_4.txt', 'files/mpty.txt')
    >>> with open('files/mpty.txt', 'r') as outfile4:
    ...    for line in outfile4:
    ...       print(line.strip())
    name,older than 35
    Kate,1

    >>> age_groups('files/info_5.txt', 'files/empty1.txt')
    >>> with open('files/empty1.txt', 'r') as outfile5:
    ...    for line in outfile5:
    ...       print(line.strip())
    name,older than 35
    Karina,-1
    Angel,-1
    Rick,-1
    """
    with open(file_in, 'r') as f_in:
        with open(file_out, 'w') as f_out:
            f_out.write('name,older than 35\n')
            next(f_in)
            for line in f_in:
                splt_lns = line.strip().split(', ')
                name = splt_lns[0].strip()
                dob = splt_lns[2].strip()
                dob_year = int(dob.split('/')[2])
                age = 2024 - dob_year
                if age > 35:
                    f_out.write(name + ',1\n')
                elif age < 35:
                    f_out.write(name + ',-1\n')
                else:
                    f_out.write(name + ',0\n')
                

# Question 3
def several_files(files_lst, file_out):
    """
    Inputs the name, city, and dob of a player into the file_out;
    replacing the month in the dob with the name of the month
    instead of the numerical version (ex. 01 = Jan)
    --
    Parameters:
    files_lst: list of files to look through
    file_out: file we are inputting our data into
    --
    Returns:
    file with information of players from the list of files. 
    Again, with the numerical version of the month replaced with
    the name of the month.

    >>> lst_1 = ['files/info_1.txt','files/info_3.txt', 'files/info_4.txt']
    >>> several_files(lst_1, 'files/several_1_out.txt')
    >>> with open('files/several_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ella,New York,Apr 09 1970
    Mary,New York.,Jan 01 2004
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    Kate,Paris,Jul 13 1945

    >>> lst_2 = ['files/info_2.txt','files/header.txt']
    >>> several_files(lst_2, 'files/several_2_out.txt')
    >>> with open('files/several_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ezra,London,Apr 12 1978
    Mary,Paris,Sep 11 1975
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989


    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #

    >>> lst_3 = ['files/info_2.txt','files/info_3.txt']
    >>> several_files(lst_3, 'files/several_3_out.txt')
    >>> with open('files/several_3_out.txt', 'r') as outfile3:
    ...    for line in outfile3:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ezra,London,Apr 12 1978
    Mary,Paris,Sep 11 1975
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970

    >>> lst_4 = ['files/info_3.txt','files/info_4.txt']
    >>> several_files(lst_4, 'files/several_4_out.txt')
    >>> with open('files/several_4_out.txt', 'r') as outfile4:
    ...    for line in outfile4:
    ...       print(line.strip())
    name,city,DOB
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    Kate,Paris,Jul 13 1945

    >>> lst_5 = ['files/info_4.txt','files/info_5.txt']
    >>> several_files(lst_5, 'files/several_5_out.txt')
    >>> with open('files/several_5_out.txt', 'r') as outfile5:
    ...    for line in outfile5:
    ...       print(line.strip())
    name,city,DOB
    Kate,Paris,Jul 13 1945
    Karina,Oxnard,Dec 12 2005
    Angel,Oxnard,Oct 28 2001
    Rick,El Paso,Apr 10 2004
    """
    month_dict = {'01':'Jan', '02':'Feb', '03':'Mar', 
        '04':'Apr', '05':'May', '06':'Jun', '07':'Jul', 
        '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
    with open(file_out, 'w') as f_out:
                f_out.write('name,city,DOB\n')
                for file_in in files_lst:
                    with open(file_in, 'r') as f_in:
                        next(f_in)
                        for line in f_in:
                            splt_lns = line.strip().split(', ')
                            name = splt_lns[0].strip()
                            city = splt_lns[1].strip()
                            dob = splt_lns[2].strip()
                            dob_splt = dob.split('/')
                            new_dob = month_dict[dob_splt[0]] + ' ' + \
                            dob_splt[1] + ' ' + dob_splt[2]
                            f_out.write(name+','+city+','+new_dob+'\n')


# Question 4
def postcards(info_list):
    """
    Creates a dictionary with name and postcard created from information
    in list of tuples given. Postcards have to be under $75.
    --
    Parameters:
    infor_list: list of tuples that contains name, price, age,
    and place 
    --
    Returns:
    dictionary with keys being the full names and values are 
    the corresponding postcards

    >>> postcards([
    ...     ('Yue Wang', 96, 18, 'Hoover Dam'),
    ...     ('Cleo Patra', 10, 32, 'Bellagios')
    ... ])
    {'Cleo Patra': 'cle32patra0soigalleb'}
    >>> postcards([])
    {}
    >>> postcards([
    ...     ('Mari Noh', 155, 18, 'tram'),
    ...     ('Gwen Am', 34, 54, 'Venetian'),
    ...     ('Freya Dog', 34, 1, 'The Strip')
    ... ])
    {'Gwen Am': 'gwe54am4naitenev', 'Freya Dog': 'fre1dog4pirts eht'}

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #
    >>> postcards([
    ...     ('Karina Lopez', 20, 19, 'San Diego')
    ... ])
    {'Karina Lopez': 'kar19lopez0ogeid nas'}

    >>> postcards([
    ...     ('Karina Lopez', 20, 19, 'San Diego'),
    ...     ('Angel Martinez', 60, 25, 'Oxnard')
    ... ])
    {'Karina Lopez': 'kar19lopez0ogeid nas', \
'Angel Martinez': 'ang25martinez0dranxo'}

    >>> postcards([
    ...     ('Crystal Ball', 60, 23, 'The Strip'),
    ...     ('Ashley Garcia', 20, 27, 'Hoover Dam'),
    ...     ('Karina Lopez', 20, 19, 'San Diego')
    ... ])
    {'Crystal Ball': 'cry23ball0pirts eht',\
 'Ashley Garcia': 'ash27garcia0mad revooh',\
 'Karina Lopez': 'kar19lopez0ogeid nas'}
    """
    assert isinstance(info_list, list)
    assert all(isinstance(tup, tuple) for tup in info_list)
    assert all(isinstance(tup[0], str) and isinstance(tup[3], str)
     for tup in info_list)
    assert all(isinstance(tup[1], int) and isinstance(tup[2], int)
     for tup in info_list)

    pstcrd = filter(lambda tup: tup[1] < 75, info_list)
    cards = map(lambda tup: (tup[0],(tup[0].split()[0][:3] + str(tup[2])
     + tup[0].split()[1] + str(tup[1] % 10) + tup[3][::-1])
    .lower()), pstcrd)
    return dict(cards)


# Question 5
def win_or_lose(lst, operations):
    """
    Applies inputted operations on the inputted list of integers and
    returns final result
    --
    Parameters:
    lst: list of integers
    operations: list of operations. each operation is a tuple.
    first item in the tuple is the operation name.
    second item is the value to apply with the operation.
    --
    Returns:
    Either a string or a list depending on the operation

    >>> lst = [1, 12, 123, 1234, 12345, 123456]
    >>> operations_1 = [('advance', 5), ('lost', 3), ('tie', 4)]
    >>> win_or_lose(lst, operations_1)
    [14, 125, 1236, 12347, 123458]
    >>> operations_2 = [('lost', 200), ('eliminate', 'Team ')]
    >>> win_or_lose(lst, operations_2)
    ['Team lost', 'Team lost', 'Team lost', 'Team won', 'Team won', 'Team won']

    # Add at least 3 doctests below here. DO NOT DELETE THIS LINE #

    >>> lst = [10, 20, 30, 40]
    >>> operations_2 = [('advance', 5), ('lost', 10), ('tie', 5),\
 ('win', 'final score: ')]
    >>> win_or_lose(lst, operations_2)
    'final score: 80'

    >>> lst = [100, 200, 300]
    >>> operations_3 = [('lost', 50), ('eliminate', 'Player ')]
    >>> win_or_lose(lst, operations_3)
    ['Player won', 'Player won', 'Player won']

    >>> lst = [1, 2, 3]
    >>> operations_4 = [('lost', 1), ('tie', 0), ('win', 'game score: ')]
    >>> win_or_lose(lst, operations_4)
    'game score: 3'
    """

    valid_opers = {'advance', 'lost', 'tie', 'eliminate', 'win'}
    assert isinstance(lst, list) and all(isinstance(x, int) for x in lst)\
 and len(lst) > 0
    assert isinstance(operations, list)
    assert all(oper[0] in valid_opers for oper in operations)

    commands = {
            'advance': lambda lst, amount: list(
                map(lambda x: x + amount, lst)),
            'lost': lambda lst, amount: list(
                map(lambda x: x - amount, lst)),
            'tie': lambda lst, threshold: list(
                filter(lambda x: x >= threshold, lst)),
            'eliminate':  lambda lst, symbol: list(
                map(lambda x: symbol + ('won' if x > 0 else 'lost'), lst)),
            'win': lambda lst, message: message + str(sum(lst))
    }
    for oper in operations:
        name, parameter = oper
        lst = commands[name](lst, parameter)
    return lst
