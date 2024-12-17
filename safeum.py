import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    import safeum.
elif bit == '32bit':
    import safeum.