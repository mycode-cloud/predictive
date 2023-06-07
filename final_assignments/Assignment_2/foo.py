import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_2.py") # the actual check
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1():
    """Program prints correct output 1"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "The shape of the original DataFrame is:\s*\(9999, 11\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the original DataFrame."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct output 2"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "After dropping all rows containing empty entries\, the shape of the updated DataFrame is:\s*\(6893, 11\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the DataFrame after dropping all rows containing empty entries."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct output 3"""
   
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "The R-squared valued for price vs\.\s*minimum_nights\s*is\s*0\.0007275938878409383"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the print out the R-squared value for price vs. minimum_nights."
        raise check50.Missing("Correct results",'your output',help=help)
