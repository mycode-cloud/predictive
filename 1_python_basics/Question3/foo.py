import check50 # import the check50 module
import check50.py
import re

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question3.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases(exists):
    """Program prints correct sum """
    check50.include("Question3_Sol.py")
    check50.py.append_code("Question3.py", "Question3_Sol.py")
    
    check50.run("python3 Question3.py").stdout("Johannes Jamal Galina").exit()
    
    actual = check50.run("python3 Question3.py").stdout()
    
    if "Johannes Jamal Galina" not in actual:
        help = r"Your code does not work with the list ['Johannes', 'Jamal', 'Jamal', 'Johannes', 'Galina']."
        raise check50.Missing("Johannes Jamal Galina", actual, help=help)
    if "66" not in actual:
        help = r"Your code does not work with the arrays [1,2,3,4,5] and [6,7,8,9,10,11].  Your code is being checked against several different arrays."
        raise check50.Missing("66", actual, help=help)
    if "78" not in actual:
        help = r"Your code does not work with the arrays [1,2,3,4,5] and [6,7,8,9,10,11,12].  Your code is being checked against several different arrays."
        raise check50.Missing("78", actual, help=help)
