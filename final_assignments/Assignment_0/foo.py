import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_0.py") # the actual check
    
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1():
    """Program prints correct output 1"""
    
    check50.include("Airbnb_0.csv")
    assert os.path.exists("Airbnb_0.csv")
    
    actual = check50.run("python3 Assignment_0.py").stdout(timeout=20)
    
    expected = r"1005202\s*\$1\,060\s*\$212\s*45\.0\s*49\.0\s*0\.40"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first print out of abnb.head(10)."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct output 2"""
    
    check50.include("Airbnb_0.csv")
    assert os.path.exists("Airbnb_0.csv")
   
    actual = check50.run("python3 Assignment_0.py").stdout(timeout=20)
    
    expected = "The shape of the original DataFrame is: \(9999, 7\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the original DataFrame."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct output 3"""
    
    check50.include("Airbnb_0.csv")
    assert os.path.exists("Airbnb_0.csv")
   
    actual = check50.run("python3 Assignment_0.py").stdout(timeout=20)
    
    expected = "After dropping all rows containing empty entries, the shape of the updated DataFrame is: \(8388, 7\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the updated DataFrame."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases4():
    """Program prints correct output 4"""
    
    check50.include("Airbnb_0.csv")
    assert os.path.exists("Airbnb_0.csv")
   
    actual = check50.run("python3 Assignment_0.py").stdout(timeout=20)
    
    expected = "All column headings of the DataFrame with spaces replaced by underscores are: Index\(\[\'id\', \'price\', \'service_fee\'"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the column headings of the DataFrame with spaces replaced by underscores."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases5():
    """Program prints correct output 5"""
    
    check50.include("Airbnb_0.csv")
    assert os.path.exists("Airbnb_0.csv")
   
    actual = check50.run("python3 Assignment_0.py").stdout(timeout=20)
    
    expected = "7\s*1005202\s*1060\.0\s*212\.0\s*45\.0\s*49\.0\s*0\.40"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the last .head(10) print statement."
        raise check50.Missing("Correct results",'your output',help=help)
        
