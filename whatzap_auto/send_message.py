import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

base_url = 'https://api.whatsapp.com/send?phone='
chromedriver = "/Users/michaelmathew/gitlibs/FunWorks/whatzap_auto/chromedriver"
firefoxdriver = "/Users/michaelmathew/gitlibs/FunWorks/whatzap_auto/geckodriver"
chrome_executable_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
firefox_executable_path = '/Applications/Firefox.app/Contents/MacOS/firefox'
defaultChromeProfile = '/Users/michaelmathew/Library/Application Support/Google/Chrome/Profile 1'

os.environ["webdriver.chrome.driver"] = chromedriver
os.environ["webdriver.firefox.driver"] = firefoxdriver

phone_number = 447449737838
message = 'I am interested in your car for sale'

split_message = message.split(' ')
urlformatted_msg = ''
for msg_chunk in split_message:
	urlformatted_msg = urlformatted_msg + msg_chunk + '%20'

final_url = base_url + str(phone_number) + '&text=' + urlformatted_msg

# options = webdriver.ChromeOptions() 
# options.add_argument(defaultChromeProfile) #Path to your chrome profile
# driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

driver = webdriver.Firefox()

# Go to your page url
driver.get(final_url)

print final_url

raw_input()

# Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
button_element = driver.find_element_by_id('action-button')
button_element.click()

raw_input()

elem = driver.find_element_by_name("q")
elem.send_keys(Keys.RETURN)

ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    #print ii.tag_name
    print ii.get_attribute('id')