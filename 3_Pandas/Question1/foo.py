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
    check50.exists("Question1.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases():
    """Program prints the correct mean for 'speeds' - Test 1"""
    
    actual = check50.run("python3 Question1.py").stdout()
    expected1 = 20.77333333333333
    
    if not re.search(sep_num(expected1), actual):
        help = r"Your code does not print the correct mean for 'speeds'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
     
