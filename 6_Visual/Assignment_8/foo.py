import check50 # import the check50 module
import check50.py
import re

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_8.py") # the actual check
    
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1():
    """Program prints correct output 1"""
    
    actual = check50.run("python3 Assignment_8.py").stdout(timeout=20)
    
    expected = r"\s*\[ 0\.  0\.  0\. \.\.\. 16\.  9\.  0\.\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first print out 'x'."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct output 2"""
   
    actual = check50.run("python3 Assignment_8.py").stdout(timeout=20)
    
    expected = "0\.9992044550517104"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for model.score(x_train,y_train)."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct output 3"""
   
    actual = check50.run("python3 Assignment_8.py").stdout(timeout=20)
    
    expected = r"\s*\[ 0  0  0  0  0  0  0  0  2 57\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first confusion matrix print out."
        raise check50.Missing("Correct results",'your output',help=help)
    
