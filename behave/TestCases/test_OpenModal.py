import  pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
#from webdriver_manager.chrome import ChromeDriverManager
from behave.pageObjects.firsttest import openModal



class test001_OpenModal:
    baseUrl="file:///C:/Users/NE20081402/Downloads/AutomationChallengeIDC/index.html"

    def testPage(self):
        #self.driver=webdriver.Chrome(ChromeDriverManager().install(ChromeType.GOOGLE,))
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\NE20081402\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get(self.baseUrl)
        page_title=self.driver.title
        print(page_title)
        if page_title=='Home':
            assert True
        else:
            assert False

    def testOpenModal(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\NE20081402\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.get(self.baseUrl)
        self.om=openModal(self.driver)
        self.om.clickHome()
        self.om.clickOpenModel()
        self.om.setName("hemanjali")
        self.om.setCity("somecity")
        self.om.dataEnter()
        self.om.clickClose()

tom=test001_OpenModal()
tom.testPage()
tom.testOpenModal()




