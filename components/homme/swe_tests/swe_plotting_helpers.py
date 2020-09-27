import numpy as np
import matplotlib.pyplot as plt

def calculate_2D_indices(nml,x,y):

    sorted_ind = np.lexsort((y,x))
    npp = 4
    npx = nml['ctl_nl']['ne_x'] * (npp-1)
    npy = nml['ctl_nl']['ne_y'] * (npp-1)
    return sorted_ind,npx,npy

def convert_to_2D(var,indx,npx,npy):
    return np.reshape(var[indx].values,(npx,npy))

def triplot_var(var, x, y, name):
    plt.figure(figsize=(10,8))
    plt.tricontourf(x,y,var)
    plt.colorbar()
    plt.tricontour(x,y,var)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(name+'.tri.png')
    plt.close('all')

def plot_var(var, x, y, name):
    plt.figure(figsize=(10,8))
    plt.contourf(x,y,var)
    plt.colorbar()
    plt.contour(x,y,var)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(name+'.png')
    plt.close('all')

def extract_var(var, ts=None, level=None):
    if ts is None and level is None:
        return var
    elif level is None:
        return var.isel(time=ts)
    else:
        return var.isel(time=ts,nlev=level)

def extract_2Dvar(var, indx,npx,npy, ts=None, level=None):
    evar = extract_var(var,ts=ts,level=level)
    return convert_to_2D(evar,indx,npx,npy)
