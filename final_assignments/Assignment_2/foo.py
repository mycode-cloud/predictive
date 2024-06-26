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
    
    expected = "The shape of the original DataFrame is:\s*\(9999, 14\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the original DataFrame."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct output 2"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "After dropping all rows containing empty entries\, the shape of the updated DataFrame is:\s*\(6814, 14\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the DataFrame after dropping all rows containing empty entries."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct output 3"""
   
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "host_identity_verified\s*category"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first print out of the updated column data types."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases4():
    """Program prints correct output 4"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "unconfirmed\s*3447\nverified\s*3367"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the print out of the result of .value_counts() for cat_abnb3."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases5():
    """Program prints correct output 5"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "The list of column names representing categorical data in the cleaned abnb3 DataFrame is\s*\[\'host_identity_verified\', \'instant_bookable'"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the print out of the list of column names representing categorical data in the cleaned abnb3 DataFrame."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases6():
    """Program prints correct output 6"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "The list of column names representing all data, with dummy variables included, in the cleaned abnb3 DataFrame is\s*\[\'id\', \'lat\', \'long\'"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the print out of the list of the columns in 'abnb3_dummies' using the 'tolist()' method."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases7():
    """Program prints correct output 7"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "coefficient of determination:\s*0\.5396677955761835"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the coefficient of determination."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases8():
    """Program prints correct output 8"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "service_fee\s*1\.855570"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the service_fee regression coefficient."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases9():
    """Program prints correct output 9"""
    
    actual = check50.run("python3 Assignment_2.py").stdout(timeout=20)
    
    expected = "The predicted price for the test data in abnb3_xtest is:\s*1943\.04"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the predicted price for the test data in abnb3_xtest."
        raise check50.Missing("Correct results",'your output',help=help)
