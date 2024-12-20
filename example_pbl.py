import numpy as np
from vvmtools.plot import DataPlotter
import matplotlib.pyplot as plt

# prepare expname and data coordinate
expname  = 'pbl_control'
nx = 128; x = np.arange(nx)*0.2
ny = 128; y = np.arange(ny)*0.2
nz = 50;  z = np.arange(nz)*0.04
nt = 721; t = np.arange(nt)*np.timedelta64(2,'m')+np.datetime64('2024-01-01 05:00:00')

# create dataPlotter class
figpath           = './fig/'
data_domain       = {'x':x, 'y':y, 'z':z, 't':t}
data_domain_units = {'x':'km', 'y':'km', 'z':'km', 't':'LocalTime'}
dplot = DataPlotter(expname, figpath, data_domain, data_domain_units)

# TODO: Use your tracer data, noted that you need to normalize the data by its maximum
# Normalize: data/data.max()
np.random.seed(0)
data_zt2d  = np.random.normal(0, 0.1, size=(nz,nt))

# TODO: Use your boundary layer height
line1_1d = np.sin( np.linspace(0, 2*np.pi, nt) ) +1
line2_1d = np.cos( np.linspace(0, 2*np.pi, nt) ) +1

fig, ax, cax = dplot.draw_zt(data = data_zt2d,
                            levels = np.arange(0,1.1,0.1),
                            extend = 'neither',
                            pblh_dicts={'line1': line1_1d,
                                        'line2': line2_1d,
                                    },
                            title_left  = 'draw_zt pblh example',
                            title_right = f'right_land_type',
                            cmap_name   = 'Greys',
                            figname     = 'test_pbl.png',
                      )

###
### If you want to delete the legend, turn this block on
# ax.get_legend().remove()
# plt.savefig(f'{figpath}/colorbar.png', dpi=200)
# plt.close('all')
###

plt.show()