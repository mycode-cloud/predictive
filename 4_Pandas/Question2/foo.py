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
    check50.exists("Question2.py") # the actual check
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1(exists):
    """Program prints correct output 1"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "7    98\n8    45\n9    98"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for first math scores print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2(exists):
    """Program prints correct output 2"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "1004    97\n1005    96\n1006    56"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the second math scores print out."
        raise check50.Missing("Correct results",'your output',help=help)
