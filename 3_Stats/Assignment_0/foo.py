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
    check50.exists("Assignment_0.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases():
    """Program prints the correct mean for 'speeds' - Test 1"""
    
    actual = check50.run("python3 Assignment_0.py").stdout()
    expected1 = 20.77333333333333
    
    if not re.search(sep_num(expected1), actual):
        help = r"Your code does not print the correct mean for 'speeds'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
        
        
    
        
@check50.check(check_cases) # only run this check if the exists check has passed
def check_cases2():
    """Program prints the correct mean for 'speeds2' - Test 2"""
    
    actual = check50.run("python3 Assignment_0.py").stdout()
    expected2 = 18.3
    
    if not re.search(sep_num(expected2), actual):
        help = r"Your code does not print the correct mean for 'speeds2'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
        
        
        
        
@check50.check(check_cases2) # only run this check if the exists check has passed
def check_cases3():
    """Program prints the correct mean for random data speeds - Test 3"""
    check50.include("Assignment_0_Sol.py")
    check50.py.append_code("Assignment_0.py", "Assignment_0_Sol.py")
    
    actual = check50.run("python3 Assignment_0.py").stdout()
    expected3 = 20.98
    
    if not re.search(sep_num(expected3), actual):
        help = r"Your code does not work for other data speeds.  Your code is being checked against several different data lists."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
