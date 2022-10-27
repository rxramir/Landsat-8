#import pathlib
#import argparse
import sys, os, glob
import numpy as np
from osgeo import gdal, gdalnumeric, ogr, osr

#**********************************************************************************************************************
# Code to add a land mask layer to a coposite landsat image
# Input: path to original composited landsat image, path to land mask
# Output: A Landsat image with the land mask added as the 12th band
#**********************************************************************************************************************

def resolution_change(L8path, landmaskpath):
    L8_comp = gdal.Open(L8path)
    landmask = gdal.Open(landmaskpath)
    mask = landmask.GetRasterBand(1).ReadAsArray()
    
    tmp_comp = gdal.GetDriverByName('MEM').CreateCopy('', L8_comp, 0)
    tmp_comp.AddBand()
    tmp_comp.GetRasterBand(12).WriteArray(mask)
    
    outputpath = L8path # + '.tif'
    dst_ds = gdal.GetDriverByName("GTiff").CreateCopy(outputpath, tmp_comp, 0)
    del dst_ds
resolution_change("C:/Users/rramirez.HBG-S1258/OneDrive - Science Systems and Applications, Inc/Documents/September/LC08_L1TP_052014_20180727_20180731_01_T1/LC08_L1TP_052014_20180727_20180731_01_T1.TIF", "C:/Users/rramirez.HBG-S1258/OneDrive - Science Systems and Applications, Inc/Documents/Land Mask Layers/LC08_L1TP_052014_20180727_20180731_01_T1/LC08_L1TP_052014_20180727_20180731_01_T1_landmask.tif")
#resolution_change('C:/Users/aashapur/cloud_masking/scripts/S2A_MSIL1C_20181207T160501_N0207_R054_T17PKM_20181207T192419.SAFE/IMG_DATA')