import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question1.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases():
    """Program prints correct name length - Test 1"""
    check50.run("python3 Question1.py").stdin("XXXXX").stdin("XXXXX").stdout("The length of your name is:  10").exit()
    
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2():
    """Program prints correct name length - Test 2"""
    check50.run("python3 Question1.py").stdin("XXXXXXXXXX").stdin("XXXXX").stdout("The length of your name is:  15").exit()
    
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3():
    """Program prints correct name length - Test 3"""
    check50.run("python3 Question1.py").stdin("XXXXXXXXXX").stdin("XXXXXXXXXX").stdout("The length of your name is:  20").exit()
