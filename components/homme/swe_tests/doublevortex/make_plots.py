import xarray as xr
import f90nml
import sys
sys.path.append('../')
from swe_plotting_helpers import convert_to_2D, calculate_2D_indices, triplot_var, plot_var, extract_var, extract_2Dvar

DS = xr.open_dataset('run/dbvor1.nc')
nml = f90nml.read('dblvortex.nl')

geop = DS.geop
u = DS.u
v = DS.v
x = DS.lon
y = DS.lat
zeta = DS.zeta
div = DS.div
ps = DS.ps
eta = DS.eta
pv = DS.pv

indx,npx,npy = calculate_2D_indices(nml,x,y)
x2D = convert_to_2D(x,indx,npx,npy)
y2D = convert_to_2D(y,indx,npx,npy)

#triplot_var(extract_var(ps,ts=0), x, y, 'ps')
#triplot_var(extract_var(x), x, y, 'x')
#triplot_var(extract_var(y), x, y, 'y')

plot_var(extract_2Dvar(ps,indx,npx,npy,ts=0), x2D, y2D, 'ps')
plot_var(extract_2Dvar(x,indx,npx,npy), x2D, y2D, 'x')
plot_var(extract_2Dvar(y,indx,npx,npy), x2D, y2D, 'y')

for i in range(11):
    #triplot_var(extract_var(zeta,ts=i,level=0), x, y, 'zeta'+str(i))
    #triplot_var(extract_var(eta,ts=i,level=0), x, y, 'eta'+str(i))
    #triplot_var(extract_var(pv,ts=i,level=0), x, y, 'pv'+str(i))
    #triplot_var(extract_var(div,ts=i,level=0), x, y, 'div'+str(i))
    #triplot_var(extract_var(geop,ts=i,level=0), x, y, 'geop'+str(i))
    #triplot_var(extract_var(u,ts=i,level=0), x, y, 'u'+str(i))
    #triplot_var(extract_var(v,ts=i,level=0), x, y, 'v'+str(i))

    plot_var(extract_2Dvar(zeta,indx,npx,npy,ts=i,level=0), x2D, y2D, 'zeta'+str(i))
    plot_var(extract_2Dvar(eta,indx,npx,npy,ts=i,level=0), x2D, y2D, 'eta'+str(i))
    plot_var(extract_2Dvar(pv,indx,npx,npy,ts=i,level=0), x2D, y2D, 'pv'+str(i))
    plot_var(extract_2Dvar(div,indx,npx,npy,ts=i,level=0), x2D, y2D, 'div'+str(i))
    plot_var(extract_2Dvar(geop,indx,npx,npy,ts=i,level=0), x2D, y2D, 'geop'+str(i))
    plot_var(extract_2Dvar(u,indx,npx,npy,ts=i,level=0), x2D, y2D, 'u'+str(i))
    plot_var(extract_2Dvar(v,indx,npx,npy,ts=i,level=0), x2D, y2D, 'v'+str(i))
