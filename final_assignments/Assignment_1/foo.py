import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_1.py") # the actual check
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1():
    """Program prints correct output 1"""
    
    actual = check50.run("python3 Assignment_1.py").stdout(timeout=20)
    
    expected = "The shape of the original DataFrame is:\s*\(9999, 11\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the original DataFrame."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct output 2"""
    
    actual = check50.run("python3 Assignment_1.py").stdout(timeout=20)
    
    expected = "After dropping all rows containing empty entries\, the shape of the updated DataFrame is:\s*\(6893, 11\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the DataFrame after dropping all rows containing empty entries."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct output 3"""
   
    actual = check50.run("python3 Assignment_1.py").stdout(timeout=20)
    
    expected = "The R-squared value for price vs\.\s*minimum_nights\s*is\s*0\.0007275938878409383"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the print out of the R-squared value for price vs. minimum_nights."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases4():
    """Program prints correct output 4"""
    
    actual = check50.run("python3 Assignment_1.py").stdout(timeout=20)
    
    expected = "The R-squared value for price vs\.\s*service_fee\s*is\s*0\.501482384702971"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the print out of the R-squared value for price vs. service_fee."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases5():
    """Program prints correct output 5"""
    
    actual = check50.run("python3 Assignment_1.py").stdout(timeout=20)
    
    expected = "The R-squared value for price vs\.\s*availability_365\s*is\s*0\.49198510125291073"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the print out of the R-squared value for price vs. availability_365."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases6():
    """Program prints correct output 6"""
    
    actual = check50.run("python3 Assignment_1.py").stdout(timeout=20)
    
    expected = "coefficient of determination:\s*0\.5388016431708234"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the coefficient of determination for the multi-variable model."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases7():
    """Program prints correct output 7"""
    
    actual = check50.run("python3 Assignment_1.py").stdout(timeout=20)
    
    expected = "availability_365\s*-1.627559"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the availability_365 regression coefficient."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases8():
    """Program prints correct output 8"""
    
    actual = check50.run("python3 Assignment_1.py").stdout(timeout=20)
    
    expected = "service_fee\s*1\.858834"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the service_fee regression coefficient."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases9():
    """Program prints correct output 9"""
    
    actual = check50.run("python3 Assignment_1.py").stdout(timeout=20)
    
    expected = "The predicted price for the test data in abnb1_xtest is:\s*2078\.21"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the predicted price for the test data in abnb2_xtest."
        raise check50.Missing("Correct results",'your output',help=help)

