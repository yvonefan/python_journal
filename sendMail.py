#!/usr/bin/python

import os

def execCmd(cmd):
	''' execute the system command '''
	print cmd
	r = os.popen(cmd)
	out = r.read()
	r.close()
	if not ('ps -ef' in cmd):
		print out
	return out

def sendMail(tital, sender, receiver, attachFile):
	content = composeMail('123.456\n', 'testcase{1}\n', 'This is just a test mail!\n', 'no stack\n', '/usr/bin/xxx\n');
	cmd = 'mail -s ' + tital + ' -r ' + sender + ' ' + receiver + ' < ' + content;
	errInfo = execCmd(cmd);
	print(errInfo);

def composeMail(verStr, caseList, description, stackInfo, tstLoc):
	fileName = './content';
	fd = open(fileName, 'w');
	fd.write('Version string:\n---------------\n');
	fd.write(verStr);
	fd.write('\nAffected tests:\n---------------\n');
	fd.write(caseList);
	fd.write('\nProblem:\n---------------\n');
	fd.write(description);
	fd.write('\nStack trace:\n------------\n');
	fd.write(stackInfo);
	fd.write('\nTest case location:\n-------------------\n');
	fd.write(tstLoc);
	fd.close();
	return fileName;


tital = 'testMail';
sender = 'hao.wang04@sap.com';
receiver = 'haow@sybase.com';
attachFile = '';

sendMail(tital, sender, receiver, attachFile);
