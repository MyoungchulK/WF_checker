import os
import numpy as np
from matplotlib import pyplot as plt
from tools.antenna import antenna_info

Antenna = antenna_info()[0]

color16=['firebrick','saddlebrown', 'deeppink','tomato', 'lightsalmon','greenyellow','forestgreen'
         ,'olive','cyan','steelblue','dodgerblue','navy' ,'purple','lightslategray','gray','black']

def plot_16_indi(xlabel,ylabel,title
            ,x_data,y_data
            ,d_path,file_name
            ,message
            ,xmin = None, xmax = None
            ,ymin = None, ymax = None
            ,y_scale = None
            ,vpeak = None
            ,absol = None):

    fig = plt.figure(figsize=(24, 18)) # figure size

    ax = fig.add_subplot(111) # want to have a one big XY label for all 16 plots
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
    ax.set_xlabel(xlabel, labelpad=30,fontsize=40)
    ax.set_ylabel(ylabel,labelpad=50, fontsize=40)

    plt.title(title, y=1.04,fontsize=35)

    for b in range(16):

        ax = fig.add_subplot(4,4,b+1)
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=20)
        #ax.set_xlim(-200,800)
        if xmin is not None and xmax is not None:
            ax.set_xlim(xmin,xmax)
        if ymin is not None and ymax is not None:
            ax.set_ylim(ymin,ymax)
        if y_scale is not None:
            ax.set_yscale('log')    
        #ax.set_ylim(-0.8,0.8)
        ax.grid(linestyle=':')
        ax.set_title(Antenna[b],fontsize=25)

        if absol is not None:
            y_dat = np.abs(y_data[b])
        else:
            y_dat = y_data[b]

        if vpeak is not None:
            ax.plot(x_data[b],y_dat,'-',lw=2,color='red',alpha=0.7,label='Vpeak:'+str(np.round(np.nanmax(np.abs(y_data[b])),2)))
            plt.legend(loc='best',numpoints = 1 ,fontsize=15)
        else: 
            ax.plot(x_data[b],y_dat,'-',lw=2,color='red',alpha=0.7)

    plt.tight_layout()

    # saving png into output path
    os.chdir(d_path)
    fig.savefig(file_name,bbox_inches='tight')
    #plt.show()
    plt.close()

    print(message)
