import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    import safeumm
elif bit == '32bit':
    import safeumm