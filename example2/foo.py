import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """file exists""" # this is what you will see when running check50
    check50.exists("hello2.py") # the actual check

@check50.check(exists) # only run this check if the exists check has passed
def prints_hello2():
    """Does the program print "Hello, world2\\n"? """
    import re
 
    expected = "Hello, world2\n"
    actual = check50.run("python3 hello2.py").stdout()
    if not re.match(expected, actual,re.DOTALL):
        help = None
        if re.match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("Hello, world2\n", actual, help=help)
    if re.match(expected,actual,re.DOTALL):
        print(True)
