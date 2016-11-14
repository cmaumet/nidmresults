"""
Definition of constants.

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""

from prov.model import PROV, Namespace

NIDM = Namespace('nidm', "http://purl.org/nidash/nidm#")
NIIRI = Namespace("niiri", "http://iri.nidash.org/")
CRYPTO = Namespace(
    "crypto",
    "http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions#")
FSL = Namespace("fsl", "http://purl.org/nidash/fsl#")
SPM = Namespace("fsl", "http://purl.org/nidash/spm#")
DCT = Namespace("dct", "http://purl.org/dc/terms/")
OBO = Namespace("obo", "http://purl.obolibrary.org/obo/")
DCTYPE = Namespace("dctype", "http://purl.org/dc/dcmitype/")
NLX_OLD = Namespace("nlx_old", "http://neurolex.org/wiki/")
DC = Namespace("dc", "http://purl.org/dc/elements/1.1/")
NFO = Namespace(
    "nfo", "http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#")
SCR = Namespace("scr", "http://scicrunch.org/resolver/")
NIF = Namespace("nif", "http://uri.neuinfo.org/nif/nifstd/")

# Sciencrunch constants
SCR_FSL = SCR['SCR_002823']
SCR_SPM = SCR['SCR_007037']

# NeuroLex constants
NLX_OLD_FSL = NLX_OLD['birnlex_2067']
NIDM_FSL = NIDM.uri + 'NIDM_0000167'

# NIFSTD constants
NIF_MRI = NIF['birnlex_2100']
NIF_EEG = NIF['ixl_0050003']
NIF_MEG = NIF['ixl_0050002']
NIF_PET = NIF['ixl_0050000']
NIF_SPECT = NIF['ixl_0050001']
NLX_FMRI_PROTOCOL = NIF['birnlex_2250']

# NIDM constants
FSL_FSLS_GAMMA_HRF = FSL.uri + 'FSL_0000006'
NIDM_HAS_MRI_PROTOCOL = NIDM.uri + 'NIDM_0000172'
NIDM_NUMBER_OF_SUBJECTS = NIDM.uri + 'NIDM_0000171'
NIDM_GROUP_NAME = NIDM.uri + 'NIDM_0000170'
NIDM_DATA = NIDM.uri + 'NIDM_0000169'
NIDM_NIDM_RESULTS_EXPORT = NIDM.uri + 'NIDM_0000166'
FSL_FEAT_VERSION = FSL.uri + 'FSL_0000005'
FSL_DRIFT_CUTOFF_PERIOD = FSL.uri + 'FSL_0000004'
FSL_TEMPORAL_DERIVATIVE = FSL.uri + 'FSL_0000003'
FSL_GAUSSIAN_RUNNING_LINE_DRIFT_MODEL = FSL.uri + 'FSL_0000002'
FSL_FSLS_GAMMA_DIFFERENCE_HRF = FSL.uri + 'FSL_0000001'
NIDM_CONTRAST_EXPLAINED_MEAN_SQUARE_MAP = NIDM.uri + 'NIDM_0000163'
NIDM_THRESHOLD = NIDM.uri + 'NIDM_0000162'
NIDM_EQUIVALENT_THRESHOLD = NIDM.uri + 'NIDM_0000161'
NIDM_P_VALUE_UNCORRECTED_CLASS = NIDM.uri + 'NIDM_0000160'
NIDM_NOISE_FWHM_IN_VOXELS = NIDM.uri + 'NIDM_0000159'
NIDM_NOISE_FWHM_IN_VERTICES = NIDM.uri + 'NIDM_0000158'
NIDM_NOISE_FWHM_IN_UNITS = NIDM.uri + 'NIDM_0000157'
NIDM_CLUSTERSIZEINRESELS = NIDM.uri + 'NIDM_0000156'
NIDM_F_MRI_DESIGN = NIDM.uri + 'NIDM_0000155'
NIDM_MIXED_DESIGN = NIDM.uri + 'NIDM_0000154'
NIDM_EVENT_RELATED_DESIGN = NIDM.uri + 'NIDM_0000153'
NIDM_BLOCK_BASED_DESIGN = NIDM.uri + 'NIDM_0000152'
NIDM_SINE_BASIS_SET = NIDM.uri + 'NIDM_0000151'
NIDM_LINEAR_SPLINE_BASIS_SET = NIDM.uri + 'NIDM_0000150'
NIDM_SEARCH_VOLUME_IN_RESELS = NIDM.uri + 'NIDM_0000149'
NIDM_RESEL_SIZE_IN_VOXELS = NIDM.uri + 'NIDM_0000148'
NIDM_HEIGHT_CRITICAL_THRESHOLD_FWE_05 = NIDM.uri + 'NIDM_0000147'
NIDM_HEIGHT_CRITICAL_THRESHOLD_FDR_05 = NIDM.uri + 'NIDM_0000146'
NIDM_NOISE_ROUGHNESS_IN_VOXELS = NIDM.uri + 'NIDM_0000145'
NIDM_RESELS_PER_VOXEL_MAP = NIDM.uri + 'NIDM_0000144'
NIDM_EXPECTED_NUMBER_OF_VOXELS_PER_CLUSTER = NIDM.uri + 'NIDM_0000143'
NIDM_EXPECTED_NUMBER_OF_VERTICES_PER_CLUSTER = NIDM.uri + 'NIDM_0000142'
NIDM_EXPECTED_NUMBER_OF_CLUSTERS = NIDM.uri + 'NIDM_0000141'
NIDM_CLUSTER_CENTER_OF_GRAVITY = NIDM.uri + 'NIDM_0000140'
NIDM_COORDINATE_VECTOR_IN_VOXELS = NIDM.uri + 'NIDM_0000139'
NIDM_HAS_MAXIMUM_INTENSITY_PROJECTION = NIDM.uri + 'NIDM_0000138'
NIDM_SEARCH_VOLUME_IN_VERTICES = NIDM.uri + 'NIDM_0000137'
NIDM_SEARCH_VOLUME_IN_UNITS = NIDM.uri + 'NIDM_0000136'
NIDM_CONTRAST_VARIANCE_MAP = NIDM.uri + 'NIDM_0000135'
NIDM_WITH_ESTIMATION_METHOD = NIDM.uri + 'NIDM_0000134'
NIDM_VOXEL_UNITS = NIDM.uri + 'NIDM_0000133'
NIDM_VOXEL_TO_WORLD_MAPPING = NIDM.uri + 'NIDM_0000132'
NIDM_VOXEL_SIZE = NIDM.uri + 'NIDM_0000131'
NIDM_VOXEL6CONNECTED = NIDM.uri + 'NIDM_0000130'
NIDM_VOXEL26CONNECTED = NIDM.uri + 'NIDM_0000129'
NIDM_VOXEL18CONNECTED = NIDM.uri + 'NIDM_0000128'
NIDM_VERSION = NIDM.uri + 'NIDM_0000127'
NIDM_VARIANCE_SPATIAL_MODEL = NIDM.uri + 'NIDM_0000126'
NIDM_USER_SPECIFIED_THRESHOLD_TYPE = NIDM.uri + 'NIDM_0000125'
NIDM_TARGET_INTENSITY = NIDM.uri + 'NIDM_0000124'
NIDM_STATISTIC_TYPE = NIDM.uri + 'NIDM_0000123'
NIDM_SOFTWARE_VERSION = NIDM.uri + 'NIDM_0000122'
NIDM_SEARCH_VOLUME_IN_VOXELS = NIDM.uri + 'NIDM_0000121'
NIDM_RANDOM_FIELD_STATIONARITY = NIDM.uri + 'NIDM_0000120'
NIDM_Q_VALUE_FDR = NIDM.uri + 'NIDM_0000119'
NIDM_PIXEL8CONNECTED = NIDM.uri + 'NIDM_0000118'
NIDM_PIXEL4CONNECTED = NIDM.uri + 'NIDM_0000117'
NIDM_P_VALUE_UNCORRECTED = NIDM.uri + 'NIDM_0000116'
NIDM_P_VALUE_FWER = NIDM.uri + 'NIDM_0000115'
NIDM_P_VALUE = NIDM.uri + 'NIDM_0000114'
NIDM_OBJECT_MODEL = NIDM.uri + 'NIDM_0000113'
NIDM_NUMBER_OF_DIMENSIONS = NIDM.uri + 'NIDM_0000112'
NIDM_NUMBER_OF_CLUSTERS = NIDM.uri + 'NIDM_0000111'
NIDM_GAUSSIAN_HRF = NIDM.uri + 'NIDM_0000110'
NIDM_MIN_DISTANCE_BETWEEN_PEAKS = NIDM.uri + 'NIDM_0000109'
NIDM_MAX_NUMBER_OF_PEAKS_PER_CLUSTER = NIDM.uri + 'NIDM_0000108'
NIDM_MASKED_MEDIAN = NIDM.uri + 'NIDM_0000107'
NIDM_IS_USER_DEFINED = NIDM.uri + 'NIDM_0000106'
NIDM_IN_WORLD_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000105'
NIDM_IN_COORDINATE_SPACE = NIDM.uri + 'NIDM_0000104'
NIDM_HAS_MAP_HEADER = NIDM.uri + 'NIDM_0000103'
NIDM_HAS_HRF_BASIS = NIDM.uri + 'NIDM_0000102'
NIDM_HAS_ERROR_DISTRIBUTION = NIDM.uri + 'NIDM_0000101'
NIDM_HAS_ERROR_DEPENDENCE = NIDM.uri + 'NIDM_0000100'
NIDM_HAS_CONNECTIVITY_CRITERION = NIDM.uri + 'NIDM_0000099'
NIDM_HAS_CLUSTER_LABELS_MAP = NIDM.uri + 'NIDM_0000098'
NIDM_HAS_ALTERNATIVE_HYPOTHESIS = NIDM.uri + 'NIDM_0000097'
NIDM_GRAND_MEAN_SCALING = NIDM.uri + 'NIDM_0000096'
NIDM_GLOBAL_NULL_DEGREE = NIDM.uri + 'NIDM_0000095'
NIDM_ERROR_VARIANCE_HOMOGENEOUS = NIDM.uri + 'NIDM_0000094'
NIDM_ERROR_DEGREES_OF_FREEDOM = NIDM.uri + 'NIDM_0000093'
NIDM_EQUIVALENT_ZSTATISTIC = NIDM.uri + 'NIDM_0000092'
NIDM_EFFECT_DEGREES_OF_FREEDOM = NIDM.uri + 'NIDM_0000091'
NIDM_DIMENSIONS_IN_VOXELS = NIDM.uri + 'NIDM_0000090'
NIDM_DEPENDENCE_SPATIAL_MODEL = NIDM.uri + 'NIDM_0000089'
NIDM_HAS_DRIFT_MODEL = NIDM.uri + 'NIDM_0000088'
NIDM_DRIFT_MODEL = NIDM.uri + 'NIDM_0000087'
NIDM_COORDINATE_VECTOR = NIDM.uri + 'NIDM_0000086'
NIDM_CONTRAST_NAME = NIDM.uri + 'NIDM_0000085'
NIDM_CLUSTER_SIZE_IN_VOXELS = NIDM.uri + 'NIDM_0000084'
NIDM_CLUSTER_SIZE_IN_VERTICES = NIDM.uri + 'NIDM_0000083'
NIDM_CLUSTER_LABEL_ID = NIDM.uri + 'NIDM_0000082'
NIDM_WORLD_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000081'
NIDM_VOXEL_CONNECTIVITY_CRITERION = NIDM.uri + 'NIDM_0000080'
NIDM_TWO_TAILED_TEST = NIDM.uri + 'NIDM_0000079'
NIDM_TALAIRACH_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000078'
NIDM_SUBJECT_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000077'
NIDM_STATISTIC_MAP = NIDM.uri + 'NIDM_0000076'
NIDM_STANDARDIZED_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000075'
NIDM_SPATIALLY_REGULARIZED_MODEL = NIDM.uri + 'NIDM_0000074'
NIDM_SPATIALLY_LOCAL_MODEL = NIDM.uri + 'NIDM_0000073'
NIDM_SPATIALLY_GLOBAL_MODEL = NIDM.uri + 'NIDM_0000072'
NIDM_SPATIAL_MODEL = NIDM.uri + 'NIDM_0000071'
NIDM_SIGNIFICANT_CLUSTER = NIDM.uri + 'NIDM_0000070'
NIDM_FOURIER_BASIS_SET = NIDM.uri + 'NIDM_0000069'
NIDM_SEARCH_SPACE_MASK_MAP = NIDM.uri + 'NIDM_0000068'
NIDM_CUSTOM_BASIS_SET = NIDM.uri + 'NIDM_0000067'
NIDM_RESIDUAL_MEAN_SQUARES_MAP = NIDM.uri + 'NIDM_0000066'
NIDM_POISSON_DISTRIBUTION = NIDM.uri + 'NIDM_0000065'
NIDM_PIXEL_CONNECTIVITY_CRITERION = NIDM.uri + 'NIDM_0000064'
NIDM_PEAK_DEFINITION_CRITERIA = NIDM.uri + 'NIDM_0000063'
NIDM_PEAK = NIDM.uri + 'NIDM_0000062'
NIDM_PARAMETER_ESTIMATE_MAP = NIDM.uri + 'NIDM_0000061'
NIDM_ONE_TAILED_TEST = NIDM.uri + 'NIDM_0000060'
NIDM_NON_PARAMETRIC_SYMMETRIC_DISTRIBUTION = NIDM.uri + 'NIDM_0000059'
NIDM_NON_PARAMETRIC_DISTRIBUTION = NIDM.uri + 'NIDM_0000058'
NIDM.uri + 'NIDM_OBJECT_MODEL = NIDM_NIDM_0000057'
NIDM_MODEL_PARAMETERS_ESTIMATION = NIDM.uri + 'NIDM_0000056'
NIDM_MNI305_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000055'
NIDM_MASK_MAP = NIDM.uri + 'NIDM_0000054'
NIDM_MAP_HEADER = NIDM.uri + 'NIDM_0000053'
NIDM_MAP = NIDM.uri + 'NIDM_0000052'
NIDM_MNI_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000051'
NIDM_IXI549_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000050'
NIDM_INFERENCE = NIDM.uri + 'NIDM_0000049'
NIDM_INDEPENDENT_ERROR = NIDM.uri + 'NIDM_0000048'
NIDM_ICBM_MNI152_NON_LINEAR6TH_GENERATION_COORDINATE_SYSTEM = \
    NIDM.uri + 'NIDM_0000047'
NIDM_ICBM_MNI152_NON_LINEAR2009C_SYMMETRIC_COORDINATE_SYSTEM = \
    NIDM.uri + 'NIDM_0000046'
NIDM_ICBM_MNI152_NON_LINEAR2009C_ASYMMETRIC_COORDINATE_SYSTEM = \
    NIDM.uri + 'NIDM_0000045'
NIDM_ICBM_MNI152_NON_LINEAR2009B_SYMMETRIC_COORDINATE_SYSTEM = \
    NIDM.uri + 'NIDM_0000044'
NIDM_ICBM_MNI152_NON_LINEAR2009B_ASYMMETRIC_COORDINATE_SYSTEM = \
    NIDM.uri + 'NIDM_0000043'
NIDM_ICBM_MNI152_NON_LINEAR2009A_SYMMETRIC_COORDINATE_SYSTEM = \
    NIDM.uri + 'NIDM_0000042'
NIDM_ICBM_MNI152_NON_LINEAR2009A_ASYMMETRIC_COORDINATE_SYSTEM = \
    NIDM.uri + 'NIDM_0000041'
NIDM_ICBM_MNI152_LINEAR_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000040'
NIDM_ICBM452_WARP5_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000039'
NIDM_ICBM452_AIR_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000038'
NIDM_HEMODYNAMIC_RESPONSE_FUNCTION_DERIVATIVE = NIDM.uri + 'NIDM_0000037'
NIDM_HEMODYNAMIC_RESPONSE_FUNCTION_BASIS = NIDM.uri + 'NIDM_0000036'
NIDM_HEMODYNAMIC_RESPONSE_FUNCTION = NIDM.uri + 'NIDM_0000035'
NIDM_HEIGHT_THRESHOLD = NIDM.uri + 'NIDM_0000034'
NIDM_GRAND_MEAN_MAP = NIDM.uri + 'NIDM_0000033'
NIDM_GAUSSIAN_DISTRIBUTION = NIDM.uri + 'NIDM_0000032'
NIDM_GAMMA_HRF = NIDM.uri + 'NIDM_0000031'
NIDM_GAMMA_HRB = NIDM.uri + 'NIDM_0000030'
NIDM_GAMMA_DIFFERENCE_HRF = NIDM.uri + 'NIDM_0000029'
NIDM_FINITE_IMPULSE_RESPONSE_HRB = NIDM.uri + 'NIDM_0000028'
NIDM_RESULTS = NIDM.uri + 'NIDM_0000027'
NIDM_EXTENT_THRESHOLD = NIDM.uri + 'NIDM_0000026'
NIDM_EXCURSION_SET_MAP = NIDM.uri + 'NIDM_0000025'
NIDM_EXCHANGEABLE_ERROR = NIDM.uri + 'NIDM_0000024'
NIDM_ERROR_MODEL = NIDM.uri + 'NIDM_0000023'
NIDM_ERROR_DISTRIBUTION = NIDM.uri + 'NIDM_0000022'
NIDM_REGRESSOR_NAMES = NIDM.uri + 'NIDM_0000021'
NIDM_DISPLAY_MASK_MAP = NIDM.uri + 'NIDM_0000020'
NIDM_DESIGN_MATRIX = NIDM.uri + 'NIDM_0000019'
NIDM_DATA_SCALING = NIDM.uri + 'NIDM_0000018'
NIDM_CUSTOM_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000017'
NIDM_COORDINATE_SPACE = NIDM.uri + 'NIDM_0000016'
NIDM_COORDINATE = NIDM.uri + 'NIDM_0000015'
NIDM_LEGENDRE_POLYNOMIAL_ORDER = NIDM.uri + 'NIDM_0000014'
NIDM_CONTRAST_STANDARD_ERROR_MAP = NIDM.uri + 'NIDM_0000013'
NIDM_CONNECTIVITY_CRITERION = NIDM.uri + 'NIDM_0000012'
NIDM_CONJUNCTION_INFERENCE = NIDM.uri + 'NIDM_0000011'
NIDM_HAS_FMRI_DESIGN = NIDM.uri + 'NIDM_0000010'
NIDM_COLIN27_COORDINATE_SYSTEM = NIDM.uri + 'NIDM_0000009'
NIDM_CLUSTER_LABELS_MAP = NIDM.uri + 'NIDM_0000008'
NIDM_CLUSTER_DEFINITION_CRITERIA = NIDM.uri + 'NIDM_0000007'
NIDM_CLUSTER = NIDM.uri + 'NIDM_0000006'
NIDM_BINOMIAL_DISTRIBUTION = NIDM.uri + 'NIDM_0000005'
NIDM_BINARY_MAP = NIDM.uri + 'NIDM_0000004'
NIDM_ARBITRARILY_CORRELATED_ERROR = NIDM.uri + 'NIDM_0000003'
NIDM_CONTRAST_ESTIMATION = NIDM.uri + 'NIDM_0000001'
NIDM_CONTRAST_MAP = NIDM.uri + 'NIDM_0000002'

STATO_OLS = OBO.uri + 'STATO_0000370'
STATO_WLS = OBO.uri + 'STATO_0000371'
STATO_GLS = OBO.uri + 'STATO_0000372'
STATO_TSTATISTIC = OBO.uri + 'STATO_0000176'
STATO_ZSTATISTIC = OBO.uri + 'STATO_0000376'
STATO_FSTATISTIC = OBO.uri + 'STATO_0000282'
STATO_CONTRAST_WEIGHT_MATRIX = OBO.uri + 'STATO_0000323'
STATO_NORMAL_DISTRIBUTION = OBO.uri + 'STATO_0000227'
STATO_GROUP = OBO.uri + 'STATO_0000193'

OBO_STATISTIC = OBO.uri + 'STATO_0000039'
OBO_P_VALUE_FWER = OBO.uri + 'OBI_0001265'
OBO_Q_VALUE_FDR = OBO.uri + 'OBI_0001442'

NIDM_INDEPEDENT_ERROR = NIDM.uri + 'NIDM_0000048'
OBO_SERIALLY_CORR_COV = OBO.uri + 'STATO_0000357'
OBO_COMPOUND_SYMMETRY_COV = OBO.uri + 'STATO_0000362'
OBO_UNSTRUCTURED_COV = OBO.uri + 'STATO_0000405'

SPATIALLY_GLOBAL = NIDM_SPATIALLY_GLOBAL_MODEL
SPATIALLY_LOCAL = NIDM_SPATIALLY_LOCAL_MODEL
SPATIALLY_REGUL = NIDM_SPATIALLY_REGULARIZED_MODEL

SPATIAL_DEPENDENCY_ENUM = (
    SPATIALLY_GLOBAL,
    SPATIALLY_LOCAL,
    SPATIALLY_REGUL
)
