import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


class twitterBot:

    def __init__(self, username, password, tweet):
        self.tweet = tweet
        self.username = username
        self.password = password

    def tweeter(self):
        executable_path = r'chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        driver = webdriver.Chrome(executable_path=executable_path,options=options)
        driver.get('https://twitter.com/login')

        while True:
            try:
                user = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
                user.send_keys(self.username)
                passwords = driver.find_element_by_xpath(
                    '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
                passwords.send_keys(self.password)
                driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
                break
            except NoSuchElementException:
                driver.implicitly_wait(30)
                user = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/form/div/div['
                                                    '1]/label/div/div[2]/div/input')
                user.send_keys(self.username)
                passwords = driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[1]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
                passwords.send_keys(self.password)
                driver.find_element_by_xpath(
                    '//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div').click()
                break

        driver.implicitly_wait(30)

        driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div['
                                     '2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div['
                                     '1]/div/div/div/div[2]/div/div/div/div').send_keys(self.tweet)

        driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/div['
                                     '2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span').click()
        time.sleep(0.5)

        driver.quit()
