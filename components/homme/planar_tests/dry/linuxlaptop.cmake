# CMake initial cache file for Linux 64bit RHEL6/CENTOS6
# tested with stock gcc/gfortran & openmpi
#
SET (CMAKE_Fortran_COMPILER mpif90 CACHE FILEPATH "")
SET (CMAKE_C_COMPILER mpicc CACHE FILEPATH "")
SET (CMAKE_CXX_COMPILER mpicc CACHE FILEPATH "")

SET (WITH_PNETCDF FALSE CACHE FILEPATH "")
#SET (NETCDF_DIR /home/celdred/netcdf-gnu CACHE FILEPATH "")
SET (PNETCDF_DIR /home/celdred/parallel-netcdf-gnu CACHE FILEPATH "")
SET (NetCDF_C_PATH /home/celdred/netcdf-gnu/netcdf-c CACHE FILEPATH "")
SET (NetCDF_Fortran_PATH /home/celdred/netcdf-gnu/netcdf-f CACHE FILEPATH "")



SET (NetCDF_C_INCLUDE_DIR /home/celdred/netcdf-gnu/netcdf-c/include CACHE FILEPATH "")
SET (NetCDF_C_LIBRARY /home/celdred/netcdf-gnu/netcdf-c/lib/libnetcdf.so CACHE FILEPATH "")
SET (NetCDF_Fortran_INCLUDE_DIR /home/celdred/netcdf-gnu/netcdf-f/include/ CACHE FILEPATH "")
SET (NetCDF_Fortran_LIBRARY /home/celdred/netcdf-gnu/netcdf-f/lib/libnetcdff.a CACHE FILEPATH "")


SET (USE_QUEUING FALSE CACHE BOOL "")
SET (HOMME_FIND_BLASLAPACK TRUE CACHE BOOL "")

SET (CPRNC_DIR /home/celdred/E3SM/components/homme/swe_tests CACHE FILEPATH "")
