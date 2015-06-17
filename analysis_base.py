import os
import socket
import ConfigParser
import codecs
import re
import pdb
from do_action import Action
from ServerCRAction import ServerCRAction
from TestCRAction import TestCRAction

class Analyzer(object):
    server_cr_instance = ServerCRAction()
    test_cr_instance = TestCRAction()
    action_instance = Action()

    error_str_line = {}
    error_str = ""
    severity = 6

    error_jnl_line = {}
    case_number = 0
    str_line = []
    
    exec_out_line = {}
    exec_case_number = 0
    tcf_name = ""
    exec_result = ""

    error_session_line = {}
    line_number = 0
    error_line = ""

    def __init__(self):
        self.server_cr_instance = ServerCRAction()
        self.test_cr_instance = TestCRAction()
        self.action_instance = Action()
        
        '''Hash structure to save error template file'''
        self.error_str_line = {}
        self.error_str = ""
        self.severity = 6
        
        '''Hash structure to save journal file'''
        self.case_number = 0
        ## str_line is the list of journal line
        self.str_line = []
        self.error_jnl_line = {}
        
        '''Hash structure to save execute out file'''
        self.exec_case_number = 0
        self.tcf_name = ""
        self.exec_result = ""
        self.exec_out_line = {}
        
        '''Hash structure to save session file'''
        self.error_session_line = {}
        self.line_number = 0
        self.error_line = ""
      
    def readFile(self, file_name):
        '''read file function'''
        fin = codecs.open(file_name, "r", "utf-8")
        in_file = fin.readlines()
        fin.close()
        return in_file

    def writeFile(self, file_name, lines):
        '''write file function'''
        with codecs.open(file_name, 'w', "utf-8") as out_file:
            for line in lines:
                out_file.write(line)
        out_file.close()
        
    def readErrorlog(self, jnl_file_name):
        '''read session file'''        
        
    def readExecOut(self, out_file_name):
        '''read exec out file'''
        pdb.set_trace()
        str_line = self.readFile(out_file_name)
        for line in  str_line :
            matched = re.match(r"(.*)\{([0-9]*)\}\: (\w+)", line)
            if matched:
                self.tcf_name = matched.group(1)
                self.exec_case_number = matched.group(2)
                self.exec_result = matched.group(3)
                if self.exec_result != "PASS":
                    self.exec_out_line[self.exec_case_number] = self.tcf_name + '{' + self.exec_case_number + '}' + ':' +  self.exec_result
                
    def readErrorTemplate(self, template_file_name):
        '''read error template file'''
        str_line = self.readFile(template_file_name)
        for line in  str_line :
            matched = re.match(r"(.*)( *)(\d+)", line)
            if matched:
                self.error_str = matched.group(1)
                self.severity = matched.group(3)
                if (self.error_str_line.has_key(self.error_str)== False):
                    self.error_str_line[self.error_str] = 0
                self.error_str_line[self.error_str] = self.severity
                
    def readJnl(self, jnl_file_name):
        '''read jnl file'''
        str_line = self.readFile(jnl_file_name)
        for line in  str_line :
            matched = re.match(r"^([0-9]*)\|([0-9]*)( )([1-9]*)( )([0-9]*)( )([0-9]*)( )([0-9]*)( )(0\d{1}|1\d{1}|2[0-3]):[0-5]\d{1}:([0-5]\d{1})\|(.*)", line)
            if matched:
                self.case_number = matched.group(4)
                self.str_line = matched.group(14)
                if (self.error_jnl_line.has_key(self.case_number) == False):
                    self.error_jnl_line[self.case_number] = []
                self.error_jnl_line[self.case_number].append(self.str_line)
    def doWhat(self):
        '''based on error type, do what we want'''
