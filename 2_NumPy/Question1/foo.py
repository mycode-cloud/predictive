import check50 # import the check50 module
import check50.py
import re

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question1.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases11(exists):
    """Program prints correct output for reshaped array 'a'"""
    
    actual = check50.run("python3 Question1.py").stdout()
    expected11 = '[[1,2]'
    expected12 = '[3,4]]'
    
    if not (re.search(re.escape(expected11), actual) and re.search(re.escape(expected12), actual)):
        help = r"Your code does not print the correct result for the reshaped array 'a'."
        raise check50.Missing("Reshaped array 'a'",'your output',help=help)
      
    
    
@check50.check(exists) # only run this check if the exists check has passed
def check_cases12(exists):
    """Program prints correct output for sum 'b+c'"""
    
    actual = check50.run("python3 Question1.py").stdout()
    
    expected11 = r'\\[\\[5,5\\]'
    expected12 = r'\\[5,5\\]\]]'
    
    if not (re.search(expected11, actual) and re.search(expected12, actual)):
        help = r"Your code does not print the correct result for the the sum 'b+c'."
        raise check50.Missing("Sum array 'b+c'",'your output',help=help)
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases21(exists):
    """Program prints correct output for reshaped array 'a2'"""
    
    actual = check50.run("python3 Question1.py").stdout()
    expected11 = r'\\[\\[9,8\\]'
    expected12 = r'\\[7,6\\]\\]'
    
    if not (re.search(expected11, actual) and re.search(expected12, actual)):
        help = r"Your code does not print the correct result for the reshaped array 'a2'."
        raise check50.Missing("Reshaped array 'a2'",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases22(exists):
    """Program prints correct output for sum 'b2+c'"""
    
    actual = check50.run("python3 Question1.py").stdout()
    
    expected11 = r'\\[\\[15,15\\]'
    expected12 = r'\\[15,15\\]\]]'
    
    if not (re.search(expected11, actual) and re.search(expected12, actual)):
        help = r"Your code does not print the correct result for the the sum 'b2+c'."
        raise check50.Missing("Sum array 'b2+c'",'your output',help=help)
        
        
        

        
        
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases31(exists):
    """Program prints correct output for reshaped sample arrays"""
    check50.include("Question1_Sol.py")
    check50.py.append_code("Question1.py", "Question1_Sol.py")
    
    actual = check50.run("python3 Question1.py").stdout()
    expected11 = '\\[\\[2,3\\]'
    expected12 = '\\[4,5\\]\\]'
    
    if not (re.search(expected11, actual) and re.search(expected12, actual)):
        help = r"Your code does not print the correct reshaped result for other possible arrays."
        raise check50.Missing('Sample reshaped array','sample output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases32(exists):
    """Program prints correct output for sum of sample arrays"""
    check50.include("Question1_Sol.py")
    check50.py.append_code("Question1.py", "Question1_Sol.py")
    
    actual = check50.run("python3 Question1.py").stdout()
    
    expected11 = r'\\[\\[7,7\\]'
    expected12 = r'\\[7,7\\]\]]'
    
    if not (re.search(expected11, actual) and re.search(expected12, actual)):
        help = r"Your code does not print the correct result for other possible arrays."
        raise check50.Missing('Sample sum array','sample output',help=help)




