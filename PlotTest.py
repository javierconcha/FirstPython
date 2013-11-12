#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import matplotlib.colors as mpcolors
import Image
from osgeo import gdal # Geospatial Data Abstraction

from skimage import data, img_as_float, exposure
#----------------------------------------------------
# Load images
# filename = 'LC80170302013269LGN00'
filename = 'LC80160302013262LGN00' # 09-19-13

dirpath = ''.join(('/Users/javier/Desktop/Javier/PHD_RIT/LDCM/L8images/',filename,'/'))
filepathB2 = ''.join((dirpath,filename,'_B2.TIF'))
filepathB3 = ''.join((dirpath,filename,'_B3.TIF'))
filepathB4 = ''.join((dirpath,filename,'_B4.TIF'))
filepathB5 = ''.join((dirpath,filename,'_B5.TIF'))

# crop the image
# LC8017
# y0 = 6100
# y1 = 6800
# x0 = 3200
# x1 = 3600  

# LC8016
y0 = 2124
y1 = 2745
x0 = 3200
x1 = 3800

# imgB2 = mpimg.imread(filepathB2,format='TIFF')
# imgB3 = mpimg.imread(filepathB3,format='TIFF')
# imgB4 = mpimg.imread(filepathB4,format='TIFF')
# imgB5 = mpimg.imread(filepathB5,format='TIFF')

RasterB2 = gdal.Open(filepathB2)
RasterB3 = gdal.Open(filepathB3)
RasterB4 = gdal.Open(filepathB4)
RasterB5 = gdal.Open(filepathB5)

ArrayB2 = RasterB2.GetRasterBand(1).ReadAsArray()
ArrayB3 = RasterB3.GetRasterBand(1).ReadAsArray()
ArrayB4 = RasterB4.GetRasterBand(1).ReadAsArray()
ArrayB5 = RasterB5.GetRasterBand(1).ReadAsArray()

ArrayB2crop = ArrayB2[x0:x1,y0:y1]
ArrayB3crop = ArrayB3[x0:x1,y0:y1]
ArrayB4crop = ArrayB4[x0:x1,y0:y1]
ArrayB5crop = ArrayB5[x0:x1,y0:y1]

ArrayB2cropeq = exposure.equalize_adapthist(ArrayB2crop, clip_limit=0.03)
ArrayB3cropeq = exposure.equalize_adapthist(ArrayB3crop, clip_limit=0.03)
ArrayB4cropeq = exposure.equalize_adapthist(ArrayB4crop, clip_limit=0.03)
ArrayB5cropeq = exposure.equalize_adapthist(ArrayB5crop, clip_limit=0.03)
#----------------------------------------------------
# Display geotiff info
print RasterB2.GetGeoTransform()
print 'Driver: ', RasterB2.GetDriver().ShortName,'/',RasterB2.GetDriver().LongName
print 'Size is ',RasterB2.RasterXSize,'x',RasterB2.RasterYSize,'x',RasterB2.RasterCount
print 'Projection is ',RasterB2.GetProjection()
    
geotransform = RasterB2.GetGeoTransform()
if not geotransform is None:
    print 'Origin = (',geotransform[0], ',',geotransform[3],')'
    print 'Pixel Size = (',geotransform[1], ',',geotransform[5],')'

#----------------------------------------------------
# Display RGB image
plt.figure(1)

imgRGB = np.dstack((ArrayB4cropeq,ArrayB3cropeq,ArrayB2cropeq))
imgRGB = img_as_float(imgRGB)

imgplot = plt.imshow(imgRGB)
plt.grid(True)
plt.axis('equal')
plt.colorbar()
plt.show()
# #----------------------------------------------------
# # Plotting images
# plt.figure(2)
# plt.subplot(221)
# imgplot = plt.imshow(ArrayB5crop)
# plt.gray()
# plt.grid(True)
# plt.axis('equal')
# # plt.colorbar()

# plt.subplot(222)
# plt.hist(ArrayB5crop,fc='k',ec='k')

# plt.subplot(223)
# imgplot = plt.imshow(ArrayB5cropeq)
# plt.gray()
# plt.grid(True)
# plt.axis('equal')
# # plt.colorbar()

# plt.subplot(224)
# plt.hist(ArrayB5cropeq,fc='k',ec='k')

# plt.show()
#----------------------------------------------------
# def f(t):
# 	return np.exp(-t)*np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()

#----------------------------------------------------
# import Image # search Python Imaging Library Handbook

# fileName = "./image_tutorial-1.png";

# imageObject = Image.open( fileName );

# imagePixelDataRGB = list( imageObject.getdata() );

# numPixels = len( imagePixelDataRGB )

# imagePixelDataR = [];
# imagePixelDataG = [];
# imagePixelDataB = [];
# imagePixelDataA = [];


# for i in range( 0, numPixels, 1 ):

# 	imagePixelDataR.append( (imagePixelDataRGB[i])[0] );
# 	imagePixelDataG.append( (imagePixelDataRGB[i])[1] );
# 	imagePixelDataB.append( (imagePixelDataRGB[i])[2] );

# 	if ( len( imagePixelDataRGB[i]) ):
# 		imagePixelDataA.append( (imagePixelDataRGB[i])[3]);

# 	#fi
# #rof

# print imagePixelDataRGB[0:10:2]