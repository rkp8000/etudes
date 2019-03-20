from copy import deepcopy
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")


def set_font_size(ax, font_size, legend_font_size=None):
    """Set font_size of all axis text objects to specified value."""

    texts = [ax.title, ax.xaxis.label, ax.yaxis.label] + \
        ax.get_xticklabels() + ax.get_yticklabels()

    for text in texts:
        text.set_fontsize(font_size)

    if ax.get_legend():
        if not legend_font_size:
            legend_font_size = font_size
        for text in ax.get_legend().get_texts():
            text.set_fontsize(legend_font_size)
            
            
def set_n_x_ticks(ax, n, x_min=None, x_max=None):
    x_ticks = ax.get_xticks()
    
    x_min = np.min(x_ticks) if x_min is None else x_min
    x_max = np.max(x_ticks) if x_max is None else x_max
    
    ax.set_xticks(np.linspace(x_min, x_max, n))
    
    
def set_n_y_ticks(ax, n, y_min=None, y_max=None):
    y_ticks = ax.get_yticks()
    
    y_min = np.min(y_ticks) if y_min is None else y_min
    y_max = np.max(y_ticks) if y_max is None else y_max
    
    ax.set_yticks(np.linspace(y_min, y_max, n))
