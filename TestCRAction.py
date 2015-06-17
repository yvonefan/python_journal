import os
import socket
import ConfigParser
import codecs
import re

import pdb
from do_action import Action

class TestCRAction(Action):
    
    def __init__(self):
        super(Action, self).__init__()
        
    def sendMail(self, error_type):
        '''send mail method'''
        print "invoke TestCRAction::sendMail method"
        
    def reportCR (self, error_type):
        '''report server CR method'''
        
    def attachCR (self):
        '''associate CR'''
