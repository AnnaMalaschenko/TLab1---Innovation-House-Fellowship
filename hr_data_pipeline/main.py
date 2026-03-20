import statistics

def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned_list = []
    removed_values = 0
# Corrected via Claude's help - changed cleaned_list = data.append(int()) to - > append the cleaned_list itself, and inserted 'value' inside int():
    for value in data:
        if value != "NO DATA" and value != "":
                cleaned_list.append(int(value))
        else:
            removed_values += 1
    print('Number of Removed Values: ' + str(removed_values))
    return cleaned_list

def average(cleaned_list: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    sum_of_values = 0
    for value in cleaned_list:
        sum_of_values = sum_of_values + value

    average = round(sum_of_values/len(cleaned_list), 2)
    return average

# This is my first attempt at median, which froze my computer:
#def median(cleaned_list: list) -> float:
#    print('Median of the cleaned list:')
#    print(round(median(cleaned_list)), 2)

# I asked Claude for the median function i can use, and it recommended to use 'statistics.median':

def median(cleaned_list: list) -> float:
    """
    """
    return round(statistics.median(cleaned_list), 2)


def range(cleaned_list: list) -> float:
    """
    """
    range = max(cleaned_list) - min(cleaned_list)
    return range


def rolling_avg(cleaned_list: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """

    data = []
    # open file using file I/O and read it into the `data` list
    f = open(file)
    lines = f.readlines()

    for line in lines:
     data.append(line.strip())
    

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    
    cleaned_list = clean_heartrate_data(data)


    # calculate the average, median, and range of this file using the functions you've wrote
    average(cleaned_list)
    median(cleaned_list)
    range(cleaned_list)

    # print out your data quality measure to the console
    print("Cleaned data list:")
    print(cleaned_list)

    # print out your descriptive statistics to the console
  
    print("Average: " + str(average(cleaned_list)))
    print("Median: " + str(median(cleaned_list)))
    print("Range: " + str(range(cleaned_list)))


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
