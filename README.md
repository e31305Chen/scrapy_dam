Dev: Philip Lin

Start up

    $ sudo apt-get update
    $ sudo pip install pip --upgrade
    $ sudo pip install virtualenv
    $ virtualenv -p python3 ~/.env

    $ source ~/.env/bin/activate
    $ xargs sudo apt-get install < aptlist  #逐行install
    $ pip install -r requirements.txt

DB
mysql-ctl start
mysqladmin -u root password 'root1234'

//UPDATA MYSQL 5.5 -> 5.7//
wget http://dev.mysql.com/get/mysql-apt-config_0.8.0-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.0-1_all.deb  #enter & select preferable version 
sudo apt-get update
sudo apt-get install mysql-server
rm mysql-apt-config_0.8.0-1_all.deb 

//mysql -u root -p//
SELECT USER, HOST, PASSWORD from mysql.user;

check list
-damwra OK
    scrapy crawl damwra -o dam.json 

-DataBase
