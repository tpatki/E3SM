import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import f90nml

def get_dicts(modellist, run_dir, ncname, nml_name,nlev):
    DSdict = {}
    coordsdict = {}
    for model in modellist:
        DS = xr.open_dataset(model + '/' + run_dir + '/' + ncname)
        nml = f90nml.read(model + '/' + nml_name)

        x = DS['lon']
        y = DS['lat']
        lev = DS['lev']
        topo = calculate_topo(nml,x,y,nlev)
        x2D, y2D = convert_coords_to_2D(x,y,topo)

        DSdict[model] = DS
        coordsdict[model] = {}
        coordsdict[model]['x'] = x
        coordsdict[model]['y'] = y
        coordsdict[model]['lev'] = lev
        coordsdict[model]['x2D'] = x2D
        coordsdict[model]['y2D'] = y2D
        coordsdict[model]['topo'] = topo
    return DSdict,coordsdict

class topo:
    def __init__(self,indx,npx,npy,nlev):
        self.indx = indx
        self.npx = npx
        self.npy = npy
        self.nlev = nlev

def calculate_topo(nml,x,y,nlev):

    sorted_ind = np.lexsort((y,x))
    npp = 4
    npx = nml['ctl_nl']['ne_x'] * (npp-1)
    npy = nml['ctl_nl']['ne_y'] * (npp-1)
    return topo(sorted_ind,npx,npy,nlev)

def convert_to_2D(var,topo):
    return np.reshape(var[topo.indx].values,(topo.npx,topo.npy))

def convert_coords_to_2D(x,y,topo):
    return convert_to_2D(x,topo), convert_to_2D(y,topo)

def triplot_horiz_var(var, x, y, name):
    plt.figure(figsize=(10,8))

    plt.tricontourf(x,y,var)
    plt.colorbar()
    plt.tricontour(x,y,var)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(name+'.tri.png')
    plt.close('all')

def triplot_horiz_var_multipanel(var, x, y, titles, name):
    npanels = len(var)
    plt.figure(figsize=(10*npanels,8))
    for i in range(npanels):
        plt.subplot(1,npanels,i+1)
        plt.tricontourf(x[i],y[i],var[i])
        plt.colorbar()
        plt.tricontour(x[i],y[i],var[i])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(titles[i])
    plt.tight_layout()
    plt.savefig(name+'.tri.png')
    plt.close('all')

def plot_horiz_var(var, x, y, name):
    plt.figure(figsize=(10,8))
    plt.contourf(x,y,var)
    plt.colorbar()
    plt.contour(x,y,var)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(name+'.png')
    plt.close('all')

def plot_horiz_var_multipanel(var, x, y, titles, name):
    npanels = len(var)
    plt.figure(figsize=(10*npanels,8))
    for i in range(npanels):
        plt.subplot(1,npanels,i+1)
        plt.contourf(x[i],y[i],var[i])
        plt.colorbar()
        plt.contour(x[i],y[i],var[i])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(titles[i])
    plt.tight_layout()
    plt.savefig(name+'.png')
    plt.close('all')

def plot_xzslice_var(var, x, z, name):
    plt.figure(figsize=(10,8))
    plt.contourf(x,z,var)
    plt.colorbar()
    plt.contour(x,z,var)
    plt.xlabel('x')
    plt.ylabel('z')
    plt.savefig(name+'.png')
    plt.close('all')

def plot_xzslice_var_multipanel(var, x, z, titles, name):
    npanels = len(var)
    plt.figure(figsize=(10*npanels,8))
    for i in range(npanels):
        plt.subplot(1,npanels,i+1)
        plt.contourf(x[i],z[i],var[i])
        plt.colorbar()
        plt.contour(x[i],z[i],var[i])
        plt.xlabel('x')
        plt.ylabel('z')
        plt.title(titles[i])
    plt.tight_layout()
    plt.savefig(name+'.png')
    plt.close('all')

def plot_yzslice_var(var, y, z, name):
    plt.figure(figsize=(10,8))
    plt.contourf(y,z,var)
    plt.colorbar()
    plt.contour(y,z,var)
    plt.xlabel('y')
    plt.ylabel('z')
    plt.savefig(name+'.png')
    plt.close('all')

def plot_yzslice_var_multipanel(var, y, z, titles, name):
    npanels = len(var)
    plt.figure(figsize=(10*npanels,8))
    for i in range(npanels):
        plt.subplot(1,npanels,i+1)
        plt.contourf(y[i],z[i],var[i])
        plt.colorbar()
        plt.contour(y[i],z[i],var[i])
        plt.xlabel('y')
        plt.ylabel('z')
        plt.title(titles[i])
    plt.tight_layout()
    plt.savefig(name+'.png')
    plt.close('all')

    # extract_horiz_var (time,lev,ncol) -> 1D array of ncol at given (optional) time and lev
    # extract_2D_horiz_var (time,ncol) -> 2D array x,y at given (optional) time
    # extract_3D_var (time,lev,ncol) -> 3D array lev,x,y at given (optional) time

def extract_horiz_var(var, ts=None, level=None):
    if ts is None and level is None:
        return var[:]
    elif level is None:
        return var[ts,:]
    else:
        return var[ts,level,:]

def extract_2D_horiz_var(var, topo, ts=None, level=None):
    evar = extract_horiz_var(var,ts=ts,level=level)
    return convert_to_2D(evar,topo)

