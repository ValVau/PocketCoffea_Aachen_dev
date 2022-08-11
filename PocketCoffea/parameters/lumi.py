import os

# Function to convert and round the integrated luminosity from picobarn to femtobarn
def femtobarn(picobarn, digits=None):
    if round:
        return round((picobarn)/1000., digits)
    else:
        return picobarn/1000.

# Integrated luminosity [pb^-1] for each data-taking year

"""
lumi = {
    "2016" : 36773.0,
    "2017" : 41529.0,
    "2018" : 58830.0,
}
"""

lumi = {
    "2017": {
        "B": 4803.371586,
        "C": 9574.029838,
        "D": 4247.792714,
        "E": 9314.581016,
        "F": 13539.905374,
        "tot": 41479.680527999996
    },
    "2018": {
        "A": 14027.614284,
        "B": 7066.552169,
        "C": 6898.816878,
        "D": 31839.492009,
        "tot": 59832.47534
    },
}


goldenJSON = {
    "2016_PreVFP" : os.path.join(os.getcwd(), "PocketCoffea/parameters/datacert/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt"),
    "2016_PostVFP" : os.path.join(os.getcwd(), "PocketCoffea/parameters/datacert/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt"),
    "2017" : os.path.join(os.getcwd(), "PocketCoffea/parameters/datacert/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt"),
    "2018" : os.path.join(os.getcwd(), "PocketCoffea/parameters/datacert/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"),
}

