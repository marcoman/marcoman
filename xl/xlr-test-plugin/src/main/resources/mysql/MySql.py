#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import json
import sys
from org.slf4j import Logger
from org.slf4j import LoggerFactory

class MySql(object):
    # It is convenient to have separate values for exit codes, instead of the usual exit(1)

    @staticmethod
    def exit (self, code, message):
        self.logger.error("MYSQL({}) {}".format(code, message))
        exit("MYSQL({}) {}".format(code, message))
    #        exit(code)

    @staticmethod
    def get_mysql(self):
        return MySql()

    def loginfo (self, message):
        self.logger.info(message)

    def __init__(self):
        self.logger = LoggerFactory.getLogger("mysql")
        self.logger.info("=== INITIALIZE MYSQL ==========================================")
