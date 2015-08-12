#ifndef _ainode_Obq_Toon_h_
#define _ainode_Obq_Toon_h_

enum
{
   C4DAI_OBQ_TOON_MAIN_GRP                            = 2001,

   C4DAIP_OBQ_TOON_GLOBAL_LOOPLIGHTMODE               = 17408859,
   C4DAIP_OBQ_TOON_GLOBAL_COMPMODE                    = 783134376,
   C4DAIP_OBQ_TOON_GLOBAL_LOOPMODE                    = 609033859,
   C4DAIP_OBQ_TOON_GLOBAL_MULTBYLIGHTCOLOR            = 1314177736,
   C4DAIP_OBQ_TOON_AMBIENT_COLOR                      = 1017219442,
   C4DAIP_OBQ_TOON_AMBIENT_SCALE                      = 1035750843,
   C4DAIP_OBQ_TOON_AMBIENT_MULTAMBIENCE               = 670348151,
   C4DAIP_OBQ_TOON_DIFFUSE_COLOR                      = 760546504,
   C4DAIP_OBQ_TOON_DIFFUSE_SCALE                      = 742015103,
   C4DAIP_OBQ_TOON_DIFFUSE_COVERAGE                   = 1791761349,
   C4DAIP_OBQ_TOON_DIFFUSE_SOFTNESS                   = 178532462,
   C4DAIP_OBQ_TOON_DIFFUSE_MODE                       = 1278817470,
   C4DAIP_OBQ_TOON_DIFFUSE_GRADIENT                   = 777069977,
   C4DAIP_OBQ_TOON_DIFFUSE_IMAGE                      = 753515108,
   C4DAIP_OBQ_TOON_DIFFUSE_IMAGETYPE                  = 1508365566,
   C4DAIP_OBQ_TOON_HIGHLIGHT_COLOR                    = 1124069558,
   C4DAIP_OBQ_TOON_HIGHLIGHT_SCALE                    = 1105538157,
   C4DAIP_OBQ_TOON_HIGHLIGHT_EXPONENT                 = 1007041756,
   C4DAIP_OBQ_TOON_HIGHLIGHT_COVERAGE                 = 1140683113,
   C4DAIP_OBQ_TOON_HIGHLIGHT_SOFTNESS                 = 1541055296,
   C4DAIP_OBQ_TOON_HIGHLIGHT_MODE                     = 1397952144,
   C4DAIP_OBQ_TOON_HIGHLIGHT_GRADIENT                 = 585452857,
   C4DAIP_OBQ_TOON_HIGHLIGHT_IMAGE                    = 1117038162,
   C4DAIP_OBQ_TOON_HIGHLIGHT_IMAGETYPE                = 773021168,
   C4DAIP_OBQ_TOON_RIMLIGHT_COLOR                     = 1093502706,
   C4DAIP_OBQ_TOON_RIMLIGHT_SCALE                     = 1112034107,
   C4DAIP_OBQ_TOON_RIMLIGHT_COVERAGE                  = 1364409025,
   C4DAIP_OBQ_TOON_RIMLIGHT_SOFTNESS                  = 1317329384,
   C4DAIP_OBQ_TOON_RIMLIGHT_MODE                      = 1985753400,
   C4DAIP_OBQ_TOON_RIMLIGHT_GRADIENT                  = 361726945,
   C4DAIP_OBQ_TOON_RIMLIGHT_IMAGE                     = 1100534102,
   C4DAIP_OBQ_TOON_RIMLIGHT_IMAGETYPE                 = 433958328,
   C4DAIP_OBQ_TOON_AMBIENT_FB_STR                     = 689970221,
   C4DAIP_OBQ_TOON_DIFFUSE_FB_STR                     = 773295705,
   C4DAIP_OBQ_TOON_HIGHLIGHT_FB_STR                   = 1661936811,
   C4DAIP_OBQ_TOON_RIMLIGHT_FB_STR                    = 1827377491,
   C4DAIP_OBQ_TOON_CONTOUR_FB_STR                     = 1909435645,
   C4DAIP_OBQ_TOON_PUTALPHAINFB                       = 207774194,
   C4DAIP_OBQ_TOON_DIFFUSE_AUTOREMAP                  = 536869049,
   C4DAIP_OBQ_TOON_DIFFUSE_IMAGEREMAPLEFT             = 840951772,
   C4DAIP_OBQ_TOON_DIFFUSE_IMAGEREMAPRIGHT            = 1988864783,
   C4DAIP_OBQ_TOON_HIGHLIGHT_AUTOREMAP                = 1476711513,
   C4DAIP_OBQ_TOON_HIGHLIGHT_IMAGEREMAPLEFT           = 1473662930,
   C4DAIP_OBQ_TOON_HIGHLIGHT_IMAGEREMAPRIGHT          = 1378976351,
   C4DAIP_OBQ_TOON_RIMLIGHT_AUTOREMAP                 = 1611276287,
   C4DAIP_OBQ_TOON_RIMLIGHT_IMAGEREMAPLEFT            = 1084472106,
   C4DAIP_OBQ_TOON_RIMLIGHT_IMAGEREMAPRIGHT           = 1420581047,
   C4DAIP_OBQ_TOON_DIFFUSE_IMAGEREMAPBIAS             = 840596592,
   C4DAIP_OBQ_TOON_DIFFUSE_IMAGEREMAPGAIN             = 840767824,
   C4DAIP_OBQ_TOON_HIGHLIGHT_IMAGEREMAPBIAS           = 1474018110,
   C4DAIP_OBQ_TOON_HIGHLIGHT_IMAGEREMAPGAIN           = 1473846878,
   C4DAIP_OBQ_TOON_RIMLIGHT_IMAGEREMAPBIAS            = 1084827286,
   C4DAIP_OBQ_TOON_RIMLIGHT_IMAGEREMAPGAIN            = 1084656054,
   C4DAIP_OBQ_TOON_OUTPUT_IMAGEONUV                   = 881606577,
   C4DAIP_OBQ_TOON_OPACITY                            = 820813837,
   C4DAIP_OBQ_TOON_NORMALIZEOBJECTID                  = 1889090569,
   C4DAIP_OBQ_TOON_AMBIENT_NOINTERNAL                 = 2072803891,
   C4DAIP_OBQ_TOON_DIFFUSE_NOINTERNAL                 = 1394015405,
   C4DAIP_OBQ_TOON_HIGHLIGHT_NOINTERNAL               = 629633701,
   C4DAIP_OBQ_TOON_RIMLIGHT_NOINTERNAL                = 1805251405,
   C4DAIP_OBQ_TOON_DIFFUSE_LINEARDOT                  = 366491429,
   C4DAIP_OBQ_TOON_HIGHLIGHT_LINEARDOT                = 1647089133,
   C4DAIP_OBQ_TOON_RIMLIGHT_LINEARDOT                 = 1440898667,
   C4DAIP_OBQ_TOON_DIFFUSE_SHADERINPUT                = 309009664,
   C4DAIP_OBQ_TOON_HIGHLIGHT_SHADERINPUT              = 1630046574,
   C4DAIP_OBQ_TOON_GLOBAL_REMAPMODE                   = 1941851390,
   C4DAIP_OBQ_TOON_GLOBAL_REMAPMULTBYCOLOR            = 1841337579,
   C4DAIP_OBQ_TOON_GLOBAL_CLAMP                       = 602087281,
   C4DAIP_OBQ_TOON_NAME                               = 340226741,
};

#endif
