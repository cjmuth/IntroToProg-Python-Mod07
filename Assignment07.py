# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# CMuth,11/25/2022,Created script
# ---------------------------------------------------------------------------- #

from os.path import exists
import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
pickle_file_str = 'ToDoFile.pickle'
text_file_str = 'ToDoFile.txt'
file_exists_bln = None
table_list = []
choice_str = ''


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        if exists(file_name):
            list_of_rows.clear()  # clear current data
            file = open(file_name, "r")
            for line in file:
                task, priority = line.split(",")
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)
            file.close()
            return list_of_rows


    @staticmethod
    def pickle_file(file_name, list_of_rows):
        ''' Saves data in memory to a pickle file

        :param file_name:
        :param list_of_rows:
        '''
        try:
            pickle_file = open(file_name, 'wb')
            pickle.dump(list_of_rows, pickle_file)
            pickle_file.close()
            print('Pickling complete.')
        except:
            print('Pickling failed.')


    @staticmethod
    def unpickle_file(file_name):
        ''' Looks for a pickle file and loads data if present

        :param file_name:
        :return: list_of_rows, file_exists
        '''
        list_of_rows = []
        try:
            unpickle_file = open(file_name, 'rb')
            list_of_rows = pickle.load(unpickle_file)
            unpickle_file.close()
            file_exists = True
        except:
            print(('\nFile {} was not found.\n').format(file_name))
            file_exists = False
        return list_of_rows, file_exists


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def display_current_data(list_of_rows):
        print('\n********************************************')
        for row in list_of_rows:
            print(('{}  ({})').format(row['Task'],row['Priority']))
        print('********************************************\n')


# Main Body of Script  ------------------------------------------------------ #

table_list, file_exists_bln = Processor.unpickle_file(file_name=pickle_file_str)

if file_exists_bln:
    print(('\nDisplaying data from {}').format(pickle_file_str))
else:
    choice_str = input(('Do you want to load data from {} instead? (Y/N) ').format(text_file_str))
    if choice_str.lower() == 'y':
        print(('Reading data from {}').format(text_file_str))
        table_list = Processor.read_data_from_file(file_name=text_file_str, list_of_rows=table_list)
        print(('Displaying data from {}').format(text_file_str))
    else:
        exit()

IO.display_current_data(list_of_rows=table_list)

choice_str = input('Do you want to pickle this data? (Y/N) ')
if choice_str.lower() == 'y':
    Processor.pickle_file(file_name=pickle_file_str, list_of_rows=table_list)
else:
    print('Data was not pickled.')
    exit()