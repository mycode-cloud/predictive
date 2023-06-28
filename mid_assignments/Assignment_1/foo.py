import check50
import statistics
import os
import re
import numpy as np


# Look up the values other than the mode in the student' answer and provide feedback. used in check50.Mismatch
def find_values(text, dic):
    
    missing_values = []
    for key, value in dic.items():
        pattern = fr"{value}"
        match = re.search(pattern, text)
        if not match:
            missing_values.append(f"{key}: {value}")

    if len(missing_values) == 0:
        help = "All statistics except the mode is correct. Check your find_mode() function."
    else:
        missing_info = "\n ".join(missing_values)
        help = f"Mismatch. Check your stats(l) function. Missing value(s):\n {missing_info}"
    
    return(len(missing_values),help)

        
@check50.check()
def file_exists_check():
    """Check if the 'Assignment_1.py' file exists"""
    if not os.path.isfile("Assignment_1.py"):
        raise check50.Failure("The 'Assignment_1.py' file does not exist")
 
@check50.check(file_exists_check)
def stats_check1():
    """Check the output of the stats(l) function"""
    
    # Define a sample list to test the stats(l) function
    sample_list = '1.2, 2.0, 3.4, 4.1, 5.0'

    actual = check50.run("python3 Assignment_1.py").stdin(sample_list).stdout()
    # Retrieve the expected values using the statistics module
    sample_list = [1.2, 2.0, 3.4, 4.1, 5.0]
    ex_mean = statistics.mean(sample_list)
    ex_median = statistics.median(sample_list)
    ex_mode = 'nan'
    ex_stdv = statistics.stdev(sample_list)
    ex_range = max(sample_list) - min(sample_list)
    
    expected = fr"Mean:\s*{ex_mean}\s*\nMedian:\s*{ex_median}\s*\nMode:\s*{ex_mode}\s*\nStandard deviation:\s*{ex_stdv}\s*\nRange:\s*{ex_range}"
    #display version of expected to show when error raised 

    expected_dis = f"Mean: {ex_mean}\nMedian: {ex_median}\nMode: {ex_mode}\nStandard deviation: {ex_stdv}\nRange: {ex_range}"
    
    # Compare the expected values with the stats(l) output
    if not re.search(expected, actual, re.IGNORECASE):
       
        missing_v, help = find_values(actual, {'Mean':ex_mean, 'Median': ex_median, 'Mode': ex_mode, 'Standard deviation':ex_stdv, 'Range':ex_range})
        if missing_v == 2:
            raise check50.Missing(ex_mode, actual, help=help)
        else:
            raise check50.Mismatch(expected_dis, actual, help=help)
        #raise check50.Failure("The stats(l) function does not produce the correct output")
        
@check50.check(file_exists_check)
def stats_check2():
    """Check the output of the stats(l) function"""
    
    # Define a sample list to test the stats(l) function
    sample_list = '2.1, 2.1, 3.0, 4.0, 5.0, 5.0, 5.0, 9.1'

    actual = check50.run("python3 Assignment_1.py").stdin(sample_list).stdout()
    # Retrieve the expected values using the statistics module
    sample_list = [2.1, 2.1, 3.0, 4.0, 5.0, 5.0, 5.0, 9.1]
    ex_mean = statistics.mean(sample_list)
    ex_median = statistics.median(sample_list)
    ex_mode = float(5.0)
    ex_stdv = statistics.stdev(sample_list)
    ex_range = max(sample_list) - min(sample_list)
    
    expected = fr"Mean:\s*{ex_mean}\s*\nMedian:\s*{ex_median}\s*\nMode:\s*{ex_mode}\s*\nStandard deviation:\s*{ex_stdv}\s*\nRange:\s*{ex_range}"    
    #display version of expected to show when error raised
    
    expected_dis = f"Mean: {ex_mean}\nMedian: {ex_median}\nMode: {ex_mode}\nStandard deviation: {ex_stdv}\nRange: {ex_range}"
    
    # Compare the expected values with the stats(l) output
    if not re.search(expected, actual, re.IGNORECASE):
       
        missing_v, help = find_values(actual, {'Mean':ex_mean, 'Median': ex_median, 'Mode': ex_mode, 'Standard deviation':ex_stdv, 'Range':ex_range})
        if missing_v == 2:
            raise check50.Missing(ex_mode, actual, help=help)
        else:
            raise check50.Mismatch(expected_dis, actual, help=help)
