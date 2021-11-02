import check50 # import the check50 module
import check50.py
import re

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question4.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases(exists):
    """Program prints correct number of points for organizer """
    check50.include("Question4_Sol.py")
    check50.py.append_code("Question4.py", "Question4_Sol.py")
    
    actual = check50.run("python3 Question4.py").stdout()
    
    if "25" not in actual:
        help = r"Your code does not print the correct result for 'Johanne'."
        raise check50.Missing("25", actual, help=help)
    if "5" not in actual:
        help = r"Your code does not work for 'John'.  Your code is being checked against several different cases."
        raise check50.Missing("a b c", actual, help=help)
    if "d e f g" not in actual:
        help = r"Your code does not work for other dictionaries.  Your code is being checked against several different dictionaries."
        raise check50.Missing("d e f g", actual, help=help)
