TargetVerification (version 1.0)


Video Introduction
------------------
https://www.youtube.com/watch?v=4qr7dkpxK44


=== 1. DESCRIPTION

A Python script that allow users to verify a list of URLs if they are ISIS/Daesh pages.

It accepts any URLs such as website, Facebook, Instagram etc. 
- One URL per line.

If the URL is Twitter, the script will:
i.  If the account is suspended or deactivated/changed name, skip it and move to the next target.

ii. If the URL is in ID format (see below), auto redirect the user to the username page so that he/she could verify tweets.
https://twitter.com/intent/user?user_id=xxxxxxxxx

REMINDER
--------
Please wait until the dialog box is displayed, before you scroll down the page to check for ISIS contents. Or else, the dialog box might hide behind your browser.

   
=== 2. REQUIREMENTS

Install

i.  Python 2.7.

ii. Splinter:

UNIX
Follow instructions : http://splinter.readthedocs.org/en/latest/install.html

WINDOWS
Get the zip : https://github.com/cobrateam/splinter/archive/master.zip unzip on your disk, open a terminal (start menu -> type cmd -> launch cmd.exe) go in the folder you unzip splinter (cd XXXX) launch 'python setup.py install'

iii.PyQt4:

LINUX
http://pythoncentral.io/install-pyside-pyqt-on-windows-mac-linux/

WINDOWS
http://pythoncentral.io/install-pyside-pyqt-on-windows-mac-linux/
https://riverbankcomputing.com/software/pyqt/download


=== 3. CONFIGURATION

If you are using a proxy, set its values in TargetVerification.py.


=== 4. EXECUTION

Execute "python TargetVerification.py -h" to show help.
  
Usage Examples:

- If you are not using a proxy:
  python TargetVerification.py -f <filename.txt> 

- If you are using a proxy:
  python TargetVerification.py -f <filename.txt> -p

(replace filename.txt with your input file with URLs to verify)


=== 5. LICENSE

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
