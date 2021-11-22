import check50 # import the check50 module
import check50.py
import re


def search_n(num):
    # regex that matches `num` not surrounded by any other numbers
    # (so search_n(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question2.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases(exists):
    """Program prints correct sum - Test 1"""
    check50.include("Question2_Sol.py")
    check50.py.append_code("Question2.py", "Question2_Sol.py")
    
    actual = check50.run("python3 Question2.py").stdout()
    
    if "55" not in actual:
        help = r"Your code does not work with the arrays [1,2,3,4,5] and [6,7,8,9,10]."
        raise check50.Missing("55", 'your output', help=help)       
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2(exists):
    """Program prints correct sum - Test 2"""
    check50.include("Question2_Sol.py")
    check50.py.append_code("Question2.py", "Question2_Sol.py")
    
    actual = check50.run("python3 Question2.py").stdout()
    
    if "66" not in actual:
        help = r"Your code does not work with the arrays [1,2,3,4,5] and [6,7,8,9,10,11].  Your code is being checked against several different arrays."
        raise check50.Missing("66", 'your output', help=help)
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3(exists):
    """Program prints correct sum - Test 3"""
    check50.include("Question2_Sol.py")
    check50.py.append_code("Question2.py", "Question2_Sol.py")
    
    actual = check50.run("python3 Question2.py").stdout()
    
    if "78" not in actual:
        help = r"Your code does not work with the arrays [1,2,3,4,5] and [6,7,8,9,10,11,12].  Your code is being checked against several different arrays."
        raise check50.Missing("78", 'your output', help=help)
