from constants import *

class Parameters:
    num_lanes = [    8, # AVX 512
                    32, # ARM SVE 2048
                   128, # something in between
                 ]
    page_size_bytes = [4 * oneKiB, 2 * oneMiB]
    element_size_bytes = [8 # double precision
                         ]
