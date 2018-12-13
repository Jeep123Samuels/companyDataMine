# companyDataMine
Data mining service based on company information.

Search and get data for domains and user's comapnies if available.


For ubuntu 16.04: 

########################################
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
 
apt-get install zlib1g=1:1.2.8.dfsg-2ubuntu4
# Install requirements 
sudo apt-get install -y build-essential 
sudo apt-get install -y checkinstall 
sudo apt-get install -y libreadline-gplv2-dev
sudo apt-get install -y libncursesw5-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y libsqlite3-dev
sudo apt-get install -y tk-dev
sudo apt-get install -y libgdbm-dev
sudo apt-get install -y libc6-dev
sudo apt-get install -y libbz2-dev
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y openssl
sudo apt-get install -y libffi-dev
sudo apt-get install -y python3-dev
sudo apt-get install -y python3-setuptools
sudo apt-get install -y wget

# Prepare to build
mkdir /tmp/Python37
cd /tmp/Python37

# Pull down Python 3.7, build, and install
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar xvf Python-3.7.0.tar.xz
cd /tmp/Python37/Python-3.7.0
./configure
sudo make altinstall

##################################################

create a virtualenv using:
python3.7 -m venv <directory>

Then activate the venv and run pip install requirements.

#################################################

TESTS:

To run tests:
python3.7 -m pytest
