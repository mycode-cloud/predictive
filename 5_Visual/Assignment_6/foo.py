import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_6.py") # the actual check
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1(exists):
    """Program prints correct output 1"""
    
    check50.include("Big_Mart_Numerical.csv")
    assert os.path.exists("Big_Mart_Numerical.csv")
    
    actual = check50.run("python3 Assignment_6.py").stdout()
    expected = r"\(8523, 3\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first print out of 10 rows of bmn using the head() method\."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2(exists):
    """Program prints correct output 2"""
    
    check50.include("Big_Mart_Numerical.csv")
    assert os.path.exists("Big_Mart_Numerical.csv")
    
    actual = check50.run("python3 Assignment_6.py").stdout()
    expected = r"7       16\.200         0\.016687          1076\.5986\n"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the second print out of 10 rows of 'bmn' using the '.head()' method."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3(exists):
    """Program prints correct output 3"""
    
    check50.include("Big_Mart_Numerical.csv")
    assert os.path.exists("Big_Mart_Numerical.csv")
    
    actual = check50.run("python3 Assignment_6.py").stdout()
    expected = "Intercept        2235\.5061     58\.934     37\.932      0\.000    2119\.978    2351\.034"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the results.summary() print out."
        raise check50.Missing("Correct results",'your output',help=help)
    
