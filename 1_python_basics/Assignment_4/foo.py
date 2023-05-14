import check50 # import the check50 module
import check50.py
import re

def sep_num(num):
    # regex that matches `num` not surrounded by any other numbers
    # (so coins(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_4.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases():
    """Program prints correct number of points for organizer - Test 1"""
    check50.include("Assignment_4_Sol.py")
    check50.py.append_code("Assignment_4.py", "Assignment_4_Sol.py")
    
    actual = check50.run("python3 Assignment_4.py").stdout()
    expected1 = "25\n"
    
    if not re.search(sep_num(25), actual):
        help = r"Your code does not print the correct result for 'Johannes'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
        
        
        
        
        
@check50.check(check_cases) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct number of points for organizer - Test 2"""
    check50.include("Assignment_4_Sol.py")
    check50.py.append_code("Assignment_4.py", "Assignment_4_Sol.py")
    
    actual = check50.run("python3 Assignment_4.py").stdout()
    expected2 = "5\n"
    
    if not re.search(sep_num(5), actual):
        help = r"Your code does not work for 'John'.  Your code is being checked against several different cases."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
        
        
        
        
@check50.check(check_cases2) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct number of points for organizer - Test 3"""
    check50.include("Assignment_4_Sol.py")
    check50.py.append_code("Assignment_4.py", "Assignment_4_Sol.py")
    
    actual = check50.run("python3 Assignment_4.py").stdout()
    expected3 = "55\n"
    
    if not re.search(sep_num(55), actual):
        help = r"Your code does not work for other dictionaries.  Your code is being checked against several different dictionaries."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
        
        
        
        
        
@check50.check(check_cases3) # only run this check if the exists check has passed
def check_cases4():
    """Program prints correct number of points for organizer - Test 4"""
    check50.include("Assignment_4_Sol.py")
    check50.py.append_code("Assignment_4.py", "Assignment_4_Sol.py")
    
    actual = check50.run("python3 Assignment_4.py").stdout()
    expected4 = "35\n"
    
    if not re.search(sep_num(35), actual):
        help = r"Your code does not work for other dictionaries.  Your code is being checked against several different dictionaries."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
