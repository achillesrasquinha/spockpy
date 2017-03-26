import os

ABSPATH_ROOT           = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ABSPATH_DATA           = os.path.join(ABSPATH_ROOT, 'data')
ABSPATH_MODELS         = os.path.join(ABSPATH_DATA, 'models')
ABSPATH_ENCODERS       = os.path.join(ABSPATH_DATA, 'encoders')

ABSPATH_ENCODER_DHCD   = os.path.join(ABSPATH_ENCODERS, 'DHCD-LE.pkl')

ABSPATH_MODEL_DHCD_SVC = os.path.join(ABSPATH_MODELS, 'DHCD-SVC-96.61,10-96.30,0.60.pkl')

DHCD_INPUT_SIZE        = (32, 32)
