import numpy as np
from vvmtools.plot import DataPlotter
from vvmtools.analyze import DataRetriever
import matplotlib.pyplot as plt

# prepare expname and data coordinate
expname  = 'pbl_hw9_s1'
nx = 128; x = np.arange(nx)*0.2
ny = 128; y = np.arange(ny)*0.2
nz = 50;  z = np.arange(nz)*0.04
nt = 721; t = np.arange(nt)*np.timedelta64(2,'m')+np.datetime64('2024-01-01 05:00:00')

# create dataPlotter class
figpath           = './Figure/hw9/'
data_domain       = {'x':x, 'y':y, 'z':z, 't':t}
data_domain_units = {'x':'km', 'y':'km', 'z':'km', 't':'LocalTime'}
dplot = DataPlotter(expname, figpath, data_domain, data_domain_units)

# TODO: Change to your own data
vvmtools_case = DataRetriever(f'/data/mlcloud/ch995334/VVM/DATA/{expname}')
# Get surface NO, NO2, NO3, averaged over y
NO  = vvmtools_case.get_var_parallel(var='NO', time_steps=np.arange(721), compute_mean=True, axis=-2)[:, 0, :]
NO2 = vvmtools_case.get_var_parallel(var='NO2', time_steps=np.arange(721), compute_mean=True, axis=-2)[:, 0, :]
NO3 = vvmtools_case.get_var_parallel(var='NO3', time_steps=np.arange(721), compute_mean=True, axis=-2)[:, 0, :]
NOx = NO+NO2+NO3
data_xt2d  = NOx

fig, ax, cax = dplot.draw_xt(data = data_xt2d,
                                levels = np.arange(0,30.001,2),
                                extend = 'max',
                                cmap_name = 'OrRd',
                                title_left  = 'NOx [ppb]',
                                title_right = f'Ocean-Forest',
                                figname     = 'test_hov.png',
                               )
plt.show()
