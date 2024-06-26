import check50
import check50.py
import os
import re

@check50.check()
def file_exists_check():
    """Check if the 'Assignment_1.py' file exists"""
    if not os.path.isfile("Assignment_1.py"):
        raise check50.Failure("The 'Assignment_1.py' file does not exist")
 
@check50.check(file_exists_check)
def read_text_check1():
    """Check the output of the read_text() function (line 4) for sample.txt""" # file provided to students
    
    check50.include("sample.txt")
    assert os.path.exists("sample.txt")

    actual = check50.run("python3 Assignment_1.py").stdin('sample.txt').stdout()
    expected = r"- Revenue: \$1,234,567" #"- Expenses: \$4,123,456"
        
    if not re.search(expected, actual):
        help = "read_text() function does not produce the correct output"
        #raise check50.Mismatch(expected, actual, help=help)
        raise check50.Failure("read_text() function does not produce the correct output")

@check50.check(file_exists_check)
def read_text_check2():
    """Check the output of the read_text() function (line 4) for sampletext2.txt""" # file NOT provided to students
    
    check50.include("sampletext2.txt")
    assert os.path.exists("sampletext2.txt")

    actual = check50.run("python3 Assignment_1.py").stdin('sampletext2.txt').stdout()
    expected = r"- Net Profit: \$1,555,445"
        
    if not re.search(expected, actual):
        help = "read_text() function does not produce the correct output"
        #raise check50.Mismatch(expected, actual, help=help)
        raise check50.Failure("read_text() function does not produce the correct output")        
        
@check50.check(file_exists_check)
def extract_values_check1():
    """Check the output of the extract_values() function for Expenses of Location1 for sample.txt""" # file provided to students
    
    check50.include("sample.txt")
    assert os.path.exists("sample.txt")

    actual = check50.run("python3 Assignment_1.py").stdin('sample.txt').stdout()
    expected = "987654.0"
        
    if not re.search(expected, actual):
        if re.search(r"\$987,654", actual): # if the correct value with $ and comma exists, it means make_value_float() does not work properly or not applied
            help = "Expected a float value for Expenses. make_value_float() function does not produce the correct output"
            raise check50.Mismatch(expected, actual, help=help)
        raise check50.Failure("extract_values() function does not produce the correct output")
        
        
@check50.check(file_exists_check)
def extract_values_check2():
    """Check the output of the extract_values() function for Location2 for sample.txt""" # file provided to students
    
    check50.include("sample.txt")
    assert os.path.exists("sample.txt")

    actual = check50.run("python3 Assignment_1.py").stdin('sample.txt').stdout()
    expected = "{'Revenue': 2345678.0, 'Expenses': 1876543.0, 'Net Profit': 469135.0, 'Units Sold': 15000.0, 'Average Unit Price': 156.42, 'Equity': 2222212.0}"
        
    if not re.search(expected, actual):
        #help = "extract_values() function does not produce the correct output"
        #raise check50.Mismatch(expected, actual, help=help)
        help = "Make sure the financials for Location2 are in a dictionary and all values are float"
        raise check50.Failure("extract_values() function does not produce the correct output", help = help)
        
@check50.check(file_exists_check)
def extract_values_check3():
    """Check the output of the extract_values() function for Expenses of Location1 for sampletext2.txt""" # file NOT provided to students
    
    check50.include("sampletext2.txt")
    assert os.path.exists("sampletext2.txt")

    actual = check50.run("python3 Assignment_1.py").stdin('sampletext2.txt').stdout()
    expected = "4123456.0"
        
    if not re.search(expected, actual):
        if re.search(r"\$4,123,456", actual): # if the correct value with $ and comma exists, it means make_value_float() does not work properly or not applied
            help = "Expected a float value for Expenses. make_value_float() function does not produce the correct output"
            raise check50.Mismatch(expected, actual, help=help)
        raise check50.Failure("extract_values() function does not produce the correct output")
        
        
@check50.check(file_exists_check)
def extract_values_check4(): 
    """Check the output of the extract_values() function for Location2 for sampletext2.txt""" # file NOT provided to students
    
    check50.include("sampletext2.txt")
    assert os.path.exists("sampletext2.txt")

    actual = check50.run("python3 Assignment_1.py").stdin('sampletext2.txt').stdout()
    expected = "{'Revenue': 6789012.0, 'Expenses': 5012345.0, 'Net Profit': 1776667.0, 'Units Sold': 18000.0, 'Average Unit Price': 398.33, 'Equity': 2469107.0}"
        
    if not re.search(expected, actual):
        #help = "extract_values() function does not produce the correct output"
        #raise check50.Mismatch(expected, actual, help=help)
        help = "Make sure the financials for Location2 are in a dictionary and all values are float"
        raise check50.Failure("extract_values() function does not produce the correct output", help = help)

@check50.check(file_exists_check)
def make_value_float_check():
    '''Checks the out put of make_value_float() function for extra_check.py'''

    check50.include("sample.txt")
    assert os.path.exists("sample.txt")
    check50.include("extra_checks.py")
    
    check50.py.append_code("Assignment_1.py", "extra_checks.py")
    actual = check50.run("python3 Assignment_1.py").stdin('sample.txt').stdout()
    expected = "1234008.23"

    if not re.search(expected, actual):
        help = "make_value_float() function does not produce the correct output"
        raise check50.Mismatch(expected, actual, help=help)
        #raise check50.Failure("make_value_float() function does not produce the correct output")
