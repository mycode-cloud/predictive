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
    check50.exists("Assignment_2.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases():
    """Program prints the correct variance and standard deviation for 'speeds' - Test 1"""
    
    actual = check50.run("python3 Assignment_n3.py").stdout()
    expected1 = "[26.05885057  5.10478703]"
    
    if not re.search(expected1, actual):
        help = r"Your code does not print the correct variance and standard deviation for 'speeds'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
        
        
    
        
@check50.check(check_cases) # only run this check if the exists check has passed
def check_cases2():
    """Program prints the correct variance and standard deviation for 'speeds2' - Test 2"""
    
    actual = check50.run("python3 Assignment_2.py").stdout()
    expected2 = "[30.506      5.5232237]"
    
    if not re.search(expected2, actual):
        help = r"Your code does not print the correct variance and standard deviation for 'speeds2'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
        
        
        
        
@check50.check(check_cases2) # only run this check if the exists check has passed
def check_cases3():
    """Program prints the correct variance and standard deviation for random data speeds - Test 3"""
    check50.include("Assignment_2_Sol.py")
    check50.py.append_code("Assignment_2.py", "Assignment_2_Sol.py")
    
    actual = check50.run("python3 Assignment_2.py").stdout()
    expected3 = "[34.85742857  5.904018  ]"
    
    if not re.search(expected3, actual):
        help = r"Your code does not work for other data speeds.  Your code is being checked against several different data lists."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
