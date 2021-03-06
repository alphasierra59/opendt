######################
#Colour Math Library
######################

#########################
#   Standard Observers  #
#########################

#CIE 1931 Standard Observer Lookup Table
#Published by CIE 
#   http://www.cie.co.at/
#   http://files.cie.co.at/204.xls
CIE1931StdObs = { 
    380	: [0.001368,0.000039,0.006450],
    385	: [0.002236,0.000064,0.010550],
    390	: [0.004243,0.000120,0.020050],
    395	: [0.007650,0.000217,0.036210],
    400	: [0.014310,0.000396,0.067850],
    405	: [0.023190,0.000640,0.110200],
    410	: [0.043510,0.001210,0.207400],
    415	: [0.077630,0.002180,0.371300],
    420	: [0.134380,0.004000,0.645600],
    425	: [0.214770,0.007300,1.039050],
    430	: [0.283900,0.011600,1.385600],
    435	: [0.328500,0.016840,1.622960],
    440	: [0.348280,0.023000,1.747060],
    445	: [0.348060,0.029800,1.782600],
    450	: [0.336200,0.038000,1.772110],
    455	: [0.318700,0.048000,1.744100],
    460	: [0.290800,0.060000,1.669200],
    465	: [0.251100,0.073900,1.528100],
    470	: [0.195360,0.090980,1.287640],
    475	: [0.142100,0.112600,1.041900],
    480	: [0.095640,0.139020,0.812950],
    485	: [0.057950,0.169300,0.616200],
    490	: [0.032010,0.208020,0.465180],
    495	: [0.014700,0.258600,0.353300],
    500	: [0.004900,0.323000,0.272000],
    505	: [0.002400,0.407300,0.212300],
    510	: [0.009300,0.503000,0.158200],
    515	: [0.029100,0.608200,0.111700],
    520	: [0.063270,0.710000,0.078250],
    525	: [0.109600,0.793200,0.057250],
    530	: [0.165500,0.862000,0.042160],
    535	: [0.225750,0.914850,0.029840],
    540	: [0.290400,0.954000,0.020300],
    545	: [0.359700,0.980300,0.013400],
    550	: [0.433450,0.994950,0.008750],
    555	: [0.512050,1.000000,0.005750],
    560	: [0.594500,0.995000,0.003900],
    565	: [0.678400,0.978600,0.002750],
    570	: [0.762100,0.952000,0.002100],
    575	: [0.842500,0.915400,0.001800],
    580	: [0.916300,0.870000,0.001650],
    585	: [0.978600,0.816300,0.001400],
    590	: [1.026300,0.757000,0.001100],
    595	: [1.056700,0.694900,0.001000],
    600	: [1.062200,0.631000,0.000800],
    605	: [1.045600,0.566800,0.000600],
    610	: [1.002600,0.503000,0.000340],
    615	: [0.938400,0.441200,0.000240],
    620	: [0.854450,0.381000,0.000190],
    625	: [0.751400,0.321000,0.000100],
    630	: [0.642400,0.265000,0.000050],
    635	: [0.541900,0.217000,0.000030],
    640	: [0.447900,0.175000,0.000020],
    645	: [0.360800,0.138200,0.000010],
    650	: [0.283500,0.107000,0.000000],
    655	: [0.218700,0.081600,0.000000],
    660	: [0.164900,0.061000,0.000000],
    665	: [0.121200,0.044580,0.000000],
    670	: [0.087400,0.032000,0.000000],
    675	: [0.063600,0.023200,0.000000],
    680	: [0.046770,0.017000,0.000000],
    685	: [0.032900,0.011920,0.000000],
    690	: [0.022700,0.008210,0.000000],
    695	: [0.015840,0.005723,0.000000],
    700	: [0.011359,0.004102,0.000000],
    705	: [0.008111,0.002929,0.000000],
    710	: [0.005790,0.002091,0.000000],
    715	: [0.004109,0.001484,0.000000],
    720	: [0.002899,0.001047,0.000000],
    725	: [0.002049,0.000740,0.000000],
    730	: [0.001440,0.000520,0.000000],
    735	: [0.001000,0.000361,0.000000],
    740	: [0.000690,0.000249,0.000000],
    745	: [0.000476,0.000172,0.000000],
    750	: [0.000332,0.000120,0.000000],
    755	: [0.000235,0.000085,0.000000],
    760	: [0.000166,0.000060,0.000000],
    765	: [0.000117,0.000042,0.000000],
    770	: [0.000083,0.000030,0.000000],
    775	: [0.000059,0.000021,0.000000],
    780	: [0.000042,0.000015,0.000000]
}

