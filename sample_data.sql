use asterisk;
INSERT INTO  ps_endpoints(id,transport,aors,auth,context,disallow,allow,direct_media,moh_suggest,send_pai,send_rpid,callerid,named_call_group,named_pickup_group) VALUES ("101","transport-udp","101","auth101","internal","all","alaw","yes","QRMOH","yes","yes","Test01 <12341011>",NULL,NULL);
INSERT INTO  ps_endpoints(id,transport,aors,auth,context,disallow,allow,direct_media,moh_suggest,send_pai,send_rpid,callerid,named_call_group,named_pickup_group) VALUES ("102","transport-udp","102","auth102","internal","all","alaw","yes","QRMOH","yes","yes","Test02 <12341012>",NULL,NULL);

INSERT INTO ps_auths(id,auth_type,password,username) VALUES ("auth101","userpass","101","101");
INSERT INTO ps_auths(id,auth_type,password,username) VALUES ("auth102","userpass","102","102");
INSERT INTO ps_aors(id,max_contacts) VALUES("101","1");
INSERT INTO ps_aors(id,max_contacts) VALUES("102","1");



