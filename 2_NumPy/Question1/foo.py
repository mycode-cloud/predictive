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
    
    actual = check50.run("python3 Question1.py").stdout(regex=True)
    expected1 = r'\[\[1,2\]\n \[3,4\]\]'
    expected2 = r'\[\[5,5\]\n \[5,5\]\]'
    expected3 = r'\[\[9,8\]\n \[7,6\]\]'
    expected4 = r'\[\[15,15\]\n \[15,15\]\]'
    expected5 = r'\[\[2,3\]\n \[4,5\]\]'
    expected6 = r'\[\[7,7\]\n \[7,7\]\]'
    
    if not re.search(expected1, actual):
        help = r"Your code does not print the correct result for 'a'."
        raise check50.Mismatch("[[1,2]\n [3,4]]", actual, help=help)
    if not re.search(expected2, actual):
        help = r"Your code does not print the correct sum 'b+c'."
        raise check50.Mismatch(expected2, actual, help=help)
    if not re.search(expected3, actual):
        help = r"Your code does not print the correct result for 'a2'."
        raise check50.Mismatch(expected3, actual, help=help)
    if not re.search(expected4, actual):
        help = r"Your code does not print the correct sum 'b2+c'."
        raise check50.Mismatch(expected4, actual, help=help)
    if not re.search(expected5, actual):
        help = r"Your code does not print the correct result for other arrays."
        raise check50.Mismatch(expected5, actual, help=help)
    if not re.search(expected6, actual):
        help = r"Your code does not print the correct sum for other arrays."
        raise check50.Mismatch(expected6, actual, help=help)
