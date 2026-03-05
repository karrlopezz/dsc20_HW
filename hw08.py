"""
DSC 20 Spring 2025 Homework 08
Name: Karina Lopez
PID: A18356687
Source: no
"""

def q1_doctests():
    """
    Doctests for Question 1.
    
    >>> broom_1 = FlyingBroom()
    >>> broom_2 = NormalBroom()
    >>> broom_3 = CursedBroom()
    >>> broom_2.boost(20)
    True
    >>> broom_1.duel(broom_2)
    False
    >>> broom_2.high_score()
    9100
    >>> broom_2.duel(broom_3)
    False
    >>> broom_2.speed
    30
    >>> broom_3.high_score()
    25750
    >>> broom_4 = CursedBroom()
    >>> broom_3.duel(broom_4)
    True
    >>> broom_4.size
    7
    >>> broom_4.speed
    20
    >>> broom_3.size
    8
    >>> broom_4.boost(40)
    True
    >>> broom_4.lives
    6
    >>> broom_4.duel(broom_2)
    True
    >>> broom_4.high_score()
    24650
    >>> broom_4.size
    8
    >>> broom_2.speed
    50
    
    
    # ADD DOCTESTS HERE. Do NOT delete this line. #
    
    >>> karina_broom = FlyingBroom()
    >>> karina_broom.set_speed(80)
    >>> karina_broom.set_size(6)
    >>> karina_broom.set_lives()
    >>> karina_broom.speed
    80
    >>> karina_broom.size
    6
    >>> karina_broom.lives
    4
    >>> karina_broom.high_score()
    10000



    >>> karina_cursed = CursedBroom()
    >>> karina_cursed.boost(10)
    True
    >>> karina_cursed.speed > 70
    True
    >>> karina_cursed.lives >= 5
    True
    >>> karina_normal = NormalBroom()
    >>> karina_cursed.duel(karina_normal)
    True
    >>> karina_normal.lives
    2
    >>> karina_normal.speed
    50


    >>> angel_broom = CursedBroom()
    >>> angel_broom.set_speed(100)
    >>> angel_broom.set_size(9)
    >>> angel_broom.set_lives(False)
    >>> angel_broom.speed
    100
    >>> angel_broom.size
    9
    >>> angel_broom.lives
    4
    >>> angel_broom.high_score()
    21450
    """
    return

class FlyingBroom:
    """
    Implementation of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of FlyingBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): current speed of broom, default is 50
        - size (positive int): physical size of broom, default is 5
        - magic_power (non-negative int): number of magic boosts remaining
          for this broom, default is 3
        - lives (non-negative int): number of lives a wizard has while
          flying this broom, default is 3
        """
        self.speed = 50
        self.size = 5
        self.magic_power = 3
        self.lives = 3
        pass

    def boost(self, charm_power):
        """
        Boosts the speed of the broom by using a magical
        charm. Speed boost is calculated using the formula
        specified in the write-up. If boost is successfully
        applied (enough magic power to perform boost), return True.
        Otherwise (no remaining magic power to perform boost), return False.
        
        Parameters:
        - charm_power (int): used to calcualte speed boost formula.
          Applied as long the broom still has some magic power
          remaining.
        """
        if self.magic_power <= 0:
            return False

        old_speed = self.speed
        new_speed = int(((old_speed + charm_power) ** 2\
         + (old_speed - charm_power) ** 2) ** (1/2))

        old_score = self.high_score()
        self.speed = new_speed
        new_score = self.high_score()
        if new_score >= 2 * old_score:
            self.set_lives(True)
        self.magic_power -= 1
        return True
        pass

    def set_speed(self, new_speed):
        """
        Setter method that assigns given speed value to 
        speed attribute.
        
        Parameters:
        - new_speed (int): new speed value
        """
        self.speed = new_speed
        pass

    def set_lives(self, gains = True):
        """
        Setter method that increments lives attribute 
        by 1 if gains is True, otherwise decrement by 1.
        
        Parameters:
        - gains (bool): decides whether to increment/decrement
          lives attribute by 1.
        """
        if gains:
            self.lives += 1
        else:
            self.lives -= 1
        pass

    def set_size(self, new_size):
        """
        Setter method that assigns given size value
        (non-negative) to size attribute.
        
        Parameters:
        - new_size (non-negative int): new size value
        """
        if new_size >= 0:
            self.size = new_size
        pass

    def duel(self, other_broom):
        """
        Determines if a duel can occur between
        current broom and other_broom. If so,
        the following happens as specified in
        the write-up. Return True if current
        broom successfully performs duel, otherwise
        False.
        
        Parameters:
        - other_broom (object): Broom object
        """
        if self.size > other_broom.size:
            other_broom.set_speed(other_broom.speed - 50)
            self.set_speed(self.speed + 50)
            if other_broom.speed <= 0:
                other_broom.set_lives(False)
                other_broom.set_speed(50)
                self.set_size(self.size + 1)
            return True
        elif self.size < other_broom.size:
            self.set_speed(self.speed - 50)
            other_broom.set_speed(other_broom.speed + 50)
            if self.speed <= 0:
                self.set_lives(False)
                self.set_speed(50)
                other_broom.set_size(other_broom.size + 1)
            return False
        else:
            return False
        pass

    def high_score(self):
        """
        Formula for high score and returns it.
        """
        return self.speed * 100 + self.lives * 500
        pass

