# 2014-12-02 02.44 am
# Note: Presets have been done as Maya stock attrPresets
#       ior4standard and iorExpression are not yet implemented

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import mtoa.utils as utils
import mtoa.ui.ae.utils as aeUtils
from mtoa.ui.ae.shaderTemplate import ShaderAETemplate


modeModeEnumOp = [
    (0, 'Custom'), 
    (1, 'Preset'), 
    (2, 'File'), 
]


def Obq_FresnelCreateModeMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_FresnelModeMode', attribute=attr, label="Mode", 
                               enumeratedItem=modeModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetModeMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_FresnelModeMode', edit=True, attribute=attr)
    

# ADD MATERIAL PRESETS HERE AND DOWN IN THE LOGIC SECTION       #
# KEEP ALPHABETICAL ORDER, NUMBERS ARE ONLY IMPORTANT FOR LOGIC #

presetsModeEnumOp = [
    (39, '---------------------- METALS -----------------------'), 
    (0, 'Aluminium (Al) [Rakic]'), 
    (1, 'Aluminium Copper (AlCu)'), 
    (2, 'Chromium (Cr) [Palik]'), 
    (3, 'Chromium (Cr) [Sopra]'), 
    (4, 'Cobalt (Co) [Sopra]'), 
    (5, 'Copper (Cu) [Palik]'), 
    (6, 'Gold (Au) [Palik]'), 
    (7, 'Iridium (Ir) [Palik]'), 
    (42, 'Iron (Fe) [Palik]'), 
    (8, 'Lithium (Li) [Sopra]'), 
    (9, 'Mercury (Hg) [Palik]'), 
    (10, 'Nickel (Ni) [Palik]'), 
    (11, 'Osmium (Os) [Palik]'), 
    (12, 'Palladium (Pd) [Sopra]'), 
    (13, 'Platinum (Pt) [Palik]'), 
    (14, 'Rhodium (Rh) [Palik]'), 
    (15, 'Silver (Ag) [Palik]'), 
    (16, 'Tantalum (Ta) [Sopra]'), 
    (17, 'Titanium (Ti) [Sopra]'), 
    (18, 'Tungsten (W) [Palik]'), 
    (41, '---------------------- LIQUIDS ----------------------'), 
    (19, 'Acetone (CH3COCH3) [Rheims]'), 
    (20, 'Ethanol (C2H5OH) [Rheims]'), 
    (21, 'Ethylene Glycol (C2H4(OH)2) [El-Kashef]'), 
    (22, 'Glycerol (C3H5(OH)3) [Birkhoff]'), 
    (23, 'Honey [RobinWood]'), 
    (24, 'Milk [RobinWood]'), 
    (25, 'Shampoo [RobinWood]'), 
    (26, 'Vegetable Oil [RobinWood]'), 
    (27, 'Water (H20) [Hale]'), 
    (38, '-------------------- CRYSTALS etc. ------------------'), 
    (28, 'Acrylic (Plexiglass)'), 
    (29, 'Crystal [RobinWood]'), 
    (30, 'Diamond (C) [Handbook of Optics]'), 
    (31, 'Emerald [RobinWood]'), 
    (32, 'Garnet [RobinWood]'), 
    (33, 'Glass (Schott N-KF9 crown/flint)'), 
    (34, 'Ice (H20) [Warren]'), 
    (35, 'Salt (NaCl) [Palik]'), 
    (40, '---------------------- PLASTICS ---------------------'), 
    (36, 'Cellulose [Kasarova]'), 
    (37, 'Polystyrene (PS) [Kasarova]'), 
]

def Obq_FresnelCreatePresetsMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_FresnelPresetsMode', attribute=attr, label="Presets", 
                               enumeratedItem=presetsModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetPresetsMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_FresnelPresetsMode', edit=True, attribute=attr)
    

methodModeEnumOp = [
    (0, 'Refractive'), 
    (1, 'Metal'), 
]

def Obq_FresnelCreateMethodMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_FresnelMethodMode', attribute=attr, label="Material Type", 
                               enumeratedItem=methodModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetMethodMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_FresnelMethodMode', edit=True, attribute=attr)
    

lambdaUnitsModeEnumOp = [
    (0, 'Nano (nm) [360-830]'), 
    (1, 'Micro (um) [0.360-0.830]'), 
]

def Obq_FresnelCreateLambdaUnitsMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_FresnelLambdaUnitsMode', attribute=attr, label="Wavelength Units", 
                               enumeratedItem=lambdaUnitsModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetLambdaUnitsMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_FresnelLambdaUnitsMode', edit=True, attribute=attr)
    
backfaceModeEnumOp = [
    (0, 'Same as Frontface'), 
    (1, 'Swap IORs (Media In -> n2)'), 
    (2, 'Always White'), 
    (3, 'Always Black'), 
]

def Obq_FresnelCreateBackfaceMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_FresnelBackfaceMode', attribute=attr, label="Backface", 
                               enumeratedItem=backfaceModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetBackfaceMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_FresnelBackfaceMode', edit=True, attribute=attr)
    
outputGammaModeEnumOp = [
    (0, 'Linear'), 
    (1, 'sRGB'), 
]

def Obq_FresnelCreateOutputGammaMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_FresnelOutputGammaMode', attribute=attr, label="Gamma", 
                               enumeratedItem=outputGammaModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetOutputGammaMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_FresnelOutputGammaMode', edit=True, attribute=attr)
    
    
inputTypeModeEnumOp = [
    (0, 'RGB (LEGACY)'), 
    (1, 'String SPD'), 
]

def Obq_FresnelCreateInputTypeMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_FresnelInputTypeMode', attribute=attr, label="inputType", 
                               enumeratedItem=inputTypeModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetInputTypeMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_FresnelInputTypeMode', edit=True, attribute=attr)
      
      
ccModeModeEnumOp = [
    (0, 'Off'), 
    (1, 'HSV'), 
    (1, 'HLS'), 
]

def Obq_FresnelCreateccModeMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_FresnelccModeMode', attribute=attr, label="Mode", 
                               enumeratedItem=ccModeModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetccModeMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_FresnelccModeMode', edit=True, attribute=attr)
        
saturationOpModeEnumOp = [
    (0, 'Add'), 
    (1, 'Multiply'), 
    (2, 'Exponent'), 
]

def Obq_FresnelCreateSaturationOpMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_FresnelSaturationOpMode', attribute=attr, label="Operation", 
                               enumeratedItem=saturationOpModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetSaturationOpMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_FresnelSaturationOpMode', edit=True, attribute=attr)
        
xyz2rgbModeEnumOp = [
    (0, 'sRGB Illuminant E'), 
    (1, 'sRGB Illuminant D65 <- E (Bradford)'), 
    (2, 'sRGB Illuminant D65'), 
]

def Obq_FresnelCreatexyz2rgbMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('Obq_Fresnelxyz2rgbMode', attribute=attr, label="XYZ to RGB Matrix", 
                               enumeratedItem=xyz2rgbModeEnumOp)    
    cmds.setUITemplate(popTemplate=True)

def Obq_FresnelSetxyz2rgbMode(attr):
    cmds.attrEnumOptionMenuGrp('Obq_Fresnelxyz2rgbMode', edit=True, attribute=attr)
        
                        
    
def Obq_FresnelHelpURL():
    # Add the Obq_Shader docs URL to the Attribute Editor help menu
    ObqNodeType = 'Obq_Fresnel'
    ObqNodeHelpURL = 'http://s3aws.obliquefx.com/public/shaders/help_files/Obq_Fresnel.html'
    ObqHelpCommand = 'addAttributeEditorNodeHelp("' + ObqNodeType + '", "showHelp -absolute \\"' +ObqNodeHelpURL +'\\"");'
    mel.eval(ObqHelpCommand)

