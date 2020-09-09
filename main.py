# a program that receives a list of dictionaries
# whose value is converted to csv format

import functools
import csv

def decorator(func):
    @functools.wraps(func)
    def wrapped():
        result = func()
        for i in range(len(result)):
            colums = list(result[i].keys())
            with open('output.csv', 'a', newline='') as out_file:
                csv_writer = csv.DictWriter(out_file, fieldnames=colums)
                csv_writer.writeheader()
                csv_writer.writerow(result[i])

        return result
    return wrapped()


@decorator
def dec_fun():
    lst = [{1: 'a', 2: 'b'}, {3: 'c', 4: 'd'}, {5: 'e', 6: 'f'}] # example list
    return lst