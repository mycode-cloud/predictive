import check50 # import the check50 module
import re
import check50.py

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question4.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases():
    """Program prints correct weighted average - Test 1"""
    actual = check50.run("python3 Question4.py").stdin("81").stdin("42").stdin("79").stdin("81").stdin("19").stdin("12").stdin("6").stdin("63").stdout()
    expected = "76.2"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for SAMPLE_DATA#1."
        raise check50.Missing('Correct weighted average','your output',help=help)
    
@check50.check(check_cases) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct weighted average - Test 2"""
    actual = check50.run("python3 Question4.py").stdin("28").stdin("6").stdin("18").stdin("48").stdin("47").stdin("83").stdin("55").stdin("89").stdout()
    expected = "70.76"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result SAMPLE_DATA#2."
        raise check50.Missing('Correct weighted average','your output',help=help)
    
@check50.check(check_cases2) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct weighted average - Test 3"""
    actual = check50.run("python3 Question4.py").stdin("22").stdin("13").stdin("7").stdin("58").stdin("87").stdin("72").stdin("92").stdin("76").stdout()
    expected = "79.02"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result random weights and grades."
        raise check50.Missing('Correct weighted average','your output',help=help)
