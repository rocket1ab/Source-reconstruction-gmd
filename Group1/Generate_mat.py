#%%
import numpy as np
import pandas as pd
import scipy.io

rootdir_model = "./Simulation_datasets/release_"
subdir_model = "/test.xlsx"
rootdir_obs = "./Measurements" # 观测数据根路径
subdir_obs = "/Conc.xlsx" # 观测数据存储路径
rootdir_source_loc = './Training_datasets'
subdir_source_loc = '/Group1_location_6561.csv'

Sample_amount = 6561
sim_data = np.zeros((Sample_amount, 15, 4)) #mSv/h
unit = 'ng/m3'
Scaling_factor = 1

# Read simulation data
for location in range(1,Sample_amount+1):
    rootdir = rootdir_model + str(location)  # 需要转换的xls文件存放处
    location_single = pd.read_excel(rootdir+subdir_model,header=None)
    location_single = location_single.values
    # print(location_single.shape)
    sim_data[location-1, :, :] = location_single

# Read obs data
df_obs = pd.read_excel(rootdir_obs+subdir_obs,header=None) # 读取观测数据
obs_data = np.array(df_obs.values)

# Read source location
release_loc = pd.read_csv(rootdir_source_loc+subdir_source_loc,header=None)
release_loc_array = release_loc.iloc[:,0:2].values

# output mat file
scipy.io.savemat("./datafile.mat",
                 {"sim_data": sim_data,
                  "obs_data": obs_data,
                  "release_loc": release_loc_array,
                  "Scaling_factor": Scaling_factor,
                  "unit": unit   
                 })
# %% Read data mat
source_data = scipy.io.loadmat('./datafile.mat')

# %%
