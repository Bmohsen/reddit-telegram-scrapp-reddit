from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.firefox.options import Options
import datetime
import time
import requests
import random
import os
from os import path

from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.reddit.com/r/memes/"  # url for scrap
scrollPauseTime = 15  # scroll Pause time
t = datetime.datetime.now()
folderPath = "memes-" + str(t.year) + "-" + str(t.month) + "-" + str(t.day) + "-" + str(t.hour) + "-" + str(
    t.minute) + "-" + str(
    t.second)  # generate folder path for saving images each time script run
images_list = []  # local image list
images_url = []  # external image list

class Reddit:
    def dl_reddit_memes(self,step, scrollheight, headless, download):
        """
        @param step:step to scroll default : 5000
        @param scrollheight: scroll height of page
        @param headless: open driver GUI (True or false)
        @param download : (download memes localy?)True or false
        """
        self.scrollhight = scrollheight
        self.headless = headless
        self.download = download
        self.step = step

        options = Options()
        # change to false if you want to see firefox
        options.headless = self.headless
        counter = 5000
        # create new browser
        driver = webdriver.Firefox(options=options)
        try:
            print("loading page (it depeneds on your internet speed) ... please wait")
            # open the URL
            driver.get(url)
            # scroll the page
            while counter <= self.scrollhight:
                # excute javascript that scroll the page
                driver.execute_script("window.scrollTo(0," + str(counter) + ");")
                counter += self.step
                # time.sleep(1)
            time.sleep(scrollPauseTime)
            # check for path to not exists
            if not path.exists(folderPath) and self.download == True:
                # make new directory for images
                os.mkdir(folderPath)
                # loop through image src attributes
                for i in driver.find_elements_by_class_name('ImageBox-image'):
                    # check image source if faild to get
                    if i.get_attribute('src') != "None" or i.get_attribute('src') != "none":
                        # get the memes image url and append it to images_url list
                        images_url.append(i.get_attribute('src'))
                        # get image src binary
                        img = requests.get(i.get_attribute('src')).content
                        if(self.download == True):
                            # save each image into it file with random number
                            with open(imgName := folderPath + "/" + "meme-" + str(random.randrange(5000)) + ".jpg", "wb") as f:
                                f.write(img)
                                print(imgName + " downloaded into " + folderPath)
                            # success message
                            print("all memes downloaded succefully!")
                            # append image local name to images_list
                            images_list.append(imgName)
        # get the error on close the driver
        except StaleElementReferenceException:
            print(StaleElementReferenceException.msg)
            driver.close()
        driver.close()

