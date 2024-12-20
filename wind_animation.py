# Import
import numpy as np
import xarray as xr
from datetime import *
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import seaborn.colors.xkcd_rgb as c
import cmaps

ds_dyn = xr.open_mfdataset(f'/data/mlcloud/ch995334/VVM/DATA/pbl_control_dt/archive/pbl_control_dt.L.Dynamic*')
da_u   = ds_dyn.u
da_v   = ds_dyn.v
da_w   = ds_dyn.w
# 1000m = level 26 (python idx 25)
# Field 1000m
u1000 = da_u.isel(lev=25)
v1000 = da_v.isel(lev=25)
w1000 = da_w.isel(lev=25)
# Wind field 1000m
time_now    = datetime(2024, 1, 1, 5, 0, 0)
for tt in range(u1000.shape[0]):
    fig, ax = plt.subplots(figsize=(6, 6))
    imw     = ax.imshow(w1000[tt, ...], vmin=-2, vmax=2, origin='lower', cmap=cmaps.MPL_RdBu)
    ax.quiver(np.arange(128)[::4], np.arange(128)[::4], u1000[tt, ::4, ::4], v1000[tt, ::4, ::4])
    cax     = fig.add_axes([ax.get_position().x1+0.015, ax.get_position().y0, 0.02, ax.get_position().height])
    cbar    = fig.colorbar(imw, cax=cax, extend='both')
    cbar.ax.tick_params(labelsize=14)
    cbar.set_label(label='w (m/s)', fontsize=14)
    ax.set_xticks(np.arange(0, 128.1, 40))
    ax.set_xticklabels(np.arange(0, 128.1, 40)*0.2, fontsize=14)
    ax.set_xlabel('km', fontsize=14)
    ax.set_yticks(np.arange(0, 128.1, 40))
    ax.set_yticklabels(np.arange(0, 128.1, 40)*0.2, fontsize=14)
    ax.set_ylabel('km', fontsize=14)
    ax.set_title('Wind Field @ 1000m', loc='left', fontsize=16)
    ax.set_title(time_now.strftime('%H:%M'), loc='right', fontsize=16)
    plt.savefig(f'/data/mlcloud/ch995334/hw1/wind_animation/dt5_{time_now.strftime("%d%H%M")}.png', 
                facecolor='w', bbox_inches='tight', dpi=400)
    time_now= time_now+timedelta(minutes=1)