## Installation of Asterisk certified version
import os,subprocess,shlex,datetime,time,functions,preInstall,astInstall,dbInstall,finish

print "\033[1;32m-------------------------------"
print "Please ensure that you have"
print "1. Internet connection"
print "2. Base and Development tools intalled"
print "--------------------------------------\033[1;m \n"

answer=functions.qa("Do you wish to continue with installation ... [y/n]")


preInstall.checkNET()
preInstall.preInstall()
astInstall.astInstall()
dbInstall.dbSetup()
finish.run_as_asterisk()
finish.cdr_fix()

