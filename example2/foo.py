import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """file exists""" # this is what you will see when running check50
    check50.exists("hello2.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def prints_hello2():
    """program prints "Hello, world2\n"? """
    check50.run("python3 hello2.py").stdout("[Hh]ello, [Ww]orld2\n", regex=True).exit(0)
