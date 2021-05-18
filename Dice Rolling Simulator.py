"""
As the name of the program suggests, we will be imitating a rolling dice. This is one of the interesting python projects and will generate a random number each dice the program runs, 
and the users can use the dice repeatedly for as long as he wants. When the user rolls the dice, the program will generate a random number between 1 and 6 
dice simulator is a simple computer model that can roll a dice for us."""

# Tkinter is the most common, fast, and easy to use Python package used to build Graphical User Interface applications.
# Image, Imagetk: Imported from PIL, i.e. Python Imaging Library. We use it to perform operations involving images in our UI.
# Random: Imported to generate random numbers.
# import the required modules

import tkinter
from PIL import Image, ImageTk
import random

# top-level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the dice')

