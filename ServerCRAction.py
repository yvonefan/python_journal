import os
import socket
import ConfigParser
import codecs
import re
import pdb
from do_action import Action

class ServerCRAction(Action):
    
    def __init__(self):
        super(Action, self).__init__()
        
    #def sendMail(self, error_type, exec_out_str, jnl_error_str):
    #    '''send mail method'''
    #    print "ServerCRAction sendMail method call"

    def sendMail(self):
       print "invoke ServerCRAction::sendMail method"
        
    def reportCR (self, error_type):
        '''report server CR method'''
        
    def attachCR (self):
        '''associate CR'''
