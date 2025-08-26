
import numpy as np

def calc_fwhm(d_tel=8.2,wvlh_microns=[1.25,1.65,2.18]):
 
 fwhm=1.028*206265*np.array(wvlh_microns)*1e-6/d_tel

 print(fwhm)


if __name__ == '__main__':

 calc_fwhm()