#CIE 1964 Standard Observer Lookup Table
#Published by CIE 
#   http://www.cie.co.at/
#   http://files.cie.co.at/204.xls
CIE1964StdObs = {
    380 : [0.000160, 0.000017, 0.000705],
    385 : [0.000662, 0.000072, 0.002928],
    390 : [0.002362, 0.000253, 0.010482],
    395 : [0.007242, 0.000769, 0.032344],
    400 : [0.019110, 0.002004, 0.086011],
    405 : [0.043400, 0.004509, 0.197120],
    410 : [0.084736, 0.008756, 0.389366],
    415 : [0.140638, 0.014456, 0.656760],
    420 : [0.204492, 0.021391, 0.972542],
    425 : [0.264737, 0.029497, 1.282500],
    430 : [0.314679, 0.038676, 1.553480],
    435 : [0.357719, 0.049602, 1.798500],
    440 : [0.383734, 0.062077, 1.967280],
    445 : [0.386726, 0.074704, 2.027300],
    450 : [0.370702, 0.089456, 1.994800],
    455 : [0.342957, 0.106256, 1.900700],
    460 : [0.302273, 0.128201, 1.745370],
    465 : [0.254085, 0.152761, 1.554900],
    470 : [0.195618, 0.185190, 1.317560],
    475 : [0.132349, 0.219940, 1.030200],
    480 : [0.080507, 0.253589, 0.772125],
    485 : [0.041072, 0.297665, 0.570060],
    490 : [0.016172, 0.339133, 0.415254],
    495 : [0.005132, 0.395379, 0.302356],
    500 : [0.003816, 0.460777, 0.218502],
    505 : [0.015444, 0.531360, 0.159249],
    510 : [0.037465, 0.606741, 0.112044],
    515 : [0.071358, 0.685660, 0.082248],
    520 : [0.117749, 0.761757, 0.060709],
    525 : [0.172953, 0.823330, 0.043050],
    530 : [0.236491, 0.875211, 0.030451],
    535 : [0.304213, 0.923810, 0.020584],
    540 : [0.376772, 0.961988, 0.013676],
    545 : [0.451584, 0.982200, 0.007918],
    550 : [0.529826, 0.991761, 0.003988],
    555 : [0.616053, 0.999110, 0.001091],
    560 : [0.705224, 0.997340, 0.000000],
    565 : [0.793832, 0.982380, 0.000000],
    570 : [0.878655, 0.955552, 0.000000],
    575 : [0.951162, 0.915175, 0.000000],
    580 : [1.014160, 0.868934, 0.000000],
    585 : [1.074300, 0.825623, 0.000000],
    590 : [1.118520, 0.777405, 0.000000],
    595 : [1.134300, 0.720353, 0.000000],
    600 : [1.123990, 0.658341, 0.000000],
    605 : [1.089100, 0.593878, 0.000000],
    610 : [1.030480, 0.527963, 0.000000],
    615 : [0.950740, 0.461834, 0.000000],
    620 : [0.856297, 0.398057, 0.000000],
    625 : [0.754930, 0.339554, 0.000000],
    630 : [0.647467, 0.283493, 0.000000],
    635 : [0.535110, 0.228254, 0.000000],
    640 : [0.431567, 0.179828, 0.000000],
    645 : [0.343690, 0.140211, 0.000000],
    650 : [0.268329, 0.107633, 0.000000],
    655 : [0.204300, 0.081187, 0.000000],
    660 : [0.152568, 0.060281, 0.000000],
    665 : [0.112210, 0.044096, 0.000000],
    670 : [0.081261, 0.031800, 0.000000],
    675 : [0.057930, 0.022602, 0.000000],
    680 : [0.040851, 0.015905, 0.000000],
    685 : [0.028623, 0.011130, 0.000000],
    690 : [0.019941, 0.007749, 0.000000],
    695 : [0.013842, 0.005375, 0.000000],
    700 : [0.009577, 0.003718, 0.000000],
    705 : [0.006605, 0.002565, 0.000000],
    710 : [0.004553, 0.001768, 0.000000],
    715 : [0.003145, 0.001222, 0.000000],
    720 : [0.002175, 0.000846, 0.000000],
    725 : [0.001506, 0.000586, 0.000000],
    730 : [0.001045, 0.000407, 0.000000],
    735 : [0.000727, 0.000284, 0.000000],
    740 : [0.000508, 0.000199, 0.000000],
    745 : [0.000356, 0.000140, 0.000000],
    750 : [0.000251, 0.000098, 0.000000],
    755 : [0.000178, 0.000070, 0.000000],
    760 : [0.000126, 0.000050, 0.000000],
    765 : [0.000090, 0.000036, 0.000000],
    770 : [0.000065, 0.000025, 0.000000],
    775 : [0.000046, 0.000018, 0.000000],
    780 : [0.000033, 0.000013, 0.000000]
}

