# Task7-isthisarealjob

****Required libraries****
pip install selenium
pip install pandas

requirements Chrome=77


#About
The cac scraper is a web scraping bot using selenium webdriver. It uses a sequential 3 charater combination string (eg. 'aaa', 'aab', 'aac', etc.)to search the cac website. This returns a table of companies that begin with that paticular character combination. The bot then scrapes the table data and stores it in a csv file in the data folder.
It has functionality to allow anyone chose which letter combination the wish to start from, this is valuabe for division of labour. for instance one person searches from 'aaa' to azz. next person 'baa' to 'bzz' and so on

#Usage
Download the cac_scraper.py script and data folder.
Launch command prompt change the directory to where you saved the cac_scraper.py script and data folder(<b>DON'T</b> store the script <b>IN</b> the data folder). Run the app with this syntax(if u want to search for companies beginning with AAA).

#>python cac_scraper.py aaa

 The bot launches a new chrome window and directs it to the CAC website and inputs the combination string in the search box. The CAC website implements CAPTCHA, so there has to be manual input. In the window, click the checkbox to say you are not a robot, solve the captcha quiz and click submit. the search string would be entered automatically while you solve the captcha. after clicking submit, wait for the scraper to reload the page and solve the next captcha. If at any point you get tired, you simply close the browser window. The bot will update the data file.
 
