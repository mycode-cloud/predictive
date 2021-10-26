import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question2.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def check_cases(exists):
    """Program prints correct name length """
    check50.run("python3 Question1.py").stdin("[1, 2, 3, 4, 5]").stdin("[6, 7, 8, 9, 10]").stdout("55").exit()
    check50.run("python3 Question1.py").stdin("[1, 2, 3, 4, 5]").stdin("[6, 7, 8, 9, 10, 11]").stdout("66").exit()
    check50.run("python3 Question1.py").stdin("[1, 2, 3, 4, 5]").stdin("[6, 7, 8, 9, 10, 11, 12]").stdout("78").exit()
