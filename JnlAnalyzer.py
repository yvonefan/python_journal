import os
import socket
import ConfigParser
import codecs
import re
import pdb
import sys
import getopt
from analysis_base import Analyzer

class JnlAnalyzer(Analyzer):
    

    error_str = ""
    severity = 6
    
    case_number = 0
    str_line = []
    
    def __init__(self):
        super(Analyzer, self).__init__()
        
        self.error_str = ""
        self.severity = 6
        
        self.case_number = 0
        self.str_line = []

    def doWhat(self):
        '''based on error type, do what we want'''
        for self.error_str,self.severity in self.error_str_line.items():
            for self.case_number,self.str_line in self.error_jnl_line.items():
                print "hej"
                #if (self.error_str.find(" ".join(self.str_line)) != -1):
                if ((" ".join(self.str_line)).find(self.error_str.strip()[1:-1]) != -1):
                    if int(self.severity) == 0:
                        #self.server_cr_instance.reportCR(severity, self.exec_out_line[case_number], self.error_jnl_line[case_number])
                        self.server_cr_instance.sendMail(self.severity, self.exec_out_line[self.case_number], self.error_jnl_line[self.case_number])
                    elif int(self.severity) == 1:
                        print "severity %s" % self.severity
                        print "case number is %s" % self.case_number
                        print "exec out line is %s" % self.exec_out_line[self.case_number]
                        print "journal line is %s" % self.error_jnl_line[self.case_number]
                        #self.server_cr_instance.reportCR(severity, self.exec_out_line[case_number], self.error_jnl_line[case_number])
                        pdb.set_trace()
                        #self.server_cr_instance.sendMail(self.severity, self.exec_out_line[self.case_number], self.error_jnl_line[self.case_number])
                        self.server_cr_instance.sendMail()
                    elif int(self.severity) == 2:
                        print "severity %s" % self.severity
                        #self.test_cr_instance.reportCR(severity, self.exec_out_line[case_number], self.error_jnl_line[case_number])
                        self.test_cr_instance.sendMail(self.severity, self.exec_out_line[self.case_number], self.error_jnl_line[self.case_number])

if __name__ == '__main__':
    jnl_analyzer_instance = JnlAnalyzer()
    opts, args = getopt.getopt(sys.argv[1:], "j:t:e:")
    for op, value in opts:
        if op == "-j":
            jnl_file_name = value
        if op == "-t":
            error_temp_file = value
        if op == "-e":
            exec_out_file = value
    
    jnl_analyzer_instance.readErrorTemplate(error_temp_file)        
    jnl_analyzer_instance.readJnl(jnl_file_name)
    jnl_analyzer_instance.readExecOut(exec_out_file)
    jnl_analyzer_instance.doWhat()
    