##TODO
#need to figure out an interpolation scheme
def CIE1931ObsInterp(wavelength):
    
    if(wavelength >= 780):
        raise ValueError("Cannot interpolate past 780nm")
    
    CIE1931StdObs[wavelength]
        
    return CIE1931StdObs[wavelength]

##TODO
def CIE1931ObsInterp(wavelength):
    
    return 0

#############################
#   Standard Illuminants    #
#############################

#Standard Illuminant White Points
#Defining class for points
class StdIllumWhitePt:
    
    x = 0
    y = 0
    CCT = 0

    def __init__(self,xCoord,yCoord,CCTVal):
        #CIE 1931 Chromaticity Coordinates
        self.x   = xCoord
        self.y   = yCoord
        self.CCT = CCTVal

#Various Standard Illuminant White Points
#TODO insert citation
A_Wpt   = StdIllumWhitePt(0.44757,0.40745,2856)     #Incandescent / Tungsten
D50_WPt = StdIllumWhitePt(0.34567,0.35850,5003)     #Horizon Light. ICC profile PCS
D55_WPt = StdIllumWhitePt(0.33242,0.34743,5503)     #Mid-morning / Mid-afternoon Daylight
D65_WPt = StdIllumWhitePt(0.31271,0.32902,6504)     #Noon Daylight: Television, sRGB color space
D75_WPt = StdIllumWhitePt(0.29902,0.31485,7504)     #North sky Daylight
E_WPt   = StdIllumWhitePt((1/3)  ,(1/3)  ,5454)	    #Equal energy
F1_WPt  = StdIllumWhitePt(0.31310,0.33727,6430)     #Daylight Fluorescent
F2_WPt  = StdIllumWhitePt(0.37208,0.37529,4230)     #Cool White Fluorescent
F3_WPt  = StdIllumWhitePt(0.40910,0.39430,3450)     #White Fluorescent
F4_WPt  = StdIllumWhitePt(0.44018,0.40329,2940)     #Warm White Fluorescent
F5_WPt  = StdIllumWhitePt(0.31379,0.34531,6350)     #Daylight Fluorescent
F6_WPt  = StdIllumWhitePt(0.37790,0.38835,4150)     #Lite White Fluorescent
F7_WPt  = StdIllumWhitePt(0.31292,0.32933,6500)     #D65 simulator, Daylight simulator
F8_WPt  = StdIllumWhitePt(0.34588,0.35875,5000)     #D50 simulator, Sylvania F40 Design 50
F9_WPt  = StdIllumWhitePt(0.37417,0.37281,4150)     #Cool White Deluxe Fluorescent
F10_WPt = StdIllumWhitePt(0.34609,0.35986,5000)     #Philips TL85, Ultralume 50
F11_WPt = StdIllumWhitePt(0.38052,0.37713,4000)     #Philips TL84, Ultralume 40
F12_WPt = StdIllumWhitePt(0.43695,0.40441,3000)     #Philips TL83, Ultralume 30

