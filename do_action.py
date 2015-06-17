import os
import socket
import ConfigParser
import codecs
import re
import pdb

class Action(object):
    
    def __init__(self):

        self.host_name = socket.gethostname()
        self.testscript_subdir = 'pythonMini/testscripts'
        
    def execCmd(self, cmd):
        ''' execute the system command '''
        print cmd

        r = os.popen(cmd)
        out = r.read()
        r.close()

        if not ('ps -ef' in cmd):
            print out
        return out
        
    #def sendMail(self, error_type, exec_out_str, jnl_error_str):
    #    '''send mail method'''
    #    print "invoke sendMail method"
        #self.execCmd('mail -s %s %s %s' % (exec_out_str, jnl_error_str, mailto));
        #mail -s "GridTestRun:Started on host $HOSTNAME $GRIDSTATUSDIR"  $MAILTO << endofmsg
    def sendMail(self):
       print "invoke Action :: sendMail method"
         
    def reportCR (self, error_type):
        '''report server CR method'''
        
    def attachCR (self):
        '''associate CR'''
