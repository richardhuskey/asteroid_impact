'''
Parallel port wrapper interface

Wraps the Windows inpout32.dll (or inpoutx64.dll) from
http://www.highrez.co.uk/downloads/inpout32/

These DLLs require the windows driver included with the download.
The driver works on both 32-bit and 64-bit Windows 10.

Last tested with 1.5.0.1 of InpOut32

The address of your parallel port can be found in the Windows Device Manager:
1. Open Device Manager. In Win10 you can right click on start button then press M
2. Locate your parallel port under Ports (COM & LPT). Open properties
3. On the Resources tab, the first entry in the first I/O range is the base address
    in hex. For example, "BF00-BF07" means the base port address is 0xBF00

https://en.wikipedia.org/wiki/Parallel_port#IBM_PC_Implementation
The address table shown on wikipedia shows which bits on the base address and
next two bytes correspond to which parallel port pins.
'''


import ctypes
import os
import platform

# to find inpout32.dll/inpoutx64.dll
# add current directory to PATH environment variable
os.environ['PATH'] =  os.environ['PATH'] + ';' + os.path.abspath(os.path.dirname(__file__))

class StubParallelPort:
    '''Stub parallel port implementation'''
    def __init__(self):
        pass
    def Inp32(addr):
        return 0
    def Out32(addr, data_byte):
        pass

try:
    dllfile = ''
    arch = platform.architecture()
    if arch == ('32bit', 'WindowsPE'):
        # 32-bit python on 32-bit or 64-bit Windows:
        dllfile = 'inpout32.dll'
        pport = ctypes.windll.inpout32
    elif arch == ('64bit', 'WindowsPE'):
        # 64-bit python on 64-bit Windows:
        dllfile = 'inpoutx64.dll'
        pport = ctypes.windll.inpoutx64
    else:
        print('WARNING: Parallel port support not available. Parallel port interface only implemented for Windows')
        pport = StubParallelPort()

except AttributeError as e:
    # ctypes.windll doesn't exist outside windows
    print(e)
    pport = StubParallelPort()
except WindowsError as e:
    # dll probably not found
    print(e)
    print(dllfile, 'not found. parallel port support is unavailable')
    pport = StubParallelPort()
except OSError as e:
    # probably running 64-bit python trying to load 32-bit DLL
    print(e)
    pport = StubParallelPort()

def Out32(port_addr, data_byte):
    pport.Out32(port_addr, data_byte)

def Inp32(port_addr):
    return pport.Inp32(port_addr)

