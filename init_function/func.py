import numpy as np
import matplotlib.pyplot as plt

def New_fig(config="",
        fig_size=(7,7),
        fig_dpi=120,
        xtick_direction="in",
        ytick_direction="in",
        tick_fontsize=16,
):
    plt.figure(figsize=fig_size,dpi=fig_dpi)
    plt.rcParams['xtick.direction']=xtick_direction
    plt.rcParams['ytick.direction']=ytick_direction
    plt.xticks(fontsize=tick_fontsize)
    plt.yticks(fontsize=tick_fontsize)


def Plot(x,y,label="",
         linestyle="-",
         color="k",
         linewidth=1,
         marker="o",
         markersize=7,
         xlabel="x",
         ylabel="y",
         label_fontsize=18
         ):
    plt.plot(x,y,linestyle="-",color="k",linewidth=1,marker="o",markersize=7,label=label)
    plt.xlabel(xlabel,fontsize=label_fontsize)
    plt.ylabel(ylabel,fontsize=label_fontsize)

def Legend(legend_location='best',
           fontsize=16,
           edgecolor="k"
           ):
    plt.legend(loc=legend_location,fontsize=fontsize,edgecolor=edgecolor)
    