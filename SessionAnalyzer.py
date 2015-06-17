import os
import socket
import ConfigParser
import codecs
import re
import pdb
from analysis_base import Analyzer

class SessionAnalyzer(Analyzer):
    
    def __init__(self):
        super(Analyzer, self).__init__()
    
    def doWhat(self, error_type):
        '''based on error type, do what we want'''
        for error_str,severity in self.error_str_line.items():
            for case_number,str_line in self.error_jnl_line.items():
                if (error_str.find(str_line) != -1):
                    if severity == 0:
                        self.server_cr_instance.reportCR(severity, self.exec_out_line[case_number], self.error_jnl_line[case_number])
                        self.server_cr_instance.sendMail(severity, self.exec_out_line[case_number], self.error_jnl_line[case_number])
                    elif severity == 1:
                        self.server_cr_instance.reportCR(severity, self.exec_out_line[case_number], self.error_jnl_line[case_number])
                        self.server_cr_instance.sendMail(severity, self.exec_out_line[case_number], self.error_jnl_line[case_number])
                    elif severity == 2:
                        self.test_cr_instance.reportCR(severity, self.exec_out_line[case_number], self.error_jnl_line[case_number])
                        self.test_cr_instance.sendMail(severity, self.exec_out_line[case_number], self.error_jnl_line[case_number])
