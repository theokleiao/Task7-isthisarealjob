#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install beautifulsoup4')


# In[6]:


get_ipython().system('pip install mysqlclient')


# In[7]:


get_ipython().system('pip install requests')


# In[8]:


import requests
import MySQLdb
from bs4 import BeautifulSoup


# In[9]:


HOST = "localhost"
USERNAME = "scraping_user"
PASSWORD = ""
DATABASE = "scraping_sample"


# In[10]:


url_to_scrape = 'https://howpcrules.com/sample-page-for-web-scraping/'
#Load html's plain data into a variable
plain_html_text = requests.get(url_to_scrape)
#parse the data
soup = BeautifulSoup(plain_html_text.text, "html.parser")


# In[11]:


print(soup.prettify())


# In[12]:


#Get the name of the class
name_of_class = soup.h3.text.strip()


# In[13]:


#Get all data associated with this class
basic_data_table = soup.find("table", {"summary": "Basic data for the event"});
#Get all cells in the base data table
basic_data_cells = basic_data_table.findAll('td')


# In[14]:


#get all the different data from the table's tds
type_of_course = basic_data_cells[0].text.strip()
lecturer = basic_data_cells[1].text.strip()
number = basic_data_cells[2].text.strip()
short_text = basic_data_cells[3].text.strip()
choice_term = basic_data_cells[4].text.strip()
hours_per_week_in_term = basic_data_cells[5].text.strip()
expected_num_of_participants = basic_data_cells[6].text.strip()
maximum_participants = basic_data_cells[7].text.strip()
assignment = basic_data_cells[8].text.strip()
lecture_id = basic_data_cells[9].text.strip()
credit_points = basic_data_cells[10].text.strip()
hyperlink = basic_data_cells[11].text.strip()
language = basic_data_cells[12].text.strip()


# In[22]:


#Save class's base data to the database
# Open database connection
db = MySQLdb.connect(host = '127.0.0.1', user = 'scraping_user', password = '1234dammie', database = 'scraping_sample')
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO classes(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, 'NOW()')
try:
 # Execute the SQL command
 cursor.execute(sql)
 # Commit your changes in the database
 db.commit()
except:
 # Rollback in case there is any error
 db.rollback()
 #get the just inserted class id
sql = "SELECT LAST_INSERT_ID()"
try:
 # Execute the SQL command
 cursor.execute(sql)
 # Get the result
 result = cursor.fetchone()
 # Set the class id to the just inserted class
 class_id = result[0]
except:
 # Rollback in case there is any error
 db.rollback()
 # disconnect from server
 db.close()
 # on error set the class_id to -1
 class_id = -1


# In[15]:


#Get the tables where the dates are written.
dates_tables = soup.find_all("table", {"summary": "Overview of all event dates"});


# In[34]:


#Iterate through the tables
for table in dates_tables:
 #Iterate through the rows inside the table
 for row in table.select("tr"):
  #Get all cells inside the row
  cells = row.findAll("td")
  #check if there is at least one td cell inside this row
  if(len(cells) > 0):
   #get all the different data from the table's tds
   #Split this cell into two different parts seperated by 'to' in order to have a start_date and an end_date.
   duration = cells[0].text.split("to")
   start_date = duration[0].strip()
   end_date = duration[1].strip()
   day = cells[1].text.strip()
   #Split this cell into two different parts seperated by 'to' in order to have a start_time and an end_time.
   time = cells[2].text.split("to")
   start_time = time[0].strip()
   end_time = time[1].strip()
   frequency = cells[3].text.strip()
   room = cells[4].text.strip()
   lecturer_for_date = cells[5].text.strip()
   status = cells[6].text.strip()
   remarks = cells[7].text.strip()
   cancelled_on = cells[8].text.strip()
   max_participants = cells[9].text.strip()
   #Save event data to database
   # Open database connection
   db = MySQLdb.connect(host = '127.0.0.1', user = 'scraping_user', password = '1234dammie', database = 'scraping_sample')
   # prepare a cursor object using cursor() method
   cursor = db.cursor()
   # Prepare SQL query to INSERT a record into the database.
   sql = "INSERT INTO events(class_id, start_date, end_date, day, start_time, end_time, frequency, room, lecturer_for_date, status, remarks, cancelled_on, max_participants, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(class_id, start_date, end_date, day, start_time, end_time, frequency, room, lecturer_for_date, status, remarks, cancelled_on, max_participants, 'NOW()')
try:
    # Execute the SQL command
    cursor.execute(sql)
     # Commit your changes in the database
    db.commit()
except:
     # Rollback in case there is any error
    db.rollback()
     # disconnect from server
    db.close()


# In[ ]:




