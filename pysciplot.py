import openpyxl
import numpy as np
import matplotlib.pyplot as plt
from configparser import ConfigParser

## import custom function
import init_function.func as fun
import init_function.io as io

x=np.arange(0,10,0.5)
y=x**2

fun.New_fig(fig_size=(7,7))
fun.Plot(x,y,label="func of y")
fun.Legend()
plt.show()