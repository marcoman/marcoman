#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from org.slf4j import Logger
from org.slf4j import LoggerFactory
from mysql.MySql import MySql
import os

mydb = MySql.get_mysql("startup")


mydb.loginfo("=== MYSQL SHOW TABLES ===")
mydb.loginfo("You will connect to {} with username {}".format(serverurl, username))

f = open("mysql-command", "a")
f.write("show databases;")
f.close()

f = open("mysql-invoke", "a")
f.write("mysql -h{} -u {} -p{}".format(serverurl, username, password))
f.close()

myCmd = 'pwd'
myOutput = os.system(myCmd)
mydb.loginfo("=== MYSQL Command output is \n{}".format(myOutput))
