import openpyxl
import numpy as np
import matplotlib.pyplot as plt
from configparser import ConfigParser
import os

## import custom function
import func
import func_io

xlsx_data=func_io.Readxlsx('data.xlsx')
data=func_io.Getdata(xlsx_data,type='xy')

func.New_fig(fig_size=(7,7))

for i in range(len(data)):
    print(i)
    func.Plot(data[i][0],data[i][1],label=data[i][2],linenumber=i)
func.Legend()
plt.show()