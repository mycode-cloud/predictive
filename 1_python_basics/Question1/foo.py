import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Question1.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def prints_hello():
    """Program prints "Hello, world!" """
    check50.run("python3 Question1.py").stdout("Hello, world!", regex=True).exit(0)
