from selenium import webdriver


# define the website to scrape and path where the chromediver is located
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = '/usr/local/bin/chromedriver' # write the path here

driver = webdriver.Chrome(path)
driver.get(website)
