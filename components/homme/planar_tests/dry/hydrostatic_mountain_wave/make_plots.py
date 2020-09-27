import xarray as xr
import matplotlib.pyplot as plt
import numpy as np


def plot_3Dvar(var, x, y, name, level, i):
    plt.figure(figsize=(10,8))
    plt.tricontourf(x,y,var.isel(time=i,lev=level))
    plt.colorbar()
    plt.tricontour(x,y,var.isel(time=i,lev=level))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(name+str(i)+'.'+str(level)+'.png')
    plt.close('all')

def plot_2Dvar(var, x, y, name, i):
    plt.figure(figsize=(10,8))
    plt.tricontourf(x,y,var.isel(time=i))
    plt.colorbar()
    plt.tricontour(x,y,var.isel(time=i))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(name+str(i)+'.png')
    plt.close('all')

def plot_2Dconst(var, x, y, name):
    plt.figure(figsize=(10,8))
    plt.tricontourf(x,y,var)
    plt.colorbar()
    plt.tricontour(x,y,var)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(name+'.png')
    plt.close('all')

# MULTI-PANEL PLOTTING?
DS_list = []
for model in ['theta-nh','preqx','theta-h']:

    DS = xr.open_dataset(model + '/run/hgw1.nc')
    DS_list.append(DS)

    T = DS.T
    u = DS.u
    v = DS.v
    omega = DS.omega
    x = DS.lon
    y = DS.lat
    Th = DS.Th

    #STATS PLOTTING

    plot_2Dconst(x, x, y, model+'.x')
    plot_2Dconst(y, x, y, model+'.y')

    for i in range(7):
    	plot_3Dvar(Th, x, y, model+'.Th', 9, i)
    	plot_3Dvar(T, x, y, model+'.T', 9, i)
    	plot_3Dvar(u, x, y, model+'.u', 9, i)
    	plot_3Dvar(v, x, y, model+'.v', 9, i)
    	plot_3Dvar(omega, x, y, model+'.omega', 9, i)
