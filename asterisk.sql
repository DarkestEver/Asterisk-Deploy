CREATE database asterisk;
CREATE database asteriskcdrdb;
grant all on asterisk.* to 'astrt'@'localhost' identified by 'astrt';
grant all on asteriskcdrdb.* to 'astcdr'@'localhost' identified by 'astcdr';
grant all on *.* to 'dbadmin'@'10.23.24.%' identified by 'dbadmin';
use asteriskcdrdb;
CREATE TABLE cdr ( 
        calldate datetime NOT NULL default '0000-00-00 00:00:00', 
        clid varchar(80) NOT NULL default '', 
        src varchar(80) NOT NULL default '', 
        dst varchar(80) NOT NULL default '', 
        dcontext varchar(80) NOT NULL default '', 
        channel varchar(80) NOT NULL default '', 
        dstchannel varchar(80) NOT NULL default '', 
        lastapp varchar(80) NOT NULL default '', 
        lastdata varchar(80) NOT NULL default '', 
        duration int(11) NOT NULL default '0', 
        billsec int(11) NOT NULL default '0', 
        disposition varchar(45) NOT NULL default '', 
        amaflags int(11) NOT NULL default '0', 
        accountcode varchar(20) NOT NULL default '', 
        uniqueid varchar(32) NOT NULL default '', 
        userfield varchar(255) NOT NULL default '' 
);

