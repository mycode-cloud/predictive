import check50 # import the check50 module
import check50.py
import re

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question1.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases(exists):
    """Program prints correct output """
    check50.include("Question1_Sol.py")
    check50.py.append_code("Question1.py", "Question1_Sol.py")
    
    actual = check50.run("python3 Question1.py").stdout()
    expected1_1 = '[[1,2]'
    expected1_2 = '[3,4]]'
    expected2 = r'\[\[5,5\]\n \[5,5\]\]'
    expected3 = r'\[\[9,8\]\n \[7,6\]\]'
    expected4 = r'\[\[15,15\]\n \[15,15\]\]'
    expected5 = r'\[\[2,3\]\n \[4,5\]\]'
    expected6 = r'\[\[7,7\]\n \[7,7\]\]'
    
    if not re.search(expected1_1, actual):
        help = r"Your code does not print the correct result for the reshaped array 'a'."
        raise check50.Missing('Reshaped array','Given output',help=help)
