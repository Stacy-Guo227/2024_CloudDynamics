# Import
import numpy as np
import xarray as xr
from datetime import *
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import seaborn.colors.xkcd_rgb as c
import cmaps

ds_thm = xr.open_mfdataset(f'/data/mlcloud/ch995334/VVM/DATA/pbl_control_dt/archive/pbl_control_dt.L.Thermodynamic*')
# 1000m = level 26 (python idx 25)
pi1000 = 0.967    #T=theta*pi
da_t   = ds_thm.th
T1000  = da_t.isel(lev=25)*pi1000
# qv field 1000m
time_now    = datetime(2024, 1, 1, 5, 0, 0)
for tt in range(T1000.shape[0]):
    fig, ax = plt.subplots(figsize=(6, 6))
    imT     = ax.imshow(T1000[tt, ...], vmin=286.6, vmax=287.6, origin='lower', cmap=cmaps.cmocean_matter)
    cax     = fig.add_axes([ax.get_position().x1+0.015, ax.get_position().y0, 0.02, ax.get_position().height])
    cbar    = fig.colorbar(imT, cax=cax, extend='both')
    cbar.ax.tick_params(labelsize=14)
    cbar.set_label(label='T (K)', fontsize=14)
    ax.set_xticks(np.arange(0, 128.1, 40))
    ax.set_xticklabels(np.arange(0, 128.1, 40)*0.2, fontsize=14)
    ax.set_xlabel('km', fontsize=14)
    ax.set_yticks(np.arange(0, 128.1, 40))
    ax.set_yticklabels(np.arange(0, 128.1, 40)*0.2, fontsize=14)
    ax.set_ylabel('km', fontsize=14)
    ax.set_title('Temp. Field @ 1000m', loc='left', fontsize=16)
    ax.set_title(time_now.strftime('%H:%M'), loc='right', fontsize=16)
    plt.savefig(f'/data/mlcloud/ch995334/hw1/T_animation/dt5_{time_now.strftime("%d%H%M")}.png', 
                facecolor='w', bbox_inches='tight', dpi=400)
    time_now= time_now+timedelta(minutes=1)