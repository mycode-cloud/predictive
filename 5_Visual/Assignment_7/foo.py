import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_6.py") # the actual check
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1():
    """Program prints correct output 1"""
    
    check50.include("Big_Mart.csv")
    assert os.path.exists("Big_Mart.csv")
    actual = check50.run("python3 Assignment_6.py").stdout(timeout=20)
    
    expected = "Item_Fat_Content\nLow Fat    2774\nRegular    1575\nLF          177\nreg          71\nlow fat      53"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first print out of .value_counts for the Item_Fat_Content column."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct output 2"""
    
    check50.include("Big_Mart.csv")
    assert os.path.exists("Big_Mart.csv")
    actual = check50.run("python3 Assignment_6.py").stdout(timeout=20)
    
    expected = "7       16\.200         0\.016687          1076\.5986"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the second print out of the first 10 rows of the 'bmn' DataFrame using the '.head' method."
        raise check50.Missing("Correct results",'your output',help=help)

        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct output 3"""
    
    check50.include("Big_Mart.csv")
    assert os.path.exists("Big_Mart.csv")
    actual = check50.run("python3 Assignment_6.py").stdout(timeout=20)
    
    expected = "Intercept        2235\.5061     58\.934     37\.932      0\.000    2119\.978    2351\.034"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the print out of results.summary()."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases4():
    """Program prints correct output 4"""
    
    check50.include("Big_Mart.csv")
    assert os.path.exists("Big_Mart.csv")
    actual = check50.run("python3 Assignment_6.py").stdout(timeout=20)
    
    expected = "adjusted coefficient of determination:  0\.007167665509702048"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the adjusted coefficient of determination."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases5():
    """Program prints correct output 5"""
    
    check50.include("Big_Mart.csv")
    assert os.path.exists("Big_Mart.csv")
    actual = check50.run("python3 Assignment_6.py").stdout(timeout=20)
    
    expected = "The results are probably not reliable because the R-square value is relatively small\."
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct final message."
        raise check50.Missing("Correct results",'your output',help=help)
    
