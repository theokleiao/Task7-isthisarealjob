# Task7-isthisarealjob

****Required libraries****
pip install selenium
pip install pandas
 
Download the cac_scraper.py script and data folder.
Launch command prompt change the directory to where you saved the cac_scraper.py script and data folder(<b>DON'T</b> store the script <b>IN</b> the data folder). Run the app with this syntax

#>python cac_scraper.py aaa

The cac scraper launches a selenium webdriver that opens a new chrome window. in this window, it uses a sequential 3 charater combination string (eg. 'aaa', 'aab', 'aac', etc.)to search the cac website. this returns a table of companies that begin with the character combination. the app then scrapes the table data and stores it in a csv file in the data folder.
it has functionality to allow anyone chose which letter combination the wish to start from, this is valuabe for division of labour. for instance one person searches from 'aaa' to azz. next person 'baa' to 'bzz' and so on
so you open the cac_scraper.ipnyb, run the codes and run cac_scraper('baa'), if u want to search for companies beginning with BAA. then, in the new chrome window the scraper opens, click the checkbox to say you are not a robot, solve the captcha quiz and click submit. the search string would be entered automatically while you solve the captcha. after clicking submit, wait for the scraper to reload the page and solve the next captcha. if at any point you get tired, you simply close the browser window
