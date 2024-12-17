import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    import safeum_enc.cpython-311.so
elif bit == '32bit':
    import safeum_enc.cpython-311.so
