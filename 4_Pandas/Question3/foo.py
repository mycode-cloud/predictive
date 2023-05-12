import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question3.py") # the actual check

        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1(exists):
    """Program prints correct output 1"""
    
    check50.include("StudentsPerformance.csv")
    assert os.path.exists("StudentsPerformance.csv")
    
    
    actual = check50.run("python3 Question3.py").stdout()
    expected = "2           90             95             93\n3           47             57             44\n4           76             78             75"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for your first10_numerical print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2(exists):
    """Program prints correct output 2"""
    
    check50.include("StudentsPerformance.csv")
    assert os.path.exists("StudentsPerformance.csv")
    
    actual = check50.run("python3 Question3.py").stdout()
    expected = "994          63             63             62\n995          88             99             95\n996          62             55             55"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for your last10_numerical print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3(exists):
    """Program prints correct output 3"""
    
    check50.include("StudentsPerformance.csv")
    assert os.path.exists("StudentsPerformance.csv")
    
    actual = check50.run("python3 Question3.py").stdout()
    expected = "2          90             95             93"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for your excellent_students print out."
        raise check50.Missing("Correct results",'your output',help=help)
