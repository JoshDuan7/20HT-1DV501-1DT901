import numpy as np
def Median(lst):
    median_salary = np.median(lst)
    return median_salary

def Average(lst):
    avg_salary = np.mean(lst)
    return avg_salary

def Gap(lst):
    salary_gap = max(lst) - min(lst)
    return salary_gap

while True:
    lst = input("Provide salaries: ")
    salaries = lst.split()
    ints = [int(s) for s in salaries]
    median = Median(ints)
    avg = Average(ints)
    gap = Gap(ints)
    print("Median: ",median)
    print("Average: ",avg)
    print("Gap: ",gap)