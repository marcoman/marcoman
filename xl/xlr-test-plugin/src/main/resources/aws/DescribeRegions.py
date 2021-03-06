#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from aws.AWS import AWS

aws = AWS.get_aws("startup")

aws.logger.info("=== AWS Describe Regions===")
aws.logger.info("You will connect to region {} with aws_access_key_id {} ".format(Region, Access_Key_ID))

f = open("aws-command", "a")
f.write('''\
export AWS_ACCESS_KEY_ID={}
export AWS_SECRET_ACCESS_KEY={}
export AWS_DEFAULT_REGION=us-west-2
aws ec2 describe-instances
'''.format(Access_Key_ID, Secret_Access_Key))
f.close()
