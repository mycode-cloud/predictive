import check50 # import the check50 module
import check50.py
import re

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_0.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases11(exists):
    """Program prints correct output for reshaped array 'a'"""
    
    actual = check50.run("python3 Assignment_0.py").stdout()
    expected = "\[\[1 2\]\n \[3 4\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the reshaped array 'a'."
        raise check50.Missing("Reshaped array 'a'",'your output',help=help)
      
    
    
@check50.check(exists) # only run this check if the exists check has passed
def check_cases12(exists):
    """Program prints correct output for sum 'b+c'"""
    
    actual = check50.run("python3 Assignment_0.py").stdout()
    expected = "\[\[5 5\]\n \[5 5\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the the sum 'b+c'."
        raise check50.Missing("Sum array 'b+c'",'your output',help=help)
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases21(exists):
    """Program prints correct output for reshaped array 'a2'"""
    
    actual = check50.run("python3 Assignment_0.py").stdout()
    expected = "\[\[9 8\]\n \[7 6\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the reshaped array 'a2'."
        raise check50.Missing("Reshaped array 'a2'",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases22(exists):
    """Program prints correct output for sum 'b2+c'"""
    
    actual = check50.run("python3 Assignment_0.py").stdout()
    expected = "\[\[15 15\]\n \[15 15\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the the sum 'b2+c'."
        raise check50.Missing("Sum array 'b2+c'",'your output',help=help)
        
        
        

        
        
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases31(exists):
    """Program prints correct output for reshaped sample arrays"""
    check50.include("Assignment_0_Sol.py")
    check50.py.append_code("Assignment_0.py", "Assignment_0_Sol.py")
    
    actual = check50.run("python3 Assignment_0.py").stdout()
    expected = "\[\[2 3\]\n \[4 5\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct reshaped result for other possible arrays."
        raise check50.Missing('Sample reshaped array','sample output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases32(exists):
    """Program prints correct output for sum of sample arrays"""
    check50.include("Assignment_0_Sol.py")
    check50.py.append_code("Assignment_0.py", "Assignment_0_Sol.py")
    
    actual = check50.run("python3 Assignment_0.py").stdout()
    expected = "\[\[7 7\]\n \[7 7\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for other possible arrays."
        raise check50.Missing('Sample sum array','sample output',help=help)

        