runs = {
    "SingleMuon" : {
        "2016_PreVFP" : {
            "B-ver1" : [272760, 272761, 272762, 272774, 272775, 272776, 272782, 272783, 272784, 272785, 272786, 272798, 272811, 272812, 272815, 272816, 272818, 272827, 272828, 272930, 272936, 273013, 273017],
            "B-ver2" : [273150, 273158, 273290, 273291, 273292, 273294, 273295, 273299, 273301, 273302, 273402, 273403, 273404, 273405, 273406, 273407, 273408, 273409, 273410, 273411, 273425, 273426, 273445, 273446, 273447, 273448, 273449, 273450, 273492, 273493, 273494, 273502, 273503, 273523, 273526, 273537, 273554, 273555, 273589, 273590, 273592, 273725, 273728, 273730, 274094, 274102, 274103, 274104, 274105, 274106, 274107, 274108, 274142, 274146, 274157, 274159, 274160, 274161, 274172, 274198, 274199, 274200, 274240, 274241, 274244, 274250, 274251, 274282, 274283, 274284, 274285, 274286, 274314, 274315, 274316, 274317, 274318, 274319, 274335, 274336, 274337, 274338, 274339, 274344, 274345, 274382, 274387, 274388, 274420, 274421, 274422, 274440, 274441, 274442, 274443, 274954, 274955, 274957, 274958, 274959, 274967, 274968, 274969, 274970, 274971, 274998, 274999, 275000, 275001, 275059, 275062, 275063, 275064, 275066, 275067, 275068, 275073, 275074, 275124, 275125, 275282, 275283, 275284, 275285, 275286, 275289, 275290, 275291, 275292, 275293, 275309, 275310, 275311, 275319, 275337, 275338, 275344, 275345, 275370, 275371, 275375, 275376],
            "C" : [275656, 275657, 275658, 275659, 275757, 275758, 275759, 275761, 275763, 275764, 275766, 275767, 275768, 275772, 275773, 275774, 275776, 275777, 275778, 275781, 275782, 275828, 275829, 275831, 275832, 275833, 275834, 275835, 275836, 275837, 275841, 275846, 275847, 275886, 275887, 275890, 275911, 275912, 275913, 275918, 275920, 275921, 275922, 275923, 275931, 275963, 276062, 276063, 276064, 276092, 276095, 276097, 276242, 276243, 276244, 276282, 276283],
            "D" : [276315, 276317, 276318, 276326, 276327, 276352, 276355, 276357, 276361, 276363, 276384, 276437, 276453, 276454, 276458, 276495, 276501, 276502, 276525, 276527, 276528, 276542, 276543, 276544, 276545, 276581, 276582, 276583, 276584, 276585, 276586, 276587, 276653, 276655, 276659, 276775, 276776, 276794, 276807, 276808, 276810, 276811],
            "E" : [276831, 276832, 276834, 276836, 276837, 276870, 276935, 276940, 276941, 276942, 276944, 276945, 276946, 276947, 276948, 276950, 277069, 277070, 277071, 277072, 277073, 277075, 277076, 277087, 277093, 277094, 277096, 277112, 277126, 277127, 277148, 277166, 277168, 277180, 277194, 277202, 277217, 277218, 277219, 277220, 277305, 277420],
            "F" : [277932, 277934, 277981, 277991, 277992, 278017, 278018, 278167, 278175, 278193, 278239, 278240, 278273, 278274, 278288, 278289, 278290, 278308, 278309, 278310, 278315, 278345, 278346, 278349, 278366, 278406, 278509, 278761, 278770, 278806, 278807]
        },
        "2016_PostVFP" : {
            "F" : [278769, 278801, 278802, 278803, 278804, 278805, 278808],
            "G" : [278820, 278821, 278822, 278873, 278874, 278875, 278923, 278957, 278962, 278963, 278969, 278975, 278976, 278986, 279024, 279029, 279071, 279080, 279115, 279116, 279479, 279480, 279488, 279489, 279588, 279653, 279654, 279656, 279658, 279667, 279681, 279682, 279683, 279684, 279685, 279691, 279694, 279715, 279716, 279760, 279766, 279767, 279794, 279823, 279841, 279844, 279887, 279931, 279966, 279975, 279993, 279994, 279995, 280002, 280006, 280007, 280013, 280014, 280015, 280016, 280017, 280018, 280019, 280020, 280021, 280022, 280023, 280024, 280187, 280188, 280189, 280190, 280191, 280194, 280242, 280249, 280251, 280327, 280330, 280349, 280363, 280364, 280383, 280384, 280385],
            "H" : [281613, 281616, 281638, 281639, 281641, 281663, 281674, 281680, 281686, 281689, 281691, 281693, 281707, 281726, 281727, 281797, 281974, 281975, 281976, 282033, 282034, 282035, 282037, 282092, 282663, 282707, 282708, 282710, 282711, 282712, 282730, 282731, 282732, 282733, 282734, 282735, 282800, 282807, 282814, 282842, 282917, 282918, 282919, 282922, 282923, 282924, 283042, 283043, 283049, 283050, 283052, 283059, 283270, 283283, 283305, 283306, 283307, 283308, 283353, 283358, 283359, 283407, 283408, 283413, 283415, 283416, 283453, 283469, 283478, 283548, 283672, 283675, 283676, 283680, 283681, 283682, 283685, 283820, 283830, 283834, 283835, 283863, 283865, 283876, 283877, 283884, 283885, 283933, 283934, 283946, 283964, 284006, 284014, 284025, 284029, 284035, 284036, 284037, 284038, 284039, 284040, 284041, 284042, 284043, 284044]
        },
        "2017" : {
            "B" : [297047, 297050, 297056, 297057, 297099, 297100, 297101, 297113, 297114, 297168, 297169, 297170, 297171, 297175, 297176, 297177, 297178, 297179, 297180, 297181, 297211, 297215, 297218, 297219, 297224, 297225, 297227, 297281, 297286, 297292, 297293, 297296, 297308, 297359, 297411, 297424, 297425, 297426, 297429, 297430, 297431, 297432, 297433, 297434, 297435, 297467, 297468, 297469, 297474, 297483, 297484, 297485, 297486, 297487, 297488, 297503, 297504, 297505, 297557, 297558, 297562, 297563, 297598, 297599, 297603, 297604, 297605, 297606, 297620, 297656, 297659, 297660, 297664, 297665, 297666, 297670, 297671, 297672, 297674, 297675, 297678, 297722, 297723, 298678, 298996, 298997, 298998, 299000, 299042, 299061, 299062, 299064, 299065, 299067, 299096, 299149, 299178, 299180, 299184, 299185, 299316, 299317, 299318, 299324, 299325, 299326, 299327, 299329],
            "C" : [299368, 299369, 299370, 299380, 299381, 299394, 299395, 299396, 299420, 299443, 299450, 299477, 299478, 299479, 299480, 299481, 299592, 299593, 299594, 299595, 299597, 299614, 299616, 299617, 299649, 300079, 300087, 300105, 300106, 300107, 300117, 300122, 300123, 300124, 300155, 300156, 300157, 300226, 300233, 300234, 300235, 300236, 300237, 300238, 300239, 300240, 300280, 300281, 300282, 300283, 300284, 300364, 300365, 300366, 300367, 300368, 300369, 300370, 300371, 300372, 300373, 300374, 300375, 300389, 300390, 300391, 300392, 300393, 300394, 300395, 300396, 300397, 300398, 300399, 300400, 300401, 300459, 300461, 300462, 300463, 300464, 300466, 300467, 300497, 300498, 300499, 300500, 300514, 300515, 300516, 300517, 300538, 300539, 300545, 300548, 300551, 300552, 300558, 300560, 300574, 300575, 300576, 300631, 300632, 300633, 300635, 300636, 300673, 300674, 300675, 300676, 300742, 300777, 300780, 300785, 300806, 300811, 300812, 300816, 300817, 301046, 301086, 301141, 301142, 301161, 301165, 301179, 301180, 301183, 301281, 301283, 301298, 301323, 301330, 301359, 301383, 301384, 301391, 301392, 301393, 301394, 301395, 301396, 301397, 301398, 301399, 301417, 301447, 301448, 301449, 301450, 301461, 301472, 301473, 301474, 301475, 301476, 301480, 301519, 301524, 301525, 301526, 301528, 301529, 301530, 301531, 301532, 301567, 301627, 301664, 301665, 301694, 301912, 301913, 301914, 301941, 301959, 301960, 301969, 301970, 301984, 301985, 301986, 301987, 301997, 301998, 302019, 302026, 302029],
            "D" : [302031, 302033, 302034, 302036, 302037, 302038, 302040, 302041, 302042, 302043, 302131, 302159, 302163, 302165, 302166, 302225, 302228, 302229, 302239, 302240, 302262, 302263, 302277, 302279, 302280, 302322, 302328, 302337, 302342, 302343, 302344, 302349, 302350, 302388, 302392, 302393, 302448, 302472, 302473, 302474, 302475, 302476, 302479, 302484, 302485, 302486, 302487, 302488, 302490, 302491, 302492, 302493, 302494, 302509, 302513, 302522, 302523, 302524, 302525, 302526, 302548, 302550, 302551, 302553, 302554, 302555, 302563, 302564, 302565, 302566, 302567, 302570, 302571, 302572, 302573, 302596, 302597, 302634, 302635, 302646, 302651, 302654, 302660, 302661, 302663],
            "E" : [303824, 303825, 303832, 303838, 303885, 303948, 303989, 303998, 303999, 304000, 304062, 304119, 304120, 304125, 304144, 304158, 304169, 304170, 304196, 304197, 304198, 304199, 304200, 304204, 304209, 304291, 304292, 304333, 304354, 304366, 304446, 304447, 304448, 304449, 304451, 304452, 304505, 304506, 304507, 304508, 304562, 304616, 304625, 304626, 304654, 304655, 304661, 304662, 304663, 304671, 304672, 304737, 304738, 304739, 304740, 304776, 304777, 304778, 304797],
            "F" : [305040, 305043, 305044, 305045, 305046, 305059, 305062, 305063, 305064, 305081, 305112, 305113, 305114, 305178, 305179, 305180, 305181, 305182, 305183, 305184, 305185, 305186, 305188, 305202, 305204, 305207, 305208, 305234, 305235, 305236, 305237, 305247, 305248, 305249, 305250, 305252, 305282, 305310, 305311, 305312, 305313, 305314, 305336, 305338, 305341, 305349, 305350, 305351, 305358, 305364, 305365, 305366, 305376, 305377, 305405, 305406, 305440, 305441, 305516, 305517, 305518, 305586, 305588, 305589, 305590, 305636, 305766, 305809, 305814, 305821, 305832, 305840, 305841, 305842, 305862, 305898, 305902, 305967, 306029, 306030, 306036, 306037, 306038, 306041, 306042, 306048, 306049, 306051, 306091, 306092, 306093, 306095, 306121, 306122, 306125, 306126, 306134, 306135, 306137, 306138, 306139, 306153, 306154, 306155, 306169, 306170, 306171, 306417, 306418, 306419, 306420, 306422, 306423, 306425, 306432, 306454, 306455, 306456, 306457, 306458, 306459, 306460, 306462]
        },
        "2018" : {
            "A" : [315257, 315258, 315259, 315264, 315265, 315267, 315270, 315322, 315339, 315357, 315361, 315363, 315365, 315366, 315420, 315488, 315489, 315490, 315506, 315509, 315510, 315512, 315543, 315555, 315556, 315557, 315640, 315641, 315642, 315644, 315645, 315646, 315647, 315648, 315689, 315690, 315702, 315703, 315704, 315705, 315713, 315721, 315741, 315764, 315770, 315784, 315785, 315786, 315788, 315789, 315790, 315800, 315801, 315840, 315973, 315974, 316058, 316059, 316060, 316061, 316062, 316082, 316109, 316110, 316111, 316112, 316113, 316114, 316151, 316153, 316186, 316187, 316199, 316200, 316201, 316202, 316216, 316217, 316218, 316219, 316239, 316240, 316241, 316271, 316361, 316362, 316363, 316377, 316378, 316379, 316380, 316455, 316456, 316457, 316469, 316470, 316472, 316505, 316569, 316590, 316613, 316615, 316664, 316665, 316666, 316667, 316700, 316701, 316702, 316715, 316716, 316717, 316718, 316719, 316720, 316721, 316722, 316723, 316758, 316766, 316876, 316877, 316879, 316928, 316944, 316985, 316993, 316994, 316995],
            "B" : [317080, 317087, 317088, 317089, 317182, 317212, 317213, 317279, 317291, 317292, 317295, 317296, 317297, 317319, 317320, 317338, 317339, 317340, 317382, 317383, 317391, 317392, 317434, 317435, 317438, 317475, 317478, 317479, 317480, 317481, 317482, 317484, 317488, 317509, 317510, 317511, 317512, 317527, 317591, 317626, 317640, 317641, 317648, 317649, 317650, 317661, 317663, 317683, 317696, 318733, 318816, 318819, 318820, 318828, 318872, 318874, 318876, 318877, 318944, 319077, 319310],
            "C" : [319337, 319347, 319348, 319349, 319449, 319450, 319456, 319459, 319486, 319503, 319524, 319526, 319528, 319579, 319625, 319639, 319656, 319657, 319658, 319659, 319678, 319687, 319697, 319698, 319756, 319840, 319841, 319847, 319848, 319849, 319851, 319852, 319853, 319854, 319908, 319909, 319910, 319912, 319913, 319914, 319915, 319941, 319942, 319950, 319991, 319992, 319993, 320002, 320006, 320007, 320008, 320009, 320010, 320011, 320012, 320023, 320024, 320025, 320026, 320038, 320039, 320040, 320058, 320059, 320060, 320061, 320062, 320063, 320064, 320065],
            "D" : [320500, 320569, 320570, 320571, 320673, 320674, 320688, 320712, 320757, 320804, 320807, 320809, 320821, 320822, 320823, 320824, 320838, 320840, 320841, 320853, 320854, 320855, 320856, 320857, 320858, 320859, 320887, 320888, 320916, 320917, 320920, 320933, 320934, 320936, 320941, 320980, 320995, 320996, 321004, 321005, 321006, 321007, 321009, 321010, 321011, 321012, 321051, 321055, 321067, 321068, 321069, 321119, 321121, 321122, 321123, 321124, 321126, 321134, 321138, 321140, 321149, 321162, 321164, 321165, 321166, 321167, 321177, 321178, 321218, 321219, 321221, 321230, 321231, 321232, 321233, 321261, 321262, 321283, 321294, 321295, 321296, 321305, 321310, 321311, 321312, 321313, 321393, 321396, 321397, 321414, 321415, 321431, 321432, 321433, 321434, 321436, 321457, 321461, 321475, 321709, 321710, 321712, 321730, 321731, 321732, 321735, 321755, 321758, 321759, 321760, 321773, 321774, 321775, 321776, 321777, 321778, 321780, 321781, 321794, 321796, 321813, 321815, 321817, 321818, 321819, 321820, 321831, 321832, 321833, 321834, 321879, 321880, 321887, 321908, 321909, 321917, 321919, 321933, 321960, 321961, 321973, 321975, 321988, 321990, 322013, 322014, 322022, 322040, 322057, 322068, 322079, 322088, 322106, 322113, 322118, 322179, 322201, 322204, 322222, 322252, 322317, 322319, 322322, 322324, 322332, 322348, 322355, 322356, 322381, 322407, 322430, 322431, 322480, 322483, 322484, 322485, 322487, 322492, 322510, 322599, 322602, 322603, 322605, 322616, 322617, 322625, 322633, 323413, 323414, 323416, 323417, 323418, 323419, 323420, 323421, 323422, 323423, 323470, 323471, 323472, 323473, 323474, 323475, 323487, 323488, 323492, 323493, 323495, 323524, 323525, 323526, 323693, 323696, 323702, 323725, 323726, 323727, 323755, 323775, 323778, 323790, 323794, 323841, 323857, 323940, 323954, 323976, 323978, 323980, 323983, 323997, 324021, 324022, 324077, 324201, 324202, 324205, 324206, 324207, 324209, 324237, 324245, 324293, 324315, 324318, 324420, 324564, 324570, 324571, 324729, 324747, 324764, 324765, 324769, 324772, 324785, 324791, 324835, 324840, 324841, 324846, 324878, 324897, 324970, 324980, 324997, 324998, 324999, 325000, 325001, 325022, 325057, 325097, 325098, 325099, 325100, 325101, 325110, 325111, 325113, 325114, 325117, 325159, 325168, 325169, 325170, 325172, 325175]
        }
    }
}
