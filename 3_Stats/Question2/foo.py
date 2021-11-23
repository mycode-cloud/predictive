import check50 # import the check50 module
import re
import check50.py

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question2.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases():
    """Program prints correct name length - Test 1"""
    actual = check50.run("python3 Question2.py").stdin("XXXXX").stdin("XXXXX").stdout()
    expected = "10"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for a student with name length 10."
        raise check50.Missing('Correct name length','your output',help=help)