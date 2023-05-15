import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_4.py") # the actual check

        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1(exists):
    """Program prints correct output 1"""
    
    check50.include("Canada_YouTube_Videos.csv")
    assert os.path.exists("Canada_YouTube_Videos.csv")
    
    
    actual = check50.run("python3 Assignment_4.py").stdout()
    expected = "The shape of the DataFrame is: (5000, 16)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the original DataFrame."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2(exists):
    """Program prints correct output 2"""
    
    check50.include("Canada_YouTube_Videos.csv")
    assert os.path.exists("Canada_YouTube_Videos.csv")
    
    actual = check50.run("python3 Assignment_4.py").stdout()
    expected = "Index(['video_id', 'trending_date', 'title', 'channel_title', 'category_id', 'publish_time',\n       'tags', 'views', 'likes', 'dislikes', 'comment_count', 'thumbnail_link', 'description'],\n      dtype='object')"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the updated list of columns after using the drop method."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3(exists):
    """Program prints correct output 3"""
    
    check50.include("Canada_YouTube_Videos.csv")
    assert os.path.exists("Canada_YouTube_Videos.csv")
    
    actual = check50.run("python3 Assignment_4.py").stdout()
    expected = "The number of videos with no missing information that have more than one million views and likes is: 28"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the super_vidoes DataFrame."
        raise check50.Missing("Correct results",'your output',help=help)