class NormalBroom(FlyingBroom):
    """
    Implementation of NormalBroom. Subclass of FlyingBroom.
    """
    def duel(self, other_broom):
        """
        Duel method for NormalBroom.
        - If other_broom is an instance of CursedBroom,
          current NormalBroom loses one life, and its speed 
          resets to 30.
        - CursedBroom object gains a size, and its speed
          increases by 50.
        - Attack is thus considered unsuccessful, function
          returns False.
        - If other_broom is not a CursedBroom object, duel
          method is the same as in the parent class.
        
        Parameters:
        - other_broom (object): Broom object
        """
        if isinstance(other_broom, CursedBroom):
            self.set_lives(False)
            self.set_speed(30)
            other_broom.set_size(other_broom.size + 1)
            other_broom.set_speed(other_broom.speed + 50)
            return False
        else:
            return super().duel(other_broom)
        pass

class CursedBroom(FlyingBroom):
    """
    Implementation of CursedBroom. Subclass of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of CursedBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): default is 70
        - size (positive int): default is 7
        - magic_power (non-negative int): default is 5
        - lives (non-negative int): default is 5
        """
        self.speed = 70
        self.size = 7
        self.magic_power = 5
        self.lives = 5
        pass

    def high_score(self):
        """
        Formula for a CursedBroom high score and returns it.
        """
        return self.speed * 200 + self.lives * 300 + 250
        pass


# Question 2
# Q2, Part 1
def fix_1(lst1, lst2):
    """
    divides each element in lst1 by each element in lst2
    --
    Parameters:
    lst1: list of integers
    lst2: list of integers
    --
    Returns:
    Output list of each element in lst1 divided by each element\
    in lst2

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    
    # NO DOCTESTS NEEDED #
    """
    out = []
    for div in lst2:
        for num in lst1:
            try:
                out.append(num / div) # add try-catch block
            except ZeroDivisionError:
                continue
    return out

# Q2, Part 2
def fix_2(*filepaths):
    """
    Opens each file in *filepaths
    --
    Parameters:
    *filepaths: tuple of filepaths
    --
    Returns:
    '{filepath} opened' if filepath valid\
    '{filepath} not found' if filepath not valid

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found
    >>> fix_2('docs.txt')
    docs.txt not found
    
    # NO DOCTESTS NEEDED #
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r") # add try-catch block
            cur_file.close()
            print(f"{filepath} opened")
        except:
            print(f"{filepath} not found") 

# Q2, Part 3
def fix_3(lst):
    """
    adds each element with the following element in lst
    --
    Parameters:
    lst: list of elements
    --
    Returns:
    list of element added with following element or prints\
    types of errors caught

    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []
    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]
    >>> fix_3([])
    []
    
    # NO DOCTESTS NEEDED #
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try:
            sum_of_pairs.append(lst[i] + lst[i + 1]) # add try-catch block
        except (TypeError, IndexError) as error:
            print(type(error))
    return sum_of_pairs


# Question 3
def check_inputs(input1, input2):
    """
    checks the correctness of input1 and input2
    --
    Parameters:
    input1: list of numeric values
    input2: numeric value that exists in input1
    --
    Returns:
    Excptions if conditions not met.\
     If met, returns "Input validated"

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'
    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    
    # Add at least 3 doctests below here. Do NOT delete this line. #
    """
    if not isinstance(input1, list):
        raise TypeError("input1 is not the correct type")

    i = 0
    while i < len(input1):
        numb = input1[i]
        if not isinstance(numb, (int, float)):
            raise TypeError(f"The element at index {i}\
 is not numeric")
        i += 1

    if not isinstance(input2, (int, float)):
        raise TypeError(f"input2 is not the correct type")

    if input2 not in input1:
        raise TypeError("input2 not in input1")
    return "Input validated"


# Question 4
def load_file(filepath):
    """
    checks the correctness of the given filepath
    --
    Parameters:
    filepath: valid and existing filepath (str)
    --
    Returns:
    number of words in filepath if filepath a string, existing,\
    and not empty

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    >>> load_file('files/ten_words.txt')
    10
    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty
    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist
    
    # Add at least 3 doctests below here. Do NOT delete this line. #

    >>> load_file('files/karina.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/karina.txt does not exist

    >>> load_file('files/some_words.txt')
    13

    >>> load_file(805439)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath is not a string")
    
    try:
        test_file = open(filepath, "r")
        file = test_file.read()
        test_file.close()
    except:
        raise FileNotFoundError(f"{filepath} does not exist")

    words = file.split()
    if len(words) == 0:
        raise ValueError("File is empty")
    
    return len(words)