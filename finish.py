## Finish configuration for Asterisk
# Configure asterisk runtime ENV
# Configure asterisk configuration which will remain static

import os,subprocess,shlex,datetime,time,functions,preInstall,astInstall

def run_as_asterisk():
	functions.subprocess_cmd('useradd asterisk')
	functions.subprocess_cmd("chown -R asterisk:asterisk /var/lib/asterisk")
	functions.subprocess_cmd("chown -R asterisk:asterisk /var/log/asterisk")
	functions.subprocess_cmd("chown -R asterisk:asterisk /var/run/asterisk")
	functions.subprocess_cmd("chown -R asterisk:asterisk /var/spool/asterisk")
	functions.subprocess_cmd("chown -R asterisk:asterisk /etc/asterisk")
	functions.subprocess_cmd("chown -R asterisk.asterisk /usr/lib/asterisk")
	functions.subprocess_cmd("chown -R asterisk.asterisk /usr/lib64/asterisk")
	functions.subprocess_cmd("sed -i 's/^ASTARGS/#ASTARGS/g' /usr/sbin/safe_asterisk")
	functions.subprocess_cmd("sed -i '/#ASTARGS/a\ASTARGS=\"-U asterisk -G asterisk\"' /usr/sbin/safe_asterisk")
	functions.subprocess_cmd("sed -i 's/^#AST_USER/AST_USER/g' /etc/sysconfig/asterisk")
	functions.subprocess_cmd("sed -i 's/^#AST_GROUP/AST_GROUP/g' /etc/sysconfig/asterisk")
	functions.subprocess_cmd("sed -i 's/^;runuser/runuser/g' /etc/asterisk/asterisk.conf")
	functions.subprocess_cmd("sed -i 's/^;rungroup/rungroup/g' /etc/asterisk/asterisk.conf")
	transport_udp="""[transport-udp]
type=transport
protocol=udp
bind=0.0.0.0
"""
	f=open("/etc/asterisk/pjsip.conf","a")
	f.write(transport_udp)
	f.close()	
#	sys_name=functions.userInput("\033[1;32m Please enter system name without spaces........\033[1;m")
#	functions.subprocess_cmd("sed -i '/^;systemname/a\systemname=$sys_name' /etc/asterisk/asterisk.conf")
	functions.subprocess_cmd("service asterisk restart")

def cdr_fix():
	cdr_adaptive_odbc="""[asteriskcdrdb]
connection=asteriskcdrdb
table=cdr
alias start => calldate
"""
        f=open("/etc/asterisk/cdr_adaptive_odbc.conf","w")
        f.write(cdr_adaptive_odbc)
        f.close()

		

#run_as_asterisk()
#cdr_fix()
