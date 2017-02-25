from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Users\elkha\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("http://isthisprime.com/game/")

elem = driver.find_element_by_id("start")


def isPrime(n):
    if n==1:
        return False
    for i in range(2,long(n**0.5)+1):
        if n%i==0  :
            return False

    return True

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

    if(isPrime(primeNum)):
        yes.click()
    else:
        no.click()

driver.close()






