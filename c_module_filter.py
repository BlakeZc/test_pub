import os
import ctypes
ctypes.CDLL(os.path.join(os.getcwd(),"dlopen_hook.so"))
