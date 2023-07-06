import numpy as np
from skimage.filters import threshold_otsu


def compute_mask(img,**kwargs):
        method = "otsu"
        for key, value in kwargs.items():
            if (key =="method"):
                method = value
            if (key =="threshold"):
                threshold = value
                
        if (method == "otsu"):
            threshold = threshold_otsu(self.get_MIP(0))

        mask = np.array(img > threshold,dtype = np.bool)
        return mask


def integrate_intensity(image,mask):
    masked_data = image
    masked_data = masked_data[mask]
    return np.mean(masked_data)
