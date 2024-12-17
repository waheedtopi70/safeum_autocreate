import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    import SafeUM
elif bit == '32bit':
    import SafeUM