# sudo mv geckodriver /usr/local/bin
# https://github.com/mozilla/geckodriver/releases



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import random

# ulozeno secret var s pluginem env file luxus vec

user_name = os.environ.get("U_NAME")
user_pass =os.environ.get("U_PASSWORD")

# print(user_name)
# print(user_pass)



class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closebrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        login_button = driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]')
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_photos(self, hashtag):
        driver = self.driver

        # vyhleda hashtag
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(2)

        # scrollovani dolu
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # hledani odkazu obrazku
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs
                             if '.com/p/' in elem.get_attribute('href')]
        [pic_hrefs.append(href) for href in hrefs if href not in pic_hrefs]
        print(hashtag+" - Check: pic href length " + str(len(pic_hrefs)))

        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                driver.find_element_by_xpath('//span[@aria-label="Like"]').click()

                for second in reversed(range(0, random.randint(18, 28))):
                    print("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1


hashtags = ['rathause','townhall']

jacobs_instabot = InstagramBot(user_name, user_pass)
jacobs_instabot.login()

while True:
    try:
        # náhodně vybere hashtag
        tag = random.choice(hashtags)
        jacobs_instabot.like_photos(tag)
    except Exception:
        jacobs_instabot.closebrowser()
        time.sleep(60)
        jacobs_instabot = InstagramBot(user_name, user_pass)
        jacobs_instabot.login()

