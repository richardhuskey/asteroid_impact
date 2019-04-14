*************************
Compiling Asteroid Impact
*************************

Common Prequisites/Setup
========================

To only run the game python code, you need to install the following:

 * Python 2.7
 * PyGame 1.9.2 or later (available from pip)
 * pyserial (available from pip)

Other Prerequisites/Setup
=========================

The other requirements are:

 * pyinstaller (available from pip) is required to build standalone executables
 * sphinx (availabe from pip) is required to compile the documentation
 * 7-zip from http://www.7-zip.org/ is required to create release zip archives

Buidling Documentation
======================

To compile the documentation, from a command prompt with python 2.7 in your path ::

    > cd src\doc
    > make html

This puts the compiled HTML documentation in ``src\doc\_build\html``

Building Standalone Executable
==============================

To compile just the standalone executable, from a command prompt with python2.7 in your path::

    > cd src
    > mkdir dist
    > pyinstaller-build-windows.bat

The resulting exe, data files, and dlls are put in ``src\dist\game``

Building Release archives
=========================

To compile a source zip archive, a documentation zip archive, and standalone executable zip archive, from a command prompt with python2.7 and the 7z.exe from 7-Zip in your path ::

    > cd src
    > mkdir dist
    > makereleasewin.bat

The zip archives are put in the ``src\dist`` folder.

Please pay attention to the output of the batch file. There may be errors that didn't interrupt the build process.