class AEObq_FresnelTemplate(ShaderAETemplate):
    convertToMayaStyle = True
    
    def setup(self):

        self.addSwatch()

        self.beginScrollLayout()

        self.addCustom('message', 'AEshaderTypeNew', 'AEshaderTypeReplace')

        pm.picture(image='Obq_shader_header.png', parent="AttrEdObq_FresnelFormLayout")
        Obq_FresnelHelpURL()

        self.beginLayout("Main", collapse=False )
        
        self.beginLayout("Settings", collapse=False )
        self.addCustom("mode", Obq_FresnelCreateModeMode, Obq_FresnelSetModeMode)
        self.addCustom("inputType", Obq_FresnelCreateInputTypeMode, Obq_FresnelSetInputTypeMode)
        self.endLayout() #End Settings
                
        #self.beginLayout("Presets", collapse=True )
        # ADD NEW MATERIAL HERE AND DON'T FORGET TO ADD IT IN THE LAYOUT COMBO BOX
        # .spd, .csv and .txt, can be taken from :
        # PBRT
        # http://www.filmetrics.com/refractive-index-database 
        # or http://refractiveindex.info/?group=METALS&material=Gold
        #self.addCustom("presets", Obq_FresnelCreatePresetsMode, Obq_FresnelSetPresetsMode)
        #self.endLayout() #End Presets

        
        self.beginLayout("SPD (Strings or File *.csv, *.txt, *.spd)", collapse=False )
        self.addControl("iorFilename", label="Filename")
        self.addControl("lambdasStr", label="Lambda")
        self.addControl("etasStr", label="Eta (n)")
        self.addControl("ksStr", label="k")
        self.addCustom("lambdaUnits", Obq_FresnelCreateLambdaUnitsMode, Obq_FresnelSetLambdaUnitsMode)
        self.endLayout() #End File
        
        self.beginLayout("Refractive Indices", collapse=False )
        self.addControl("iorRGB", label="n")
        self.endLayout() #End Refractive Indices
        
        self.beginLayout("Extinction Coefficients", collapse=False )
        self.addControl("kRGB", label="k")
        self.endLayout() #End Extinction Coefficients
        
        self.beginLayout("Equations", collapse=False )
        self.addCustom("method", Obq_FresnelCreateMethodMode, Obq_FresnelSetMethodMode)
        self.endLayout() #End Equations
        
        self.beginLayout("Options", collapse=False )
        self.addControl("roughness", label="Roughness")
        self.addControl("ratioFsFp", label="Ratio of polarized Fs/Fp")
        self.addCustom("backfaceMode", Obq_FresnelCreateBackfaceMode, Obq_FresnelSetBackfaceMode)
        self.endLayout() #End Options
        
        self.beginLayout("Output", collapse=False )
        self.beginNoOptimize()
        self.addControl("transmittance", label="Output Refraction Color")
        self.endNoOptimize()
        self.endLayout() #End Output
        
        self.beginLayout("Media In Refractive Indices", collapse=False )
        self.addControl("iorInRGB", label="n")
        self.endLayout() #End Media In Refractive Indices
        
        
        self.beginLayout("Advanced", collapse=True )
        

        self.beginLayout("LookUp Table", collapse=True )
        self.addControl("useLUT", label="Enable precalculated LUT")
        self.addControl("LUTSampleSize", label="Sample size (degrees)")
        self.addControl("roughnessSampleSize", label="Roughness sample size")
        self.endLayout() #End LookUp Table
        
        self.beginLayout("Spectrum", collapse=False )
        self.addControl("useFullSpectrum", label="Use full spectrum data in equations (metal)")
        self.endLayout() #End Spectrum
        
        self.beginLayout("ColorSpace", collapse=True )
        self.addCustom("xyz2rgb", Obq_FresnelCreatexyz2rgbMode, Obq_FresnelSetxyz2rgbMode)
        self.addControl("outputGamma", label="Gamma")
        self.addControl("degamma", label="DeGamma metals for linear workflow")
        self.endLayout() #End ColorSpace
        
        self.beginLayout("Color Adjustment", collapse=True )
        self.addCustom("ccMode", Obq_FresnelCreateccModeMode, Obq_FresnelSetccModeMode)   
        self.addControl("hueShift", label="Hue Shift (degree)")
        
        self.beginLayout("Saturation", collapse=True )
        self.addControl("saturationMod", label="Modifier")        
        self.addCustom("saturationOp", Obq_FresnelCreateSaturationOpMode, Obq_FresnelSetSaturationOpMode)   
        self.endLayout() #End Saturation
     
        self.endLayout() #End Color Adjustment
        
        self.endLayout() #End Advanced
        
        #self.beginLayout("Standard IOR", collapse=False )
        #self.addControl("iorExpression", label="Expression for standard IOR")
        #self.endLayout() #End Standard IOR
        
        self.endLayout() #End Main
        
        # include/call base class/node attributes
        pm.mel.AEdependNodeTemplate(self.nodeName)

        # Hide the NormalCamera and HardwareColor Extra Attributes
        self.suppress('normalCamera')
        self.suppress('hardwareColor')

        self.addExtraControls()
        self.endScrollLayout()