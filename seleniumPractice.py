from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

name_txbox="//input[@type='text' and @id='name']"
city_txbox="//input[@type='text' and @id='city']"
enter_data_button="//button[@type='button' and @id='enter']"
close_btn="//button[text()='Close']"
driver = webdriver.Chrome(
            executable_path="C:\\Users\\NE20081402\\Downloads\\chromedriver_win32\\chromedriver.exe")
baseUrl="file:///C:/Users/NE20081402/Downloads/AutomationChallengeIDC/index.html"
driver.get(baseUrl)
driver.find_element_by_xpath("//button[contains(text(),'Open Modal')]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath(name_txbox).send_keys("hema")
driver.find_element_by_xpath(city_txbox).send_keys("cityvalue")
driver.find_element_by_xpath(enter_data_button).click()
driver.find_element_by_xpath(close_btn).click()


