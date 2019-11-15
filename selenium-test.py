# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup as soup
# driver = webdriver.Chrome()

# #url = 'https://google.com'
# url = 'https://twitter.com/hashtag/%E0%B8%AB%E0%B8%99%E0%B8%B8%E0%B9%88%E0%B8%A1%E0%B9%81%E0%B8%A7%E0%B9%88%E0%B8%99%E0%B8%AB%E0%B8%B1%E0%B8%A7%E0%B8%A3%E0%B9%89%E0%B8%AD%E0%B8%99'
# driver.get(url)
# page_html = driver.page_source
# data = soup(page_html,'html.parser')
# tweetext =data.findAll('p',{'class':'TweetTextSize'})

# for i ,tw in enumerate(tweetext):
# 	print(i)
# 	print(tw.tweetext)





# print(driver.page_source)






# elem_search = driver.find_element_by_name("q")
# elem_search.clear()
# elem_search.send_keys("tzcctv")
# elem_search.send_keys(Keys.ENTER)