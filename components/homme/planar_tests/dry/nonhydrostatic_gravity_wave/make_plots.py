
import sys
sys.path.append('../../')
from planar_plotting_helpers import get_dicts
from planar_plotting_helpers import plot_horiz, plot_horiz_multipanel, plot_xzslice, plot_yzslice, plot_xzslice_multipanel, plot_yzslice_multipanel

nlev = 10

#STATS PLOTTING
modellist = ['theta-nh','theta-h','preqx']

ncname = 'nhgw1.nc'
run_dir = '/run-' + sys.argv[1]
nml_name = 'namelist-' + sys.argv[1] + '.nl'

DSdict, coordsdict = get_dicts(modellist,run_dir, ncname, nml_name,nlev)

if sys.argv[1] == 'low': xzloc = 45
if sys.argv[1] == 'high': xzloc = 135
if sys.argv[1] == 'low-slice': xzloc = 1
if sys.argv[1] == 'high-slice': xzloc = 1
plot_horiz_multipanel(['lon','lat'], modellist, DSdict, coordsdict)
plot_horiz_multipanel(['ps',], modellist, DSdict, coordsdict, outlist=range(7))
plot_horiz_multipanel(['Th','u','v','omega','T'], modellist, DSdict, coordsdict, outlist=range(7), horiz_slice_level=4)
plot_xzslice_multipanel(['u','omega'], modellist, DSdict, coordsdict, xzloc, outlist=range(7))

# These below are useful for making sure the plotting routines are working correctly
# They are WAY too much output for analysis, however
#horiz_slice_level = 4
#xz_slice_loc = 45
#yz_slice_loc = 45
#outlist = range(7)
#varlist3D = ['Th','u','v','omega','T'] #'u','v','omega','T'
#varlist2D = ['ps',]
#constlist2D = ['lon','lat']
#plot_horiz(constlist2D, modellist, DSdict, coordsdict)
#plot_horiz_multipanel(constlist2D, modellist, DSdict, coordsdict)
#plot_horiz(constlist2D, modellist, DSdict, coordsdict, tri=True)
#plot_horiz_multipanel(constlist2D, modellist, DSdict, coordsdict, tri=True)

#plot_horiz(varlist2D, modellist, DSdict, coordsdict, outlist=outlist)
#plot_horiz_multipanel(varlist2D, modellist, DSdict, coordsdict, outlist=outlist)
#plot_horiz(varlist2D, modellist, DSdict, coordsdict, outlist=outlist, tri=True)
#plot_horiz_multipanel(varlist2D, modellist, DSdict, coordsdict, outlist=outlist, tri=True)

#plot_horiz(varlist3D, modellist, DSdict, coordsdict, outlist=outlist, horiz_slice_level=horiz_slice_level)
#plot_horiz_multipanel(varlist3D, modellist, DSdict, coordsdict, outlist=outlist, horiz_slice_level=horiz_slice_level)
#plot_horiz(varlist3D, modellist, DSdict, coordsdict, outlist=outlist, horiz_slice_level=horiz_slice_level, tri=True)
#plot_horiz_multipanel(varlist3D, modellist, DSdict, coordsdict, outlist=outlist, horiz_slice_level=horiz_slice_level, tri=True)
#plot_xzslice(varlist3D, modellist, DSdict, coordsdict, xz_slice_loc, outlist=outlist)
#plot_yzslice(varlist3D, modellist, DSdict, coordsdict, yz_slice_loc, outlist=outlist)
#plot_xzslice_multipanel(varlist3D, modellist, DSdict, coordsdict, xz_slice_loc, outlist=outlist)
#plot_yzslice_multipanel(varlist3D, modellist, DSdict, coordsdict, yz_slice_loc, outlist=outlist)
