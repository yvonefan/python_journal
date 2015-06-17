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

def sendMail(self, error_type):
	tital = getTital();
	sender = getSender();
	receiver = getReceiver();
	attachFile = getAttachFiles();
	content = composeMail(eslf, error_type);
	cmd = 'mail -s ' + tital + ' -r ' + sender + ' ' + receiver + ' < ' + content;
	errInfo = execCmd(cmd);
	print(errInfo);

def composeMail(self, error_type): 
	verStr = getVerStr();
	caseList = getCaseList();
	description = getDescription();
	stackInfo = getStackInfo();
	tstLoc = getTstLoc();
	fileName = getFilePath();
	fd = open(fileName, w);
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

