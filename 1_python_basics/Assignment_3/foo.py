import check50 # import the check50 module
import check50.py
import re

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_3.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases():
    """Program prints correct list - Test 1"""
    check50.include("Assignment_3_Sol.py")
    check50.py.append_code("Assignment_3.py", "Assignment_3_Sol.py")
    
    actual = check50.run("python3 Assignment_3.py").stdout()
    
    if "Johannes Jamal Galina" not in actual:
        help = r"Your code does not work with the list ['Johannes', 'Jamal', 'Jamal', 'Johannes', 'Galina']."
        raise check50.Missing("Correct output", "your output", help=help)                          
                              
                              
                              
@check50.check(check_cases) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct list - Test 2"""
    check50.include("Assignment_3_Sol.py")
    check50.py.append_code("Assignment_3.py", "Assignment_3_Sol.py")
    
    actual = check50.run("python3 Assignment_3.py").stdout()
    
    if "a b c" not in actual:
        help = r"Your code does not work with the list ['a', 'a', 'a', 'b', 'b', 'c'].  Your code is being checked against several different lists."
        raise check50.Missing("Correct output", "your output", help=help)
                              
                              
                              
                              
                              
@check50.check(check_cases2) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct list - Test 3"""
    check50.include("Assignment_3_Sol.py")
    check50.py.append_code("Assignment_3.py", "Assignment_3_Sol.py")
    
    actual = check50.run("python3 Assignment_3.py").stdout()
    
    if "d e f g" not in actual:
        help = r"Your code does not work with a random list.  Your code is being checked against several different lists."
        raise check50.Missing("Correct output", "your output", help=help)

        
        
        
        
        
        