def extract_3D_var(var, topo, ts=None):
    if ts is None:
        return np.reshape(var[:,topo.indx].values,(topo.nlev,topo.npx,topo.npy))
    else:
        return np.reshape(var[ts,:,topo.indx].values,(topo.nlev,topo.npx,topo.npy))


def plot_horiz(varlist, modellist, DSdict, coordsdict, outlist=[None,], horiz_slice_level=None, tri=False):
    for var in varlist:
        for model in modellist:
            for i in outlist:
                plotname = model+'.'+var+str(i)+'.xy'+str(horiz_slice_level)
                if horiz_slice_level is None:
                    plotname = model+'.'+var+str(i)
                if i is None and horiz_slice_level is None:
                    plotname = model+'.'+var

                if tri:
                    x = coordsdict[model]['x']
                    y = coordsdict[model]['y']
                    vararr = extract_horiz_var(DSdict[model][var],ts=i,level=horiz_slice_level)
                    triplot_horiz_var(vararr,x,y,model+'.'+plotname)
                else:
                    x = coordsdict[model]['x2D']
                    y = coordsdict[model]['y2D']
                    vararr = extract_2D_horiz_var(DSdict[model][var],coordsdict[model]['topo'],ts=i,level=horiz_slice_level)
                    plot_horiz_var(vararr,x,y,plotname)

def plot_horiz_multipanel(varlist, modellist, DSdict, coordsdict, outlist=[None,], horiz_slice_level=None, tri=False):
    for var in varlist:
        for i in outlist:
            plotname = var+str(i)+'.xy'+str(horiz_slice_level)
            if horiz_slice_level is None:
                plotname = var+str(i)
            if i is None and horiz_slice_level is None:
                plotname = var
            xlist =[]
            ylist =[]
            varlist = []
            for model in modellist:
                if tri:
                    xlist.append(coordsdict[model]['x'])
                    ylist.append(coordsdict[model]['y'])
                    varlist.append(extract_horiz_var(DSdict[model][var],ts=i,level=horiz_slice_level))
                else:
                    xlist.append(coordsdict[model]['x2D'])
                    ylist.append(coordsdict[model]['y2D'])
                    varlist.append(extract_2D_horiz_var(DSdict[model][var],coordsdict[model]['topo'],ts=i,level=horiz_slice_level))
            if tri:
                triplot_horiz_var_multipanel(varlist, xlist, ylist, modellist, plotname)
            else:
                plot_horiz_var_multipanel(varlist, xlist, ylist, modellist, plotname)

def plot_xzslice(varlist, modellist, DSdict, coordsdict, xz_slice_loc, outlist=[None,]):

    for var in varlist:
        for model in modellist:
            x = coordsdict[model]['x2D']
            z = coordsdict[model]['lev']
            for i in outlist:
                plotname = model+'.'+var+str(i)+'.xz'+str(xz_slice_loc)
                if i is None:
                    plotname = model+'.'+var+'.xz'+str(xz_slice_loc)
                vararr = extract_3D_var(DSdict[model][var],coordsdict[model]['topo'],ts=i)
                plot_xzslice_var(vararr[:,:,xz_slice_loc],x2D[:,xz_slice_loc],z,plotname)

def plot_yzslice(varlist, modellist, DSdict, coordsdict, yz_slice_loc, outlist=[None,]):
    for var in varlist:
        for model in modellist:
            y = coordsdict[model]['y2D']
            z = coordsdict[model]['lev']
            for i in outlist:
                plotname = model+'.'+var+str(i)+'.yz'+str(yz_slice_loc)
                if i is None:
                    plotname = model+'.'+var+'.yz'+str(yz_slice_loc)
                vararr = extract_3D_var(DSdict[model][var],coordsdict[model]['topo'],ts=i)
                plot_yzslice_var(vararr[:,yz_slice_loc,:],y2D[yz_slice_loc,:],z,plotname)

def plot_xzslice_multipanel(varlist, modellist, DSdict, coordsdict, xz_slice_loc, outlist=[None,]):

    for var in varlist:
        for i in outlist:
            plotname = var+str(i)+'.xz'+str(xz_slice_loc)
            if i is None:
                plotname = var+'.xz'+str(xz_slice_loc)
            xlist =[]
            zlist =[]
            varlist = []
            for model in modellist:
                xlist.append(coordsdict[model]['x2D'][:,xz_slice_loc])
                zlist.append(coordsdict[model]['lev'])
                varlist.append(extract_3D_var(DSdict[model][var],coordsdict[model]['topo'],ts=i)[:,:,xz_slice_loc])
            plot_xzslice_var_multipanel(varlist, xlist, zlist, modellist, plotname)

def plot_yzslice_multipanel(varlist, modellist, DSdict, coordsdict, yz_slice_loc, outlist=[None,]):
    for var in varlist:
        for i in outlist:
            plotname = var+str(i)+'.yz'+str(yz_slice_loc)
            if i is None:
                plotname = var +'.yz'+str(yz_slice_loc)
            ylist =[]
            zlist =[]
            varlist = []
            for model in modellist:
                ylist.append(coordsdict[model]['y2D'][yz_slice_loc,:])
                zlist.append(coordsdict[model]['lev'])
                varlist.append(extract_3D_var(DSdict[model][var],coordsdict[model]['topo'],ts=i)[:,yz_slice_loc,:])
            plot_yzslice_var_multipanel(varlist, ylist, zlist, modellist, plotname)
