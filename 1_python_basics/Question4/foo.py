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
    
    if "Johannes Jamal Galina" not in actual:
        help = r"Your code does not work with the list ['Johannes', 'Jamal', 'Jamal', 'Johannes', 'Galina']."
        raise check50.Missing("Johannes Jamal Galina", actual, help=help)
    if "a b c" not in actual:
        help = r"Your code does not work with the list ['a', 'a', 'a', 'b', 'b', 'c'].  Your code is being checked against several different lists."
        raise check50.Missing("a b c", actual, help=help)
    if "d e f g" not in actual:
        help = r"Your code does not work with the ['d', 'd', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'g', 'g'].  Your code is being checked against several different lists."
        raise check50.Missing("d e f g", actual, help=help)
