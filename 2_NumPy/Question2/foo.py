import check50 # import the check50 module
import check50.py
import re

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question2.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases11(exists):
    """Program prints correct output for subarray of 'a'"""
    
    actual = check50.run("python3 Question1.py").stdout()
    expected = "\[\[1 2\]\n \[5 6\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the subarray of 'a'."
        raise check50.Missing("Subarray of 'a'",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases12(exists):
    """Program prints correct output for subarray of 'b'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "\[\[27 28\]\n \[31 32\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the subarray of 'b'."
        raise check50.Missing("Subarray of 'b'",'your output',help=help)
      
    
    
@check50.check(exists) # only run this check if the exists check has passed
def check_cases13(exists):
    """Program prints correct output for difference 'a-b'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "\[\[-26 -26\]\n \[-26 -26\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the difference 'a-b'."
        raise check50.Missing("Difference array 'a-b'",'your output',help=help)
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases14(exists):
    """Program prints correct output for elementwise multiplication of subarrays for 'a' and 'b'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "\[\[27 56\]\n \[155 192\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for elementwise multiplication for 'a' and 'b' subarrays."
        raise check50.Missing("Multiplication subarray",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases15(exists):
    """Program prints correct output for elementwise division of subarrays for 'a' and 'b'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "\[\[0.03703704 0.07142857\]\n \[0.16129032 0.1875    \]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for elementwise division of subarrays for 'a' and 'b'."
        raise check50.Missing("Division subarray",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases16(exists):
    """Program prints correct output for sum of elements in subarrays for 'a' and 'b'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "132"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the sum of elements in subarrays for 'a' and 'b'."
        raise check50.Missing("Element subarray sum",'your output',help=help)
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases21(exists):
    """Program prints correct output for subarray of 'c'"""
    
    actual = check50.run("python3 Question1.py").stdout()
    expected = "\[\[11 21\]\n \[51 61\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the subarray of 'c'."
        raise check50.Missing("Subarray of 'c'",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases22(exists):
    """Program prints correct output for subarray of 'd'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "\[\[227 228\]\n \[231 232\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the subarray of 'd'."
        raise check50.Missing("Subarray of 'd'",'your output',help=help)
      
    
    
@check50.check(exists) # only run this check if the exists check has passed
def check_cases23(exists):
    """Program prints correct output for difference 'c-d'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "\[\[-216 -207\]\n \[-180 -171\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the difference 'c-d'."
        raise check50.Missing("Difference array 'c-d'",'your output',help=help)
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases24(exists):
    """Program prints correct output for elementwise multiplication of subarrays for 'c' and 'd'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "\[\[ 2497  4788\]\n \[11781 14152\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for elementwise multiplication for 'c' and 'd' subarrays."
        raise check50.Missing("Multiplication subarray",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases25(exists):
    """Program prints correct output for elementwise division of subarrays for 'c' and 'd'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "\[\[0.04845815 0.09210526\]\n \[0.22077922 0.26293103\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the elementwise division of subarrays for 'c' and 'd'."
        raise check50.Missing("Division subarray",'your output',help=help)
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases26(exists):
    """Program prints correct output for sum of elements in subarrays for 'c' and 'd'"""
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "1062"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the sum of elements in subarrays for 'c' and 'd'."
        raise check50.Missing("Element subarray sum",'your output',help=help)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3(exists):
    """Program prints correct outputs for other arrays"""
    check50.include("Question2_Sol.py")
    check50.py.append_code("Question2.py", "Question2_Sol.py")
    
    actual = check50.run("python3 Question2.py").stdout()
    expected = "\[\[113 213\]\n \[513 613\]\]"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for general first subarray."
        raise check50.Missing("General first subarray",'your output',help=help)
        
    actual00 = check50.run("python3 Question2.py").stdout()
    expected00 = "\[\[2272 2282\]\n \[2312 2322\]\]"
    
    if not re.search(expected00, actual00):
        help = r"Your code does not print the correct result for general second subarray."
        raise check50.Missing("General second subarray",'your output',help=help)

    actual0 = check50.run("python3 Question2.py").stdout()
    expected0 = "\[\[-2159 -2069\]\n \[-1799 -1709\]\]"
    
    if not re.search(expected0, actual0):
        help = r"Your code does not print the correct result for the general difference of subarrays."
        raise check50.Missing("General difference of subarrays",'your output',help=help)
        
        
    actual2 = check50.run("python3 Question2.py").stdout()
    expected2 = "\[\[ 256736  486066\]\n \[1186056 1423386\]\]"
    
    if not re.search(expected2, actual2):
        help = r"Your code does not print the correct result for elementwise multiplication for general subarrays."
        raise check50.Missing("General multiplication subarray",'your output',help=help)
        
    actua3l = check50.run("python3 Question2.py").stdout()
    expected3 = "\[\[0.04973592 0.09333918\]\n \[0.22188581 0.26399655\]\]"
    
    if not re.search(expected3, actual3):
        help = r"Your code does not print the correct result for the elementwise division of general subarrays."
        raise check50.Missing("General division subarray",'your output',help=help)
        
    actual4 = check50.run("python3 Question2.py").stdout()
    expected4 = "10640"
    
    if not re.search(expected4, actual4):
        help = r"Your code does not print the correct result for the sum of elements in general subarrays."
        raise check50.Missing("General element subarray sum",'your output',help=help)
   

        
  
