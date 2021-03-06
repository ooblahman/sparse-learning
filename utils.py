import matplotlib.pyplot as plt
import torch
import numpy as np
import seaborn as sns

def plot_df(df):
    '''
    Assumes first column x, other columns y_i
    '''
    xcol = df.columns[0]
    cmap = plt.cm.rainbow(np.linspace(0, 1, len(df.columns[1:])))
    for ycol, color in zip(df.columns[1:], cmap):
        plt.plot(xcol, ycol, data=df, color=color)
        plt.legend()

def density(x):
    return torch.norm(x.abs().add(0.9).floor(), 0)

def layer_parameters(layer):
    return torch.cat([x.view(-1) for x in layer.parameters()]) 

def plot_layers(model): 
    with torch.no_grad():
        fc1 = layer_parameters(model.fc1).cpu().numpy()
        fc2 = layer_parameters(model.fc2).cpu().numpy()
        fig, (ax,ax2) = plt.subplots(nrows=2)
        sns.heatmap([fc1], ax=ax, cmap='plasma')
        ax.set_yticks([])
        ax.set_xticks(np.arange(len(fc1)))
        ax.set_title('Layer 1')
        sns.heatmap([fc2], ax=ax2, cmap='plasma')
        ax2.set_yticks([])
        ax2.set_xticks(np.arange(len(fc2)))
        ax2.set_title('Layer 2')
        ax2.set_xlabel('parameters')
        plt.tight_layout()
        plt.show()

def prune(tensor, threshold):
	tensor[torch.abs(tensor) < threshold] = 0
	return tensor