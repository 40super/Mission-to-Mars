#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


import pandas as pd


# In[3]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


slide_elem.find('div', class_='content_title')


# In[7]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()


# ### Featured Images 

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')



# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'



# In[14]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)



# In[15]:


df.to_html()


# In[16]:


browser.quit()


# In[92]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[6]:


slide_elem.find('div', class_='content_title')


# In[7]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[93]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[94]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[95]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[96]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[97]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[98]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[99]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)



# In[17]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[85]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[86]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

html = browser.html
html_soup = soup(html, 'html.parser')


# In[87]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
# 3. Write code to retrieve the image urls and titles for each hemisphere.
item_box = html_soup.find('div', class_='collapsible results')
src_image = item_box.find_all('div' , class_='description')
for item in src_image:
    hemisphere ={}
    source_link = item.findChild()
    source = source_link.get('href')
    i_url = f'https://marshemispheres.com/{source}'
    browser.visit(i_url)
    print("Success")
    browser.is_element_present_by_css('div.list_text', wait_time=3)
    html = browser.html
    html_soup = soup(html, 'html.parser')
    item_link = html_soup.find('div' , class_='downloads')
    item_desc = html_soup.find('h2' , class_='title').text
    src_l = item_link.findChildren(name='a')[0].get('href')
    hemisphere = {"img_url":f'https://marshemispheres.com/{src_l}',"title":item_desc}
    hemisphere_image_urls.append(hemisphere)
    print(item_desc)
    browser.back()
    


# In[89]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[100]:


# 5. Quit the browser
browser.quit()


# In[ ]:




