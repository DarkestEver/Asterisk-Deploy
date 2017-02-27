## Asterisk - PRE-REQUISITES
## Created by - Rahul Nakra
import os,subprocess,shlex,datetime,time,functions,preInstall

def astInstall():
	print "\033[1;32mInitiating Asterisk Installation..........\033[1;m"
	time.sleep(1)
	os.chdir('asterisk')
	functions.subprocess_cmd('./configure --libdir=/usr/lib64')
        functions.subprocess_cmd('menuselect/menuselect --enable res_config_mysql --enable app_mysql --enable cdr_mysql menuselect.makeopts')
        functions.subprocess_cmd('make')
        functions.subprocess_cmd('make install')
        functions.subprocess_cmd('make samples')
        functions.subprocess_cmd('make config')
	functions.subprocess_cmd('mkdir /etc/asterisk/samples')
        functions.subprocess_cmd('cp /etc/asterisk/*.* /etc/asterisk/samples')
	os.chdir(functions.current_working_dir)




