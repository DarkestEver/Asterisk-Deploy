## Database configuration for Asterisk
# Start MySQL local DB with username / password
# Get input for local or remote DB options
# Create DB in local, disply local user / pass for Asterisk application DB
# Prompt for root credentials if DB is remote
# Create DB in remote, display remote user / pass for Asterisk application DB
import os,subprocess,shlex,datetime,time,functions,preInstall,astInstall


def dbSetup():
	functions.subprocess_cmd('service mysqld start')
	answer=functions.qa("Do you wish to continue with DB setup [Y/N]")
	answer=functions.userInput("Which DB do you want to use for \033[1;32mPJSIP\033[1;m [external/localhost]")
	if answer == "EXTERNAL":
		print "\033[1;31m COMING SOON \n"
		print "As soon as ALMBIC setup is available from Asterisk for remote DB"
		print "Will continue with local DB setup\n"
		print "You can take DB dump => restore on remote DB => Adjust ODBC settings accordingly"
		print "Continuing with local DB \033[1;m"
		time.sleep(2)
		localDB()	
	else:
		print "setup local DB"
		localDB()

def localDB():
	functions.subprocess_cmd('service mysqld start')
        print "\033[1;31m;---------------------------------------------------------"
        print "Setup will continue WITHOUT setting MySQL 'root' password"
        print "Please reset MySQL root password after setup\n\n"
        print "---------------------------------------------------------\033[1;m"
        time.sleep(2)
        functions.subprocess_cmd('mysql < asterisk.sql')
        os.chdir('asterisk/contrib/ast-db-manage')
        time.sleep(2)
        functions.subprocess_cmd('cp config.ini.sample config.ini')
        functions.subprocess_cmd("sed -i 's/sqlalchemy.url.*/sqlalchemy.url = mysql:\/\/localhost\/asterisk/g' config.ini")
        functions.subprocess_cmd('alembic -c config.ini upgrade head')
	os.chdir(functions.current_working_dir)
	functions.subprocess_cmd('mysql < sample_data.sql')
        file_exists=os.path.exists("/etc/odbc.ini")
        odbc_ini_content="""[asterisk]
Driver = MySQL
Description = MySQL connection to asterisk database
Server = localhost
Port = 3306
Database = asterisk
UserName = astrt
Password = astrt
[asteriskcdrdb]
Driver = MySQL
Description = MySQL connection to asteriskcdrdb database
Server = localhost
Port = 3306
Database = asteriskcdrdb
UserName = astcdr
Password = astcdr"""
        if file_exists == True:
                f=open("/etc/odbc.ini","w")
                f.write(odbc_ini_content)
                f.close()
        else:
                print "\033[1;31m Check OBDC configuration and try again\033[1;m"
                exit(0)
        functions.subprocess_cmd('rm -rf /etc/asterisk/res_odbc.conf')
        functions.subprocess_cmd('touch /etc/asterisk/res_odbc.conf')
        res_odbc_conf="""[asterisk]
enabled => yes
dsn => asterisk
username => astrt
password => astrt
pre-connect => yes
[asteriskcdrdb]
enabled => yes
dsn => asteriskcdrdb
username => astcdr
password => astcdr
pre-connect => yes"""
        f=open("/etc/asterisk/res_odbc.conf","w")
        f.write(res_odbc_conf)
        f.close()
        sorcery_conf="""[res_pjsip] ; Realtime PJSIP configuration wizard
endpoint=realtime,ps_endpoints
auth=realtime,ps_auths
aor=realtime,ps_aors
domain_alias=realtime,ps_domain_aliases
contact=realtime,ps_contacts

[res_pjsip_endpoint_identifier_ip]
identify=realtime,ps_endpoint_id_ips"""
	f=open("/etc/asterisk/sorcery.conf","w")
        f.write(sorcery_conf)
        f.close()
        extconfig_conf="""[settings]
ps_endpoints => odbc,asterisk
ps_auths => odbc,asterisk
ps_aors => odbc,asterisk
ps_domain_aliases => odbc,asterisk
ps_endpoint_id_ips => odbc,asterisk
ps_contacts => odbc,asterisk"""
        f=open("/etc/asterisk/extconfig.conf","w")
        f.write(extconfig_conf)
        f.close()
