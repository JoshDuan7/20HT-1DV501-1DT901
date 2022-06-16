def Median(lst):
    #if total salary numbers are odd
    if len(lst) % 2 != 0:
        median_index = round((len(lst) - 1)/2)
        median = lst[median_index]
        return median
    else:
        # the lower salary of the two-middle salaries
        index_1 = len(lst) // 2 - 1
        # the upper salary of the two-middle salaries
        index_2 = index_1 + 1
        median = round((lst[index_1] + lst[index_2])/2)
        return median


def Average(lst):
    sum = 0
    count = 0
    for i in lst:
        sum += i
        count += 1
    avg = round(sum / count)
    return avg


def Gap(lst):
    salary_gap = max(lst) - min(lst)
    return salary_gap

# main
salaries = input("Provide salaries: ")
salaries_string = salaries.split()
salaries_ints = [int(s) for s in salaries_string]
# first time made mistake when assign'salaries_ints.sort()'to 'salaries_int'
salaries_ints.sort() 
median = Median(salaries_ints)
avg = Average(salaries_ints)
gap = Gap(salaries_ints)
print("Median: ",median)
print("Average: ",avg)
print("Gap: ",gap)