import numpy as np
import pandas as pd
import pickle

file_name = "test.csv"

'''
    numpy as various ways to read files such as loadtxt. It returns a numppy array. You customize how the information
    is parsed such choosing a delimiter, number of rows to skip, which columns to keep, and which data type to
    convert the data into. This function is limited to data sets of the same time.
'''

data_set = np.loadtxt(file_name, delimiter=',')
data_set1 = np.loadtxt(file_name, delimiter=',', skiprows=1, usecols=[0, 2])
data_set2 = np.loadtxt(file_name, delimiter=',', skiprows=1, usecols=[0, 2], dtype=float)

'''
    genfromtxt is another method you can use to parse files. This function can work with
    multiple data types, if the dtype option is set to None. Furthermore, you use names=True to give
'''

data_set3 = np.genfromtxt(file_name, delimiter=',',names=True, dtype=None)

#columns can be see like
print(data_set3.dtype.names)

'''
    another function similar to genfromtext, but specifically for csv files is recfromcsv. dtype is set to None
    by default
'''

data_set4 = np.recfromcsv(file_name, delimiter=',', names=True)

'''
    The above will only return the data as a numpy array. There are other methods to return the data as a dataframe.
    The methods are read_csv() and read_table(). This uses pandas.

    read_csv() has varies option such as nrows and header. nrows is the number of rows that method will read. And,
    header is None means no header. There are other options: sep(choose deliminator), comment(choose a character and
    characters after that character are considered to be comments), na_values(take a string to be understood as a
    na value).

    A dataframe can be coverted to a pandas array like so
'''

data_set5 = pd.read_csv(file_name, nrows=5, header=None)
data_set6 = pd.read_csv(file_name, sep='\t', na_values='Nothing', comment='#')
data_array = data_set5.values

'''
    pandas also has methods to read excel files. One can also access sheets names. One can turn a sheet in a dataframe
    by using the sheetname or index value using the parse method. In addition, you can skiprows, select certain columns
    , and rename columns. Values are given as lists.
'''

data_set7 = pd.read_excel(file_name)
print(data_set7.sheet_names)
print(data_set7.parse("text").head())
print(data_set7.parse(0).head())
print(data_set7.parse(1, skiprows=[1], parse_cols=[0], names=['Country']))

'''
    Pickle is a module that allow python to serialize information ie transfer the object in bytestream. I've heard that
    unpickeling a picket object can allow for arbitrary code execution which is very unsafe. Never unpickle something
    from an untrusted data source.
'''
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)
