import numpy as np
from plottools import dataPlotters
import matplotlib.pyplot as plt
# TODO 1: import your vvmtools
import vvmtoolsV2

# TODO 2: change the expname to your experiment name
# prepare expname and data coordinate
casename = 'pbl_mod_wfire_coastal_s1'
vvmtools = vvmtoolsV2.VVMtools(f"/data/mlcloud/ch995334/VVM/DATA/{casename}")
nx = 128; x = np.arange(nx)*0.2
ny = 128; y = np.arange(ny)*0.2
nz = 50;  z = np.arange(1, nz)*0.04
nt = 721; t = np.arange(nt)*np.timedelta64(2,'m')+np.datetime64('2024-01-01 05:00:00')

# TODO 3: change the data to your data (seven lines for BL height and one shading for w'th')
# read or create data
domain_range = (None, None, None, None, None, 64)
# domain_range = (None, None, None, None, 64, None)
# domain_range = (None, None, None, None, None, None)
func_config  = {'domain_range':domain_range, 'wind_var':'w', 'prop_var':'th'}
turb_flux    = vvmtools.func_time_parallel(func=vvmtools.cal_turb_flux, 
                                           time_steps=np.arange(nt), 
                                           func_config=func_config, cores=10)
data_zt2d    = np.nanmean(turb_flux, axis=(-2, -1)).T

func_config  = {'domain_range':domain_range, 'method':'th05k', 'compute_mean_axis':'xy'}
line1_1d = vvmtools.func_time_parallel(func=vvmtools.get_pbl_height, time_steps=np.arange(nt), 
                                       func_config=func_config, cores=10)*1e-3
func_config  = {'domain_range':domain_range, 'method':'dthdz', 'compute_mean_axis':'xy'}
line2_1d = vvmtools.func_time_parallel(func=vvmtools.get_pbl_height, time_steps=np.arange(nt), 
                                       func_config=func_config, cores=10)*1e-3
func_config  = {'domain_range':domain_range, 'method':'tke', 'threshold':1e-1}
line3_1d = vvmtools.func_time_parallel(func=vvmtools.get_pbl_height, time_steps=np.arange(nt), 
                                       func_config=func_config, cores=10)*1e-3
func_config  = {'domain_range':domain_range, 'method':'enstrophy', 'threshold':1e-5}
line4_1d = vvmtools.func_time_parallel(func=vvmtools.get_pbl_height, time_steps=np.arange(nt), 
                                       func_config=func_config, cores=10)*1e-3
# func_config  = {'domain_range':domain_range, 'method':'wth', 'threshold':1e-3}
# result = vvmtools.func_time_parallel(func=vvmtools.get_pbl_height, 
#                                      time_steps=np.arange(nt), 
#                                      func_config=func_config, cores=10)*1e-3
# line5_1d, line6_1d, line7_1d = result[:,0], result[:,1], result[:,2]

# TODO 4: change the figpath to your figure path
# create dataPlotter class
figpath           = './Figure/'
data_domain       = {'x':x, 'y':y, 'z':z, 't':t}
data_domain_units = {'x':'km', 'y':'km', 'z':'km', 't':'LocalTime'}
dplot = dataPlotters(casename, figpath, data_domain, data_domain_units)

# draw z-t diagram
# input data dimension is (nz, nt)
# [output] figure, axis, colorbar axis

# TODO 5: change the levels to your data range, 
#         add pblh_dicts for your seven lines, 
#         change the title_left and title_right,
#         change figname for output file name.
fig, ax, cax = dplot.draw_zt(data = data_zt2d, \
                             levels = np.arange(-0.04, 0.041, 0.005), \
                             extend = 'both', \
                             pblh_dicts={r'$\theta$ + 0.5K': line1_1d,\
                                         r'max d$\theta$/dz': line2_1d,\
                                         'TKE': line3_1d,\
                                         'Enstrophy': line4_1d,\
                                         # r"top($\overline{w'\theta'}$+)":line5_1d,\
                                         # r"min($\overline{w'\theta'}$)":line6_1d,\
                                         # r"top($\overline{w'\theta'}$-)":line7_1d
                                        },\
                             title_left  = r'Vertical $\theta$ transport', \
                             title_right = f'Ocean average', \
                             figname     = 'hw7_1_ocn_cs1_ver2.png',\
                      )

plt.show()