#CIE D65 Standard Illuminant Lookup Table
#Published by CIE 
#   http://www.cie.co.at/
#   http://files.cie.co.at/204.xls
#   Meant to represent average midday light in western europe
CIE_D65 = {
    300 : 0.034100,
    305 : 1.664300,
    310 : 3.294500,
    315 : 11.765200,
    320 : 20.236000,
    325 : 28.644700,
    330 : 37.053500,
    335 : 38.501100,
    340 : 39.948800,
    345 : 42.430200,
    350 : 44.911700,
    355 : 45.775000,
    360 : 46.638300,
    365 : 49.363700,
    370 : 52.089100,
    375 : 51.032300,
    380 : 49.975500,
    385 : 52.311800,
    390 : 54.648200,
    395 : 68.701500,
    400 : 82.754900,
    405 : 87.120400,
    410 : 91.486000,
    415 : 92.458900,
    420 : 93.431800,
    425 : 90.057000,
    430 : 86.682300,
    435 : 95.773600,
    440 : 104.865000,
    445 : 110.936000,
    450 : 117.008000,
    455 : 117.410000,
    460 : 117.812000,
    465 : 116.336000,
    470 : 114.861000,
    475 : 115.392000,
    480 : 115.923000,
    485 : 112.367000,
    490 : 108.811000,
    495 : 109.082000,
    500 : 109.354000,
    505 : 108.578000,
    510 : 107.802000,
    515 : 106.296000,
    520 : 104.790000,
    525 : 106.239000,
    530 : 107.689000,
    535 : 106.047000,
    540 : 104.405000,
    545 : 104.225000,
    550 : 104.046000,
    555 : 102.023000,
    560 : 100.000000,
    565 : 98.167100,
    570 : 96.334200,
    575 : 96.061100,
    580 : 95.788000,
    585 : 92.236800,
    590 : 88.685600,
    595 : 89.345900,
    600 : 90.006200,
    605 : 89.802600,
    610 : 89.599100,
    615 : 88.648900,
    620 : 87.698700,
    625 : 85.493600,
    630 : 83.288600,
    635 : 83.493900,
    640 : 83.699200,
    645 : 81.863000,
    650 : 80.026800,
    655 : 80.120700,
    660 : 80.214600,
    665 : 81.246200,
    670 : 82.277800,
    675 : 80.281000,
    680 : 78.284200,
    685 : 74.002700,
    690 : 69.721300,
    695 : 70.665200,
    700 : 71.609100,
    705 : 72.979000,
    710 : 74.349000,
    715 : 67.976500,
    720 : 61.604000,
    725 : 65.744800,
    730 : 69.885600,
    735 : 72.486300,
    740 : 75.087000,
    745 : 69.339800,
    750 : 63.592700,
    755 : 55.005400,
    760 : 46.418200,
    765 : 56.611800,
    770 : 66.805400,
    775 : 65.094100,
    780 : 63.382800,
    785 : 63.843400,
    790 : 64.304000,
    795 : 61.877900,
    800 : 59.451900,
    805 : 55.705400,
    810 : 51.959000,
    815 : 54.699800,
    820 : 57.440600,
    825 : 58.876500,
    830 : 60.312500
}

######################
#Constants
######################
#Reference Whites


#############################
#   CIE 1931 Colour Space   #
#############################
#RGB to Tristim

#Tristim to x y
"""Convert XYZ tristimulus values to xy chromaticity coordinates"""
def TriTOxy(TriX,TriY,TriZ):
    
    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    xCoord = (TriX/(TriX+TriY+TriZ))
    yCoord = (TriY/(TriX+TriY+TriZ))
    return [xCoord,yCoord]

