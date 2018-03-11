# updating the ubuntu
sudo apt-get update
sudo apt-get install python3 python3-pip

#installing mod_wsgi
sudo apt-get remove libapache2-mod-python libapache2-mod-wsgi
sudo apt-get install libapache2-mod-wsgi-py3 python3-dev

#installing apache
sudo apt-get install apache2

#enabling wsgi
sudo a2enmod wsgi  

sudo service apache2 restart

## Getting codebase
cd /var/www
git clone https://github.com/pankajsinghrawat/trade-api

## installing dependencies
cd trade-api
pip3 install -r requirements.txt

## configuring apache
cp trade-api.conf /etc/apache2/sites-available/

## Adding new site to apache
sudo a2ensite trade-api
service apache2 reload

## removing default site from apache
a2dissite 000-default.conf
service apache2 reload

##https://www.jakowicz.com/flask-apache-wsgi/
