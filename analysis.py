# Functions to take df, combine them, analyze them and show them

# Libraries
import numpy as np
import pandas as pd
import os
from PIL import Image
import matplotlib.pyplot as plt
import importCSV
from matplotlib.widgets import Slider, Button
from matplotlib.transforms import Bbox


def combine_frames(df_combined):
    """All df in a list are combined in one by average"""
    average_df = sum(df_combined) / len(df_combined)
    return average_df


def normalize_values(df1, factor=256):
    """Changes the ranges so it is visible according to encoding"""
    df1_normalized = (df1 - df1.min()) / (df1.max() - df1.min()) * 256
    return df1_normalized


def showImage(df, aoa, twoDorthreeD):
    """Displays image from df"""
    image = Image.fromarray(df.to_numpy())
    plt.imshow(image)
    plt.axis('off')
    plt.title('IR image of ' + str(twoDorthreeD) + ' wing at aoa = ' + str(aoa) + ' [deg]')
    plt.show()


def saveImage(df, aoa, twoDorthreeD, path):
    """Creates image from numpy array and saves to a location"""
    image = Image.fromarray(df.to_numpy())
    plt.imshow(image)
    plt.axis('off')
    plt.title('IR image of ' + str(twoDorthreeD) + ' wing at aoa = ' + str(aoa) + ' [deg]')
    plt.savefig(path)


def AnalysisAoA(pathdir):
    """Combines CSV from same AoA and normalizes it"""
    df_list = importCSV.importCSVfiles(pathdir)
    df_ave = combine_frames(df_list)
    df_norm = normalize_values(df_ave)
    return df_norm


def AnalyseAoAImage(pathdir):
    """Combines CSV, converts to image and saves"""
    name = pathdir.split("\\")
    AoA = name[6]
    if name[5] == "2d_ir":
        d = '2D'
    else:
        d = '3D'
    df = AnalysisAoA(pathdir)
    saveloc = r"C:\Users\ricke\Desktop\IR_data\3d_Images" + '\\AoA_' + AoA + '.png'
    saveImage(df, AoA, d, saveloc)


def IterateImages(dir):
    """Analyses all AoA"""
    i = 0
    for file in os.listdir(dir):
        i += 1
        path = dir + '\\' + file
        AnalyseAoAImage(path)
        print(f'Image {i} done')


def TransitionLine(path, list_):
    """Analysis of image to select transition line"""
    name = path.split('\\')
    type = name[5].strip('_csv')
    aoa = name[6].strip('.csv')
    # Dataframe
    df = pd.read_csv(path, header=None)
    # Crop Dataframe
    df = df.iloc[:, 165:445]
    # Create image
    image = Image.fromarray(df.to_numpy())

    # Create Plot
    fig, ax = plt.subplots()
    ax.set_yticks([])
    plt.subplots_adjust(bottom=0.3)
    plt.title(type + " AoA " + aoa + "°")

    # Create line
    x_ = 50
    p = plt.axvline(x=x_)
    plt.imshow(image, extent=(0, 100, 0, 175))

    def valUpdate(val):
        """Effect of changing slider value"""
        p.set_xdata(slider.val)

    # Create slider
    axSlider = plt.axes([0.15, 0.15, 0.75, 0.05])
    slider = Slider(ax=axSlider, label='Line', valmin=0, valmax=100, valinit=50)
    slider.on_changed(valUpdate)

    # Create button
    axButton = plt.axes([0.81, 0.05, 0.1, 0.075])
    button_next = Button(axButton, 'Next')

    def buttonclick(val):
        """Effect of clicking button"""
        savepath = r"C:\Users\ricke\Desktop\IR_data\\" + type + "_line\\" + aoa + '.png'
        plt.savefig(savepath, pad_inches=0, bbox_inches=Bbox([[2.25, 1], [4.25, 4.5]]))
        plt.close()

    button_next.on_clicked(buttonclick)
    plt.show()

    # Updates list to include aoa, hystersis and transition line
    aoanumber = aoa
    h = False
    if aoa[-2:] == "_2":
        aoanumber = aoa.split('_')
        aoanumber = aoanumber[0]
        h = True
    if aoa[-1:] == "h":
        aoanumber = aoanumber.split()
        aoanumber = aoanumber[0]
        h = True
    aoanumber = float(aoanumber)
    list_.append([h, aoanumber, slider.val])
