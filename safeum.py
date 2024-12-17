import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    import safeum_enc
elif bit == '32bit':
    import safeum_enc