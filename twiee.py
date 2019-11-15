from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import time

opt= webdriver.ChromeOptions()
opt.add_argument('headless') #Don't open 

#path for windows 'C:\\Python37\\chromedriver.exe'
driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=opt)

pixel =0
def HashTag(keyword):

	global pixel
	url = 'https://twitter.com/hashtag/' + keyword
	driver.get(url)
	time.sleep(3)

	for i in range(1):
		driver.execute_script("window.scrollTo(0, {})".format(pixel)) 
		time.sleep(1)
		pixel= pixel+10000


	page_html = driver.page_source
	data = soup(page_html,'html.parser')

	tweetext = data.findAll('p',{'class':'TweetTextSize'})
	tweetuser =data.findAll('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'})
	
	#print(tweetuser)

	result = []

	for i ,tw in enumerate(zip(tweetuser,tweetext)):
		print(i+1)
		user=tw[0].text
		user= user.replace('\n','')
		user= user.replace('\u200f\xa0','')
		print(user)
		# print([tw[0].text])
		print('https://twitter.com'+tw[0]['href'])
		print(tw[1].text)
		print('-------------')
		result.append({'user':user,'url':url,'tweet':tw[1].text})

	driver.close()
	return result

HashTag('ประวิทย์')

# <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">ＫＲＡＩＳＩＲＩ、</strong>
# <span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>wdilbib_</b></span>

# <a class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/wdilbib_" data-user-id="333848565">
#       <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/542525390040756226/WDATowDB_bigger.jpeg" alt="">
#     <span class="FullNameGroup">
#       <strong class="fullname show-popup-with-id u-textTruncate " data-aria-label-part="">ＫＲＡＩＳＩＲＩ、</strong><span>&rlm;</span><span class="UserBadges"></span><span class="UserNameBreak">&nbsp;</span></span><span class="username u-dir u-textTruncate" dir="ltr" data-aria-label-part="">@<b>wdilbib_</b></span></a>