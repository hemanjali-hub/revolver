import  pytest
from selenium import webdriver
from DataDD.TestCases import conftest


from DataDD.pageObjects.firsttest import openModal


class test001_OpenModal:
    baseUrl="file:///C:/Users/NE20081402/Downloads/AutomationChallengeIDC/index.html"
    name="hemanjali"
    city="somecity"

    def testPage(self,setup):
        #self.driver=webdriver.Chrome(ChromeDriverManager().install(ChromeType.GOOGLE,))
        self.driver=setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        page_title=self.driver.title
        print(page_title)
        if page_title=='Home':
            assert True
        else:
            assert False

    def testOpenModal(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.om=openModal(self.driver)
        self.om.clickHome()
        self.om.clickOpenModel()

        self.om.setName(self.name)
        self.om.setCity(self.city)
        self.om.dataEnter()
        self.om.clickClose()

# tom=test001_OpenModal()
# tom.testPage()
# tom.testOpenModal()




