Asterisk Installation package

Package contains basic installation of Asterisk with PJSIP using realtime channel.

Package contains

1. Asterisk certified version 13.8
	- Installer currently works on fixed Asterisk version.
	- Only PJSIP is configured
2. MySQL DB server
	- MySQL server is installed on local machine.
	- To use external DB, follow below steps
		a. Once installation completes, take DB dump of asterisk
		b. restore DB dump on external DB
		c. Create user astrt with password astrt on external DB. Asterisk server should be allowed on DB server for this.
		d. Update /etc/odbc.ini, /etc/asterisk/res_odbc.conf, /etc/asterisk/extconfig.conf

TODO

Lot of fixes :)

