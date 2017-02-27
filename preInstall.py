## Asterisk - PRE-REQUISITES
## Created by - Rahul Nakra
import os,subprocess,shlex,datetime,time,functions

def checkNET():
	print "Probing for Internet Connection, please wait"
        functions.subprocess_cmd('wget -q --spider -T 3 google.com')

def preInstall():
        functions.subprocess_cmd('yum -y install epel-release mysql mysql-server mysql-devel unixODBC unixODBC-devel mysql-connector-odbc python-pip MySQL-python python-devel')
        time.sleep(3)
        functions.subprocess_cmd('pip install --upgrade alembic')
        time.sleep(2)
        print "Downloading Asterisk......... Please wait"
        functions.subprocess_cmd('wget http://downloads.asterisk.org/pub/telephony/certified-asterisk/asterisk-certified-13.13-current.tar.gz')
        time.sleep(2)

        dir_name = "asterisk" + "_" + functions.timenow + "old"
        dir_exists=os.path.exists('asterisk')
        if dir_exists == True:
                functions.subprocess_cmd('mv asterisk %s' % dir_name)
                time.sleep(2)
                functions.subprocess_cmd('mkdir asterisk')
                functions.subprocess_cmd('tar -xzvf asterisk-certified-13.13-current.tar.gz -C asterisk --strip-components=1')
        else:

                functions.subprocess_cmd('mkdir asterisk')
                functions.subprocess_cmd('tar -xzvf asterisk-certified-13.13-current.tar.gz -C asterisk --strip-components=1')

        functions.subprocess_cmd('./asterisk/contrib/scripts/install_prereq install')

