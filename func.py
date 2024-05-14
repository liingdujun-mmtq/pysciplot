import numpy as np
import matplotlib.pyplot as plt

## import custom func
import func_io

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


def Plot(x,y,label="",linenumber=0):
    setting=func_io.Read_config("preset/plot.conf","plot")
    setting_plot=func_io.preset_plot_plot(setting,num=linenumber)
    plt.plot(x,y,linestyle=setting_plot.linestyle,color=setting_plot.color,linewidth=setting_plot.linewidth,marker=setting_plot.marker,markersize=setting_plot.markersize,label=label)

    setting=func_io.Read_config("config.conf","main")
    setting_main=func_io.configure(setting)
    plt.xlabel(setting_main.xlabel,fontsize=setting_plot.label_fontsize)
    plt.ylabel(setting_main.ylabel,fontsize=setting_plot.label_fontsize)

def Legend():
    setting=func_io.Read_config("preset/plot.conf","legend")
    setting_legend=func_io.preset_legend(setting)
    plt.legend(loc=setting_legend.legend_location,fontsize=setting_legend.fontsize,edgecolor=setting_legend.edgecolor)
    