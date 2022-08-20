from selenium import webdriver
import time
from bs4 import BeautifulSoup

# Scraping linked in search results
def scrape_linkedin(search):
    # Opening the driver
    driver2 = webdriver.Chrome()
    url = 'https://in.linkedin.com/jobs/search?keywords=&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    driver2.get(url)
    search_bar = driver2.find_element('xpath', '/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input')
    search_bar.send_keys(search)
    search_icon = driver2.find_element('xpath', '/html/body/div[1]/header/nav/section/section[2]/form/button')
    search_icon.click()
    time.sleep(5)
    soup = BeautifulSoup(driver2.page_source)
    result_tag = soup.find('ul', class_='jobs-search__results-list')
    job_list = result_tag.find_all('li')
    for job in job_list:
        name = job.find('h3', class_="base-search-card__title").text.strip()
        company = job.find('h4', class_="base-search-card__subtitle").text.strip()
        location = job.find('span', class_='job-search-card__location').text.strip()
        print(name, company, location)
        time.sleep(2)

# Scraping Categories
def scraping_category():
    # Opening the driver
    driver = webdriver.Chrome()

    # Getting Category URL
    try:
        driver.get("https://www.careerguide.com/career-options")
        source=driver.page_source
        soup = BeautifulSoup(source, 'lxml')
        major_categories = soup.find_all('div', class_='col-md-4')
        for sub_category in major_categories:
            try:
                category_title = sub_category.find('a').text
                print(category_title)
                name_list = sub_category.find('ul', class_='c-content-list-1 c-theme c-separator-dot')
                for name in name_list:
                    try:
                        print('   ', name.text)
                        scrape_linkedin(name.text)
                    except Exception as e:
                        print(name, e)
                    continue
            except Exception as e:
                print(sub_category, e)
                continue
    except Exception as e:
        print(e)

scraping_category()