class openModal:
    navigate_home="//a[contains(text(),'Home')]"
    open_modal_button="//button[contains(text(),'Open Modal')]"
    name_txbox="//input[@type='text' and @id='name']"
    city_txbox="//input[@type='text' and @id='city']"
    enter_data_button="//button[@type='button' and @id='enter']"
    close_btn="//button[text()='Close' and @type='button']"

    def __init__(self,driver):
        self.driver=driver

    def clickHome(self):
        self.driver.find_element_by_xpath(self.navigate_home).click()
    def clickOpenModel(self):
        self.driver.find_element_by_xpath(self.open_modal_button).click()
        self.driver.implicitly_wait(5)
    def setName(self,name):
        self.driver.find_element_by_xpath(self.name_txbox).clear()
        self.driver.find_element_by_xpath(self.name_txbox).send_keys(name)
    def setCity(self,city):
        self.driver.find_element_by_xpath(self.city_txbox).clear()
        self.driver.find_element_by_xpath(self.city_txbox).send_keys(city)
    def dataEnter(self):
        self.driver.find_element_by_xpath(self.enter_data_button).click()
        #self.driver.implicitly_wait(5)

    def clickClose(self):
        self.driver.find_element_by_xpath(self.close_btn).click()






