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
    check50.exists("Question2.py") # the actual check
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1(exists):
    """Program prints correct output 1"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "7    98\n8    45\n9    98"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for first math_scores print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2(exists):
    """Program prints correct output 2"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "1004    97\n1005    96\n1006    56"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the second math_scores print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3(exists):
    """Program prints correct output 3"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "1002    35\n1003    69\n1004    99"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first writing_scores print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases4(exists):
    """Program prints correct output 4"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "1005    84\n1006    85\n1007    36"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first reading_scores print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases4(exists):
    """Program prints correct output 5"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "1007          98             36             68\n1008          45             77             43\n1009          98             88             29"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the extra_student_scores print out."
        raise check50.Missing("Correct results",'your output',help=help)
        
        

