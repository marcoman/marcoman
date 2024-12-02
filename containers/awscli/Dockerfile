# Use an official Python runtime as a parent image 
FROM ubuntu:22.10

# Set the working directory 
WORKDIR /root 
 
# Copy the current directory contents into the container
COPY startup.sh /root/startup.sh 
# Copy the aws setup script we initilize after we signon.  
# We do not automate the automatic inclusion of our credentials.  Make it a post-startup activity a human must do.
COPY setup-aws.sh /root/setup-aws.sh 
 
# Install any needed packages specified in requirements.txt 
RUN echo "America/New_York" > /etc/timezone
RUN apt-get update
RUN apt-get -y install \
  build-essential \
  curl \
  git \
  python-dev \
  python-setuptools \
  python3 \
  python3-pip \
  unzip \
  wget

# Setup aws from the bundled distribution.
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

#Setup Openshift
RUN wget https://github.com/openshift/origin/releases/download/v3.6.0/openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz -O /root/openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz 
RUN tar -xvf openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz 
RUN ln -s openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit/oc /usr/local/bin/oc 

  
# Make port 80 available to the world outside this container 
#EXPOSE 80 
 
# Define environment variable 
ENV MYNAME Marco

# Define an entrypoint if it is needed
#ENTRYPOINT ["entrypoint.sh"]
 
#Run some commands on startup
CMD ["startup.sh"] 
