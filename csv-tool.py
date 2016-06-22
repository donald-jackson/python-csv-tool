import csv

class CSVFile(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def rowCount(self):
        with open(self.file_name, 'rU') as f:
            reader = csv.reader(f, dialect=csv.excel)
            data = list(reader)
            row_count = len(data)
            return row_count

file_name = raw_input("Please enter filename: ")

#No validation that the user entered a file name? Hectic.

user_file = CSVFile(file_name)

print "Row count is: " + str(user_file.rowCount())



