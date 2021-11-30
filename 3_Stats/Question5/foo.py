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
    check50.exists("Question5.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases():
    """Program prints the correct percentiles and mode(s) for 'clicks' - Test 1"""
    
    actual = check50.run("python3 Question5.py").stdout()
    expected1 = "152.25"
    expected2 = "208.0"
    expected3 = "260.0"
    expected4 = "283.0"
    expected5 = "\[283\]"
    
    if not re.search(expected1, actual):
        help = r"Your code does not print the correct percentile P_25 for 'clicks'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected2, actual):
        help = r"Your code does not print the correct percentile P_50 for 'clicks'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected3, actual):
        help = r"Your code does not print the correct percentile P_75 for 'clicks'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected4, actual):
        help = r"Your code does not print the correct percentile P_95 for 'clicks'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected5, actual):
        help = r"Your code does not print the correct mode(s) for 'clicks'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
        
        
    
        
@check50.check(check_cases) # only run this check if the exists check has passed
def check_cases2():
    """Program prints the correct percentiles and mode(s) for 'clicks2' - Test 2"""
    
    actual = check50.run("python3 Question5.py").stdout()
    expected1 = "136.5"
    expected2 = "154.0"
    expected3 = "218.0"
    expected4 = "272.2"
    expected5 = "\[154, 200\]"
    
    if not re.search(expected1, actual):
        help = r"Your code does not print the correct percentile P_25 for 'clicks2'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected2, actual):
        help = r"Your code does not print the correct percentile P_50 for 'clicks2'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected3, actual):
        help = r"Your code does not print the correct percentile P_75 for 'clicks2'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected4, actual):
        help = r"Your code does not print the correct percentile P_95 for 'clicks2'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected5, actual):
        help = r"Your code does not print the correct mode(s) for 'clicks2'."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
        
        
        
        
@check50.check(check_cases2) # only run this check if the exists check has passed
def check_cases3():
    """Program prints the correct percentiles and mode(s) for random data - Test 3"""
    
    check50.include("Question5_Sol.py")
    check50.py.append_code("Question5.py", "Question5_Sol.py")
    
    actual = check50.run("python3 Question5.py").stdout()
    expected1 = "15.75"
    expected2 = "19.0"
    expected3 = "26.1"
    expected4 = "29.349999999999998"
    expected5 = "\[19.0\]"
    
    if not re.search(expected1, actual):
        help = r"Your code does not print the correct percentile P_25 for random data."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected2, actual):
        help = r"Your code does not print the correct percentile P_50 for random data."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected3, actual):
        help = r"Your code does not print the correct percentile P_75 for random data."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected4, actual):
        help = r"Your code does not print the correct percentile P_95 for random data."
        raise check50.Mismatch("Correct output", "your output", help=help)
        
    if not re.search(expected5, actual):
        help = r"Your code does not print the correct mode(s) for random data."
        raise check50.Mismatch("Correct output", "your output", help=help)
