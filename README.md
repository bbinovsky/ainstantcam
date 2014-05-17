ainstantcam
===========

ASCII Instant Camera

Author: Brian Binovsky
Date:   5-17-2014

Requirements:

  Windows XP - 8.1
     Probably works in Linux with slight alterations.  On OSX there are driver issues.
  Playstation 3 Eye Camera
     As tested, other cameras will work with acceptable Windows drivers.
  Code Laboratories CL Eye driver
     http://codelaboratories.com/products/eye/driver/ button on lower right to download.
  Python Video Capture libraries for Windows
     http://videocapture.sourceforge.net/
  Python 2.7.6 for Windows
     https://www.python.org/ftp/python/2.7.6/python-2.7.6.msi this is not tested in Python 3.
  Pygame 1.91
     http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi keep in mind that link is for Python 2.7.
  JP2A for Windows:
     http://sourceforge.net/projects/jp2a/

How to setup:

  Note: DO NOT plug in the camera until the driver is installed.
  1. Install the Code Laboratories driver.
  2. Plug the camera into a real USB port - not a hub.  If it doesn't work try the other USB ports.
  3. Test the camera with the 'CL-Eye Test' program the driver includes and puts on your desktop during install.
  4. If the camera doesn't work troubleshoot it.  If it does move on.
  5. Install Python 2.7.6 if it's not already.
  6. Install Pygame 1.91.
  7. Add Python (usually C:\Python27) to the Windows path.
  8. Download and install the code in a directory by itself (the reason will be obvious in step 10 below).
  9. Open the Python Video Capture library .ZIP and extract the files in:
     \VideoCapture-0.9-5.zip\VideoCapture-0.9-5\Python27
     Into the directory (assuming the default installation for Python 2.7.6):
     C:\Python27\DLLs
  10. Open the JP2A .ZIP and extract the files in:
      \jp2a-1.0.6-win32-bin.zip\win32-dist
      Into the same directory in which the ASSCI Instant Camera Python code resides.

How it works:

  When you run the Pythton code it will open a window and snap photos from the camera until you press any button.
  Once you press a button (with the capture window selected) the code will stop and save camimage.jpg.
  It will then start JP2A and convert that image to ASCII as camimage.txt.
  Finally it will display that ASCII text then exit.
