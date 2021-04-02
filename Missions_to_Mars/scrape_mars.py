#importing dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    #set up splinter 
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

    #creating dictionary
    #mars_data = {}

    #--------------------------
    #NASA Mars News

    #visit
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

    #scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all elements that contain news title
    latest_news = soup.find("div", class_="list_text")

    #get the latest news title from the page
    latest_news_title = latest_news.find_all("div", class_="content_title")[0].text

    #get the paragraph text of latest news 
    news_para = latest_news.find_all("div", class_="article_teaser_body")[0].text

    #store data in dictionary
    latest_news_title = str(latest_news_title)
    news_para = str(news_para)

    #mars_data["news_title"] = latest_news_title
    #mars_data["news_para"] = news_para
    
    #---------------------
    #JPL Mars Space Images - Featured Image

    #visit
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    time.sleep(1)

    #scrape page into soup
    img_html = browser.html
    soup = BeautifulSoup(img_html, 'html.parser')

    #get the image url for the current Featured Mars Image 
    featured_image_url = soup.find("div", class_="floating_text_area").a["href"]

    #getting the image
    featured_image_url = "https://spaceimages-mars.com/" + featured_image_url
    
    #store data in dictionary
    featured_image_url = str(featured_image_url)
    
    #mars_data["featured_image_url"] = featured_image_url

    #---------------------------
    #Mars Facts

    #visit
    url = 'https://galaxyfacts-mars.com/'

    #get data from webpage
    mars_fact = pd.read_html(url)

    #slice off the dataframe that we want usin normal indexing
    mars_facts_df = mars_fact[0]
    mars_facts_df.columns = ["Description", "Mars", "Earth"]

    #set index to description column
    mars_facts_df.set_index("Description", inplace=True)

    #convert to HTML
    html_table = (mars_facts_df.to_html()).replace('\n', '')

    #store data in dictionary
    html_table = (html_table)
    
    #mars_data["facts_table"] = html_table

    #-------------------------------
    #marshemispheres cerberus

    #visit
    url = "https://marshemispheres.com/cerberus.html"
    browser.visit(url)
    time.sleep(1)

    hemisphere_image_urls = []

    #scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #get the image url of cerberus 
    image_url = soup.find("img", class_="wide-image")["src"]
    cerberus_url = "https://marshemispheres.com/" + image_url
    cerberus_url = str(cerberus_url)

    #get the Hemisphere title
    cerberus_img_title = soup.find("h2", class_="title").text
    cerberus_img_title = str(cerberus_img_title)
       
    #store data in dictionary
    #mars_data["hemisphere_urls"] = hemisphere_image_urls
    #hemisphere_image_urls.append([{"title": cerberus_img_title, "img_url": cerberus_url}])

    hemisphere_image_urls.append({"title": cerberus_img_title, "img_url": cerberus_url})

    #-------------------------------
    #marshemispheres schiaparelli

    #visit
    url = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url)
    time.sleep(1)

    #scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #get the image url of cerberus 
    image_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_url = "https://marshemispheres.com/" + image_url
    schiaparelli_url = str(schiaparelli_url)

    #get the Hemisphere title
    schiaparelli_img_title = soup.find("h2", class_="title").text
    schiaparelli_img_title = str(schiaparelli_img_title)

    hemisphere_image_urls.append({"title": schiaparelli_img_title, "img_url": schiaparelli_url})

   #-------------------------------
    #marshemispheres syrtis

    #visit
    url = "https://marshemispheres.com/syrtis.html"
    browser.visit(url)
    time.sleep(1)

    #scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #get the image url of cerberus 
    image_url = soup.find("img", class_="wide-image")["src"]
    syrtis_url = "https://marshemispheres.com/" + image_url
    syrtis_url = str(syrtis_url)

    #get the Hemisphere title
    syrtis_img_title = soup.find("h2", class_="title").text
    syrtis_img_title = str(syrtis_img_title)

    hemisphere_image_urls.append({"title": syrtis_img_title, "img_url": syrtis_url})

   #-------------------------------
    #marshemispheres valles

    #visit
    url = "https://marshemispheres.com/valles.html"
    browser.visit(url)
    time.sleep(1)

    #scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #get the image url of cerberus 
    image_url = soup.find("img", class_="wide-image")["src"]
    valles_url = "https://marshemispheres.com/" + image_url
    valles_url = str(valles_url)

    #get the Hemisphere title
    valles_img_title = soup.find("h2", class_="title").text
    valles_img_title = str(valles_img_title)

    hemisphere_image_urls.append({"title": valles_img_title, "img_url": valles_url})

    # Closing the browser after scraping
    browser.quit()

    #-------------------------------
    #storing values into directory
    
    mars_data = {
        "news_title": latest_news_title,
        "news_para": news_para,
        "featured_image_url": featured_image_url,
        "facts_table": html_table, 
        "hemisphere_images": hemisphere_image_urls
    }

    # Return the mars_data dict
    return mars_data




   




