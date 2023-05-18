import check50 # import the check50 module
import check50.py
import re
import os

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """File exists""" # this is what you will see when running check50
    check50.exists("Assignment_5.py") # the actual check

        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases1(exists):
    """Program prints correct output 1"""
    
    check50.include("CanadaYouTubeVideos.csv")
    assert os.path.exists("CanadaYouTubeVideos.csv")
    
    actual = check50.run("python3 Assignment_5.py").stdout()
    expected = "1           23  2017-11-13T17:00:00.000Z  plush|\"bad unboxing\"|\"unboxing\"|\"fan mail\"|\"id...\""
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the first 10 rows of the 'df' DataFrame using the '.head' method."
        raise check50.Missing("Correct results",'your output',help=help)
        
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases2(exists):
    """Program prints correct output 2"""
    
    check50.include("CanadaYouTubeVideos.csv")
    assert os.path.exists("CanadaYouTubeVideos.csv")
    
    actual = check50.run("python3 Assignment_5.py").stdout()
    expected = r"Sheldon is roasting pastor of the church\\nyoun\.\.\.\s*\nFalse"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the outcome of the '.is_unique' method applied 'df['video_id']."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases3(exists):
    """Program prints correct output 3"""
    
    check50.include("CanadaYouTubeVideos.csv")
    assert os.path.exists("CanadaYouTubeVideos.csv")
    
    actual = check50.run("python3 Assignment_5.py").stdout()
    expected = "After removing the rows that contain duplicate video_id entries, the shape of the current DataFrame is: \(2794, 16\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the DataFrame after removing the rows that contain duplicate video_id entries."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases4(exists):
    """Program prints correct output 4"""
    
    check50.include("CanadaYouTubeVideos.csv")
    assert os.path.exists("CanadaYouTubeVideos.csv")
    
    actual = check50.run("python3 Assignment_5.py").stdout()
    expected = "After removing the rows that contain missing entries, the shape of the current DataFrame is: \(2657, 16\)"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the shape of the DataFrame after removing the rows that contain missing entries."
        raise check50.Missing("Correct results",'your output',help=help)
        
@check50.check(exists) # only run this check if the exists check has passed
def check_cases5(exists):
    """Program prints correct output 5"""
    
    check50.include("CanadaYouTubeVideos.csv")
    assert os.path.exists("CanadaYouTubeVideos.csv")
    
    actual = check50.run("python3 Assignment_5.py").stdout()
    expected = "The number of YouTube videos that contain the case-independent string 'amazon' in the 'tags' column is: 24"
    
    if not re.search(expected, actual):
        help = r"Your code does not print the correct result for the number of YouTube videos that contain the case-independent string 'amazon' in the 'tags' column."
        raise check50.Missing("Correct results",'your output',help=help)
        
