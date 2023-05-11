import check50 # import the check50 module
import check50.py
import re

def sep_num(num):
    # regex that matches `num` not surrounded by any other numbers
    # (so coins(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question1.py") # the actual check
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1(exists):
    """Program prints correct output for 'first12['gender'].value_counts()'"""
    
    actual = check50.run("python3 Question1.py").stdout()
    expected = "'The group of students with the highest mean scores in math, writing, and reading had a majority of female students.'"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for 'first12['gender'].value_counts()'."
        raise check50.Missing("'first12['gender'].value_counts()'",'your output',help=help)

    
