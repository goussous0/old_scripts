import requests
import time
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options



# setting up headless option for faster execution
options = Options()
options.headless = True


# a search function  to go through the html_source and find the device's vendor
def search_function(html_output):
    lines = html_output.splitlines()
    for line in lines:
        for i in range (len(line)):
            if line[i:i+17]=="""<div id="vendor">""":
                line = line.replace('<div id="vendor">','')
                line = line.replace('</div>','')
                line = line.strip()
                print ("The following Device is : \n"+str(line))
    return
    
## take input as a mac address from the user
x = str(input("Please input a vailed ip address: \n"))
#req = requests.get('https://macvendors.com/')

browser = (webdriver.Firefox(options=options))
browser.get('https://macvendors.com/')
assert 'MAC Vendor Lookup Tool & API' in browser.title
elem = browser.find_element_by_id('macaddress')
elem.send_keys(x + Keys.RETURN)
time.sleep (2)
    

html_ouput = browser.page_source
search_function(html_ouput)



browser.quit()
