# Udacity-Full-Stack-Web-DeveloperProject 1 for Udacity's Full Stack Web Developer Nanodegree

Project Description:
The main purpose of this project is building a python code using “psycopg2” module that answers the following three questions by using “newsdata.sql”:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Pre-requisites:
-Install Vagrant: https://www.vagrantup.com/downloads.html
-Install Virtual Machine:https://www.virtualbox.org/wiki/Downloads 
-Install python 3.5.2
-psycop2
-Download the FSND virtual machine files from here: https://github.com/udacity/fullstack-nanodegree-vm.
-Unix-style terminal program you can use the built-in Terminal. 

# Starting the virtual machine and exploring the data
In the terminal write these commands:
cd vagrant
vagrant up
vagrant ssh
cd /vagrant
mkdir log-analysis-project
cd log-analysis-project

After that you need to download “newsdata.sql” from the project in this link:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdat
1-unzip the file.
2-Move the “newsdata.sql” to your project folder “log-analysis-project”
3-Load the data from the “newsdata.sql” by using the following command: 
psql -d news -f newsdata.sql
psql -d news

Here's what this command does:
psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands
in the downloaded file, creating tables and populating them with data.
This only needs to be done once. When reconnecting, after vagrant up and vagrant ssh, simply use
cd /vagrant
psql -d news
To log out (the opposite of vagrant ssh), just type ctrl+d or the command
logout

To explore the data in the database:
\dt: display tables — lists the tables that are available in the database.
\d table_name: shows the database schema for that particular table.
The “newsdata.sql” has three different tables:
1-Authors: table includes information about the authors of articles.
2-Articles: table includes the articles themselves.
3-Log: table includes one entry for each time a user has accessed the site.

Running the reporting tool:
The logs reporting tool is executed with the following command:
python log_analysis.py
Then the answers to the three questions that mentioned above should be displayed.
