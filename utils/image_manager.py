import numpy as np
import czifile as cz
import os as os
from skimage.filters import threshold_otsu

class Image:
    def __init__(self, filename):
        self.data = cz.imread(filename)
        self.ID = filename.split(os.sep)[-1]
        self.mask = np.ones_like(self.data[0])  ## Temporary mask, full of ones

    def get_MIP(self, channel):  ##Max intensity projection on one channel
        tamp_data = self.data[channel]
        return np.max(tamp_data,axis = 0)[:,:,0]

    def get_MIPS(self):  ## Max intensity projection on all channels
        return np.max(self.data,axis =1)[:,:,0]

    def get_AP(self, channel):  ## Average projection on one channel
        tamp_data = self.data[channel]
        return np.mean(tamp_data,axis = 0)[:,:,0]

    def get_APS(self):
        return np.mean(self.data,axis =1)[:,:,0]




    