#Tristim to x
def TriTOx(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    xCoord = (TriX/(TriX+TriY+TriZ))
    return xCoord

#Tristim to y
def TriTOy(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    yCoord = (TriY/(TriX+TriY+TriZ))
    return yCoord

#xy to Tristim
def xyTOTri(x,y,TriY):

    if (not isinstance(x,(int,float))):
        raise TypeError("x value must be float or int")
    
    if (not isinstance(y,(int,float))):
        raise TypeError("y value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("TriY value must be float or int")
    
    XCoord = ((x/y)*TriY)
    ZCoord = (((1-x-y)/y)*TriY)
    return[XCoord,YCoord,ZCoord]

#############################
#   CIE 1976 Colour Space   #
#############################
#Lightness from Luminance
def YtoL(luminance, refwhiteluminance):
    
    #Reference White Luminance
    Y_n = 1 ##TODO --> is there some standard?
    
    if (not isinstance(luminance,(int,float))):
        raise TypeError("Luminance value must be float or int")
        
    if (not isinstance(refwhiteluminance,(int,float))):
        raise TypeError("Reference White Luminance must be float or int")
    
    normalizedLuminance = (luminance / refwhiteluminance)
    
    if(normalizedLuminance <= 0.008856):
        lightness = 903.3 * normalizedLuminance
    elif (normalizedLuminance > 0.008856):
        lightness = (116 * (normalizedLuminance**(1/3)) - (1/16))
        
    if((lightness < 0) or (lightness>100)):
        raise ValueError("Lightness L* value %d outside of allowed range 0-100" % lightness)
    
    return lightness

#Lightness from normalized Luminance
def YNormalizedtoL(luminance):
        
    if (not isinstance(luminance,(int,float))):
        raise TypeError("Luminance value must be float or int")
    
    return lightness

#Tristim to u v
def TriTOuv(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    uCoord = ((4*TriX)/(TriX+15*TriY+3*TriZ))
    vCoord = ((9*TriY)/(TriX+15*TriY+3*TriZ))
    return[uCoord,vCoord]

#Tristim to u
def TriTOu(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    uCoord = ((4*TriX)/(TriX+15*TriY+3*TriZ))
    return uCoord

#Tristim to v
def TriTOv(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    vCoord = ((9*TriY)/(TriX+15*TriY+3*TriZ))
    return vCoord

#########################################
#   CIE 1931 to/from 1960 Colour Space  #
#########################################
#x y to u v
def xyTOuv(xCoord, yCoord):
    
    if (not isinstance(xCoord,(int,float))):
        raise TypeError("xCoord value must be float or int")
    
    if (not isinstance(yCoord,(int,float))):
        raise TypeError("yCoord value must be float or int")
    
    uCoord = ((4*xCoord)/(3-2*xCoord+12*yCoord))
    vCoord = ((9*yCoord)/(3-2*xCoord+12*yCoord))
    return[uCoord,vCoord]

#uv to xy
def uvTOxy(uCoord, vCoord):

    if (not isinstance(uCoord,(int,float))):
        raise TypeError("uCoord value must be float or int")
    
    if (not isinstance(vCoord,(int,float))):
        raise TypeError("vCoord value must be float or int")
    
    xCoord = ((9*uCoord)/(6*uCoord-16*vCoord+12))
    yCoord = ((4*vCoord)/(6*uCoord-16*vCoord+12))
    return[xCoord,yCoord]
    
#####################
#   Calculate CCT   #
#####################
#CCT from xy
def CCTxy(xCoord, yCoord):

    if (not isinstance(xCoord,(int,float))):
        raise TypeError("xCoord value must be float or int")
    
    if (not isinstance(yCoord,(int,float))):
        raise TypeError("yCoord value must be float or int")
        
    n = ((xCoord-0.3320)/(0.1858-yCoord))
    CCT = (449*(n**3) + 3525*(n**2) + (6823.3*n) + 5520.33)
    
    return CCT

#CCT from TriStim
def CCT_Tri(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("TriX value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("TriY value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("TriZ value must be float or int")
        
    xCoord = TriTOx(TriX,TriY,TriZ)
    yCoord = TriTOx(TriX,TriY,TriZ)
        
    n = ((xCoord-0.3320)/(0.1858-yCoord))
    CCT = (449*(n**3) + 3525*(n**2) + (6823.3*n) + 5520.33)
    
    return CCT
    
#CCT from RGB
def CCT_RGB(RedVal, GreenVal, BlueVal):

    if (not isinstance(RedVal,(int,float))):
        raise TypeError("RedVal value must be float or int")
    
    if (not isinstance(GreenVal,(int,float))):
        raise TypeError("GreenVal value must be float or int")
    
    if (not isinstance(BlueVal,(int,float))):
        raise TypeError("BlueVal value must be float or int")
        
    n = ((0.23881*RedVal)+(0.25499*GreenVal)+(-0.58291*BlueVal))
    CCT = (449*(n**3) + 3525*(n**2) + (6823.3*n) + 5520.33)
    
    return CCT
    