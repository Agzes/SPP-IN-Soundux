from enum import Enum


from . import main
from . import blur
from . import meku



class THEME(Enum):
    BLUR = blur
    MAIN = main
    MEKU = meku
