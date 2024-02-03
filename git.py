
# Skills & Place of Work
skill = input('Enter your Skill: ').strip()
place = input('Enter the location: ').strip()
no_of_pages = int(input('Enter the # of pages to scrape: '))

indeed_posts=[]

for page in range(no_of_pages):
    
    # Connecting to India Indeed
        url = 'https://www.indeed.co.in/jobs?q=' + skill + \
            '&l=' + place + '&sort=date' +'&start='+ str(page * 10)
        
        # Get request to indeed with headers above (you don't need headers!)
        response = requests.get(url, headers=headers)
        html = response.text

        # Scrapping the Web (you can use 'html' or 'lxml')
        soup = BeautifulSoup(html, 'lxml')

        # Outer Most Entry Point of HTML:
        outer_most_point=soup.find('div',attrs={'id': 'mosaic-provider-jobcards'})
        
        # "UL" lists where the data are stored:
        
        for i in outer_most_point.find('ul'):
            
        # Job Title:
        
            job_title=i.find('h2',{'class':'jobTitle jobTitle-color-purple jobTitle-newJob'})
#             print(job_title)
            if job_title != None:
                jobs=job_title.find('a').text

        # Company Name:
    
            if i.find('span',{'class':'companyName'}) != None:
                company=i.find('span',{'class':'companyName'}).text   
                
        # Links: these Href links will take us to full job description
        
            if i.find('a') != None:
                links=i.find('a',{'class':'jcs-JobTitle'})['href']
                
        # Salary if available:
        
            if i.find('div',{'class':'attribute_snippet'}) != None:
                salary=i.find('div',{'class':'attribute_snippet'}).text

            else:
                salary='No Salary'

        # Job Post Date:

            if i.find('span', attrs={'class': 'date'}) != None:
                post_date = i.find('span', attrs={'class': 'date'}).text

        # Put everything together in a list of lists for the default dictionary
                        
            indeed_posts.append([company,jobs,links,salary, post_date])
            
            
# put together in list

# (create a dictionary with keys and a list of values from above "indeed_posts")

indeed_dict_list=defaultdict(list)

# Fields for our DF 

indeed_spec=['Company','job','link','Salary','Job_Posted_Date']


################################################################################""

from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# delay for selenium web driver wait
DELAY = 30

# create selenium driver
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('<<PATH TO chromedriver>>', options=chrome_options)

# iterate over pages
for page in range(0, 10, 1):
    
    # open web page
    driver.get(f'https://www.apec.fr/candidat/recherche-emploi.html/emploi?page={page}')
    
    # wait for element with class 'container-result' to be added
    container_result = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CLASS_NAME, "container-result")))
    # scroll to container-result
    driver.execute_script("arguments[0].scrollIntoView();", container_result)
    # get source HTML of the container-result element
    source = container_result.get_attribute('innerHTML')
    # print source
    print(source)
    # here you can continue work with the source variable either using selenium API or using BeautifulSoup API:
    # soup = BeautifulSoup(source, "html.parser")

# quit webdriver    
driver.quit()