import time
from selenium import webdriver
browser = webdriver.Chrome('/Users/manlai/Downloads/chromedriver')

while True:
    browser.get('https://cats.cs61a.org') 
    time.sleep(1)

    browser.find_element_by_xpath('//button[text()="Single Player"]').click()

    letters = browser.find_elements_by_class_name('Character')
    inputElement = browser.find_element_by_class_name('InputField')
    elapsed = browser.find_elements_by_class_name('Indicator')[2]
    time.sleep(1)

    for letter in range(len(letters)-2):
        inputElement.send_keys(letters[letter].text)

    while((len(letters)-2) / 5. * 60. / float(elapsed.text[6:]) > 250.5):
        pass
    inputElement.send_keys(letters[len(letters)-2].text)
    time.sleep(1)

    wpm = float(browser.find_element_by_class_name('Indicator').text[5:])
    username = browser.find_element_by_class_name('form-control')
    username.send_keys("python")
    browser.find_element_by_xpath('//button[text()="Submit"]').click()
    time.sleep(1)
