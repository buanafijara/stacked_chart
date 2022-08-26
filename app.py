import matplotlib
import numpy as np
import pandas as pd
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt

df = pd.read_excel('data/finished plan data.xlsx')
df_t = pd.read_excel('data/result of sea trial.xlsx')
connector_color = 'magenta'
lwidth = 5
marker_size = 100

pack = {
    'Te1' : ('m', 0, 'red'),
    'Tc'  : ('m', 0, 'green'),
    'Te2' : ('m', 0, 'dodgerblue'),
    'Ps'  : ('m', 1, 'orange'),
    'Pm'  : ('t', 1, 'darkgreen'),
    'Pc'  : ('t', 1, 'black'),
    'Ne'  : ('m', 2, 'blue'),
    'Nb'  : ('t', 2, 'grey'),
    'Be'  : ('m', 3, 'maroon'),
    'Rc'  : ('t', 3, 'purple')
}