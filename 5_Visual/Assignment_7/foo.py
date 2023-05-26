import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_7.py") # the actual check
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1():
    """Program prints correct output 1"""
    
    check50.include("Big_Mart.csv")
    assert os.path.exists("Big_Mart.csv")
    actual = check50.run("python3 Assignment_7.py").stdout(timeout=20)
    
    expected = r"Item_Fat_Content\nLow Fat\s+(?:\b2774\b|\b53\b)\nRegular\s+(?:\b1575\b|\b\d\d\b)\nLF\s+\b177\b\nreg\s+\b71\b\nlow fat\s+(?:\b2774\b|\b53\b)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first print out of .value_counts for the Item_Fat_Content column."
        raise check50.Missing("Correct results",'your output',help=help)
        
