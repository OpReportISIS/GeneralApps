#!/usr/bin/python
# -*- coding: utf-8 -*-
# Based on a script by kernelzeroday

import sys
import time
import argparse


try:
    from PyQt4 import QtCore, QtGui
except:
    print "Please install PyQt4 Python library"
    sys.exit()

try:
    from splinter import Browser
except:
    print "Please install Splinter Python library"
    sys.exit()


#-----------------------------------------------------------------------
# Proxy Settings - Set the values here if you're using a proxy
#-----------------------------------------------------------------------

# *** NOTE: The use of proxy can be enabled by command: python TargetVerify.py -p
proxyIP = ''
proxyPort = 0

proxy_values = {'network.proxy.type': 1,
                  'network.proxy.http': proxyIP,
                  'network.proxy.http_port': proxyPort,
                  'network.proxy.ssl': proxyIP,
                  'network.proxy.ssl_port': proxyPort,
                  'network.proxy.socks': proxyIP,
                  'network.proxy.socks_port': proxyPort,
                  'network.proxy.ftp': proxyIP,
                  'network.proxy.ftp_port': proxyPort
                  }


#-----------------------------------------------------------------------
# To extend the class QtGui's QDialog
#-----------------------------------------------------------------------

class VerifyTarget(QtGui.QDialog):
    def __init__(self, url, browser, parent=None):
        super(VerifyTarget, self).__init__(parent)

        message_box = QtGui.QMessageBox(QtGui.QMessageBox.Question, "Target Verification", "", parent=self)
        message_box.setText('Is this an ISIS/Daesh account?')

        # Add buttons to the dialog box
        message_box.addButton(QtGui.QPushButton('Yes'), QtGui.QMessageBox.AcceptRole)
        message_box.addButton(QtGui.QPushButton('No, not sure'), QtGui.QMessageBox.RejectRole)
        message_box.addButton(QtGui.QPushButton('Abort'), QtGui.QMessageBox.NoRole)

        browser.visit(url)

        # If the Twitter account is suspended
        if "https://twitter.com/account/suspended" in browser.url:
            print "(suspended)"
            with open("log_error.txt", "a") as log:
                log.write("%s\n" % url)

        # If the Twitter user account is deactivated or changed name
        elif browser.is_element_present_by_css('.search-404'):
            print "(deleted)"
            with open("log_error.txt", "a") as log:
                log.write("%s\n" % url)

        else:
            # Check if it is a target ID link
            if "https://twitter.com/intent/user?" in browser.url:
                if browser.is_element_present_by_css('.url'):

                    # Navigate to the target page
                    browser.find_by_css('.url').click()
                    time.sleep(2)

            # Show the target verification dialog box
            ret_value = message_box.exec_()

            # If the user selected "Yes"
            if ret_value == 0:
                print "Yes"
                with open("log_target_yes.txt", "a") as log:
                    log.write("%s\n" % url)

            # If the user selected "No"
            elif ret_value == 1:
                print "No"
                with open("log_target_no.txt", "a") as log:
                    log.write("%s\n" % url)

            # If the user aborted the script
            else:
                print "\nAborting..."
                sys.exit()


#-----------------------------------------------------------------------
# The main script that controls the flow
#-----------------------------------------------------------------------

def main():
    global proxy_values

    try:
        # Parse the optional command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--input_file", help="The file with URLs to check")
        parser.add_argument("-p", "--use_proxy", help="Enable the use of proxy", action = "store_true")
        args = parser.parse_args()

        # If the input file flag is enabled, read targets from the input file
        if args.input_file:
            input_file = args.input_file
        else:
            input_file = ""

        # If the proxy flag is enabled, use the proxy settings
        if args.use_proxy:
            proxy_settings = proxy_values
        else:
            proxy_settings = None

        # If user has not set the -f in the command line argument, exit the script execution
        if not input_file:
            print "\nPlease enter -f in the command:"
            print "\npython TargetVerify.py -f <filename.txt>\n(replace the .txt with the filename with URLs to check)\n"
            sys.exit()

        # Create a new instance of Firefox browser
        browser = Browser('firefox', profile_preferences=proxy_settings)

        try:
            # Open the file that contains URLs to be verified
            f = open(input_file, 'r')
        except:
            print "Error: Can't open input file %s " % input_file
            sys.exit(1)

        # Initialize the QtGui
        app = QtGui.QApplication([])

        # Process each URLs in the input file
        for url in f:
            url = url.strip()

            if not url:
                continue

            # Add tabs in the layout of verification logs (to be printed on screen)
            if len(url) > 30:
                spacer = "\t"
            elif len(url) > 16:
                spacer = "\t\t"
            else:
                spacer += "\t\t\t"

            # Print the verification logs of each URL on the screen
            print url, spacer,
            VerifyTarget(url, browser)

        print "\nProcess completed."

    # Keyboard interrupt
    except KeyboardInterrupt:
        print "\nQuit by keyboard interrupt sequence!"
        sys.exit()

    # Exception
    except Exception as e:
        print "\n%s" % str(e.message)
        sys.exit()


# Execute the main script
if __name__ == "__main__":
    main()
