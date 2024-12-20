import numpy as np
import xarray as xr
import glob

def create_var_dict(case_name:str)->dict:
    """
    (1) Dict storing all variable names and the corresponding file names
    (2) Dict storing all variable longnames and corresponding variable names
    """
    # TODO: create flist (all *00000.nc)
    flist = glob.glob(f'/data/mlcloud/ch995334/VVM/DATA/{case_name}/archive/*-000000.nc')
    # TODO: get file name label
    fpath = f'/data/mlcloud/ch995334/VVM/DATA/{case_name}/archive/'
    fprece= f'{case_name}.X.'   # file name precedent label
    ftail = f'-000000.nc'       # file name tail
    # TODO: search through file variables and store file name label
    var_fname = {}              # key[variable], value[file name label]
    var_longname = {}           # key[variable long name], value[variable]
    for ff in flist:
        ds   = xr.open_dataset(ff)
        for vv in ds.data_vars:
            var_fname[vv] = ff[(len(fpath)+len(fprece)):-len(ftail)]
            var_longname[ds[vv].attrs['long_name']] = vv
    return var_fname, var_longname

def get_vvm_var(case_name:str, var_name:str, var_dict:dict, assigned_timestep:int=-1)->xr.DataArray:
    """
    Get file name label from input dictionary (Remove this part in the future).
    If no assigned_timestep: default to read all possible time steps.
    """
    fpath = f'/data/mlcloud/ch995334/VVM/DATA/{case_name}/archive/'
    label = var_dict[var_name]
    if assigned_timestep>=0:
        fname = glob.glob(f'{fpath}*{label}-{assigned_timestep:06d}.nc')[0]
        return xr.open_dataset(fname)[var_name]
    else:
        print("Please assign a non-negative integer for time step.")
        #flist = sorted(glob.glob(f'{fpath}*{label}-*.nc'))
        #print(len(flist))
        #return xr.open_mfdataset(flist)
        

### Test
def main():
    case_name = 'pbl_modVVM'
    dict_fname= create_var_dict(case_name)[0]
    print(get_vvm_var(case_name, 'u', dict_fname))
    
    
if __name__=='__main__':
    main()