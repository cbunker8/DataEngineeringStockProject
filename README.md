Hello, 

(Link Access to Dashboard, further explanation down below https://cbunker8.github.io/DataEngineeringStockProject 

This is my final project for Data Engineering as part of the DACSS program. This project contains a data pipeline
to showcase skills we have learned throughout the semester. 

For my project I used an Postgresl RDS database hosted on EC2 instance where I gathered data from the yahoo finance 
API. I used crontab scheduler in order to schedule the execution of a python script which gathers data from the API
every six hours into the RDS. I included some minor transformations within SQL such as creating an is_weekend column,
which is simply a boolean expression in case I needed it for filtering during my visualization. I also used PGADMIN 4
in order to perfrom queries and look at my tables for convenience.

I utilized crontab to automatically send emails through python library smtplib, which contained the log files from the 
execution of the python file transforming data and loading into the rds (e.py). These emails send to a test email
every two hours where I can see the output of the logs.

Finally, I connected my rds to Google Looker and transformed the data into a real time dashboard report which is scheduled
to refresh every hour, although the data itself only updates every six hours. https://cbunker8.github.io/DataEngineeringStockProject

A note, the yahoo finance API is accessible through the yahoofinancer package. Generally, it has become more restrictive as
of late and is a good source of real time data. Other methods of gathering data from yahoo finance are possible, but not
stable or legal.

In summary:

Data Source: Yahoofinance.com

Extract Data from YahooFinance, I scheduled the extraction with crontab

Transform Data through Python script utilizing psycopg2 and numpy as well as SQL transformations

Load data into Amazon RDS hosted on EC2 utilizing the same script

Further Transform and visualize data

Monitor data and check for errors through logs sent every two hours to accessible email

The pipeline is automated because the scripts are automatically scheduled by crontab.
