# Functions to take CSV file, prepare it, and save it

# Libraries
import numpy as np
import pandas as pd
import os


def columns(pathfile):
    """Counts # of columns in a csv"""
    with open(pathfile, 'r') as f:
        line1 = f.readline()
    row1 = line1.split(';')
    row1 = row1[:-1]
    for n, i in enumerate(row1):
        row1[n] = float(i)
    return len(row1)


def rows(pathfile):
    """Counts # of rows in csv"""
    df = pd.read_csv(pathfile, header=None)
    rows = len(df.index)
    return rows


def CreateArray(path, col, row):
    """Changes csv from string in one column to a correct one"""
    file = np.zeros((row, col))
    with open(path, 'r') as f:
        j = -1
        for line in f.readlines():
            j += 1
            row = line.split(';')
            row = row[:-1]
            for n, i in enumerate(row):
                file[j, n] = float(i)
        df = pd.DataFrame(data=file)
    df.to_csv(path, index=False, header=False)


def correctCSV(path):
    """Applies CreateArray to a folder"""
    i = 0
    for file in os.listdir(path):
        i += 1
        pathfile = path + '\\' + file
        col = columns(pathfile)
        row = rows(pathfile)
        CreateArray(pathfile, col, row)
        print(f"File {file} done")


def Correctdir(pathdir):
    """Applies correctCSV to various folders"""
    for file in os.listdir(pathdir):
        path = pathdir + '\\' + file
        correctCSV(path)
        print(f'File {file} done')


def importCSVfiles(path):
    """Gets all CSV from folder, saves to df and puts in list"""
    df_list = []
    for file in os.listdir(path):
        pathfile = path + '\\' + file
        df = pd.read_csv(pathfile, header=None)
        df_list.append(df)
    return df_list


def importCSVfile(path):
    """Creates one df from csv"""
    df = pd.read_csv(path, header=None)
    return df


def arr2CSV(arr, type):
    path = r".\Desktop\IR_data" + '\\' + type + 'transition.csv'
    np.savetxt(path, arr)
