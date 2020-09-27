
import sys
sys.path.append('../../')
from planar_plotting_helpers import get_dicts
from planar_plotting_helpers import plot_horiz, plot_horiz_multipanel, plot_xzslice, plot_yzslice, plot_xzslice_multipanel, plot_yzslice_multipanel

nlev = 20

#STATS PLOTTING
modellist = ['theta-nh','theta-h','preqx']

ncname = 'hgw1.nc'
run_dir = '/run-' + sys.argv[1]
nml_name = 'namelist-' + sys.argv[1] + '.nl'

DSdict, coordsdict = get_dicts(modellist,run_dir, ncname, nml_name,nlev)

if sys.argv[1] == 'low': xzloc = 90
if sys.argv[1] == 'high': xzloc = 270
if sys.argv[1] == 'low-slice': xzloc = 1
if sys.argv[1] == 'high-slice': xzloc = 1
plot_horiz_multipanel(['lon','lat'], modellist, DSdict, coordsdict)
plot_horiz_multipanel(['ps',], modellist, DSdict, coordsdict, outlist=range(7))
plot_horiz_multipanel(['Th','u','v','omega','T'], modellist, DSdict, coordsdict, outlist=range(7), horiz_slice_level=9)
plot_xzslice_multipanel(['u','omega'], modellist, DSdict, coordsdict, xzloc, outlist=range(7))
