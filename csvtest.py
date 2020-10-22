import csv

def csv_reader(file_obj):
    """ read a csv file """
    reader = csv.reader(file_obj)
    for row in reader:
        print (" ".join(row))
if __name__== "__main__":
    csv+path = "TB_data_dictionary_2014-02-26.csv"
    with open(csv_path, "r")as f_obj:
        csv_reader(f_obj)
