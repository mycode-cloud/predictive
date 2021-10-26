import check50 # import the check50 module
import check50.py

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question2.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases(exists):
    """Program prints correct sum """
    check50.include("Question2_Sol.py")
    check50.py.append_code("Question2.py", "Question2_Sol.py")
    check50.run("python3 Question2.py").stdout("55").exit()
    check50.run("python3 Question2.py").stdout("66").exit()
    check50.run("python3 Question2.py").stdout("78").exit()
    
    actual = check50.run("python3 Question2.py").stdout()
    if 66 not in actual:
        help = r"Your code does not work with the arrays [1,2,3,4,5] and [6,7,8,9,10,11]"
        raise check50.Mismatch("66", actual, help=help)
    if 78 not in actual:
        help = r"Your code does not work with the arrays [1,2,3,4,5] and [6,7,8,9,10,11,12]"
        raise check50.Mismatch("78", actual, help=help)
