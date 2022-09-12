import csv
from os.path import exists

def writing_data_csv(filename, data_to_write):
    """
    Function to write data to csv file
    Parameters: filename (string) - the name of the file to be read
                data_to_write (string) - the data to be written (or appended) to the file
    """
    file_exists = exists(filename)
    if file_exists is False:
        header = ['name', 'link']
        with open(filename, 'w+', newline="", encoding='utf-8') as writing_file:
            csvwriter1 = csv.writer(writing_file) # 1. create a csvwriter object
            csvwriter1.writerow(header) # 2. write the header
            csvwriter1.writerow(data_to_write) # 3. write the rest of the data
            writing_file.close() # 4. close the file
    else:
        with open(filename, 'a', newline="", encoding='utf-8') as appending_file:
            csvwriter2 = csv.writer(appending_file) # 1. create a csvwriter object
            csvwriter2.writerow(data_to_write) # 2. write the row, without the header
            appending_file.close() # 3. close the file

def reading_data_csv(filename):
    """
    Reads the data from the csv file and returns a header and a list of rows (both as lists)
    Parameters: filename (string) - the name of the file to be read
    """
    with open(filename, 'r+', encoding='utf-8') as read_file:
        content = read_file.readlines()
    read_header = content[:1]
    read_rows = content[1:]
    read_file.close()
    if read_rows != []:
        read_header[-1] = read_header[-1].strip()
        for i in range(len(read_rows)):
            read_rows[i] = read_rows[i].strip()
        return read_header, read_rows
    else:
        return read_header, read_rows
