import matplotlib.pyplot as plt
import numpy as np



def hist(data, color='r', ax=None, **kwargs):

    if ax is None:

        ax = plt.gca()

    # compute the colors

    fc = color
    ec = None

    artist = ax.hist(data, fc=fc, ec=ec, histtype='step', **kwargs)

    return artist
    
    
    
