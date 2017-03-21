from selenium import webdriver
from itertools import count, islice
from math import sqrt
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Users\elkha\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("http://isthisprime.com/game/")

elem = driver.find_element_by_id("start")


def is_Prime(n):
    return n > 1 and all(n%i for i in islice(count(2), long(sqrt(n)-1)))

elem.click()
yes = driver.find_element_by_id("yes")
no = driver.find_element_by_id("no")
timeCounter = driver.find_element_by_id('time')
timeCount = timeCounter.text
while timeCount != '0':
    primeText = driver.find_element_by_id('n')
    try:
        primeNum = int(primeText.text)
    except:
        primeNum = 0

    if(is_Prime(primeNum)):
        yes.click()
    else:
        no.click()

driver.close()






