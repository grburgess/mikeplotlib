import matplotlib.pyplot as plt
import numpy as np
from colour import Color
import matplotlib.colors as colors

from mikeplotlib.utils.colorscale import colorscale

def hist(data, color='#3FF1A6', ax=None, **kwargs):
    """
    a custom hist 

    :param data: 
    :param color: 
    :param ax: 
    :returns: 
    :rtype: 

    """

    if ax is None:

        ax = plt.gca()

    if 'lw' in kwargs:

        lw = kwargs.pop('lw')

    else:

        lw = 2
        
    # compute the colors

    color = colors.to_hex(color)
    
    fc = color

    # now compute the edge color

    c_color = Color(color)

    HL_scale = .85
    
    ec = colorscale(c_color.hex, HL_scale)

    artist = ax.hist(data, fc=fc, ec=ec, lw=lw,**kwargs)

    return artist
    
    
    
