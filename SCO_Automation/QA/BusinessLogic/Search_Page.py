from QA.Utilities.PerformAction import PerformActions
from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from QA.BusinessLogic.CreateJPCN_Page import createJPCN_Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from pathlib import Path
from selenium import webdriver
import sys
import datetime
from pytz import timezone
import time

class Search_Page():
    global objCommon, objActions ,objConfig,objFilter,objHome,objCreateJPCN
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()
    objCreateJPCN = createJPCN_Page()

    def Search_For_ClosedPCN_And_ClickEditIcon(self):
        strPages = objActions.getText(PCN.Search_TablePage_Count_xpath, "xpath")
        strPagesCount = strPages.split(" ")
        PageCount = int(strPagesCount[4])
        # GetPagesLinks=MyConfigFiles.driver.find_elements_by_xpath("//div[@class='content']//li//a")
        # PageCount=len(GetPagesLinks)
        print(PageCount)
        objTablerow = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='created-jpcn']/tbody/tr")
        intRowCount = len(objTablerow)
        print("Rows Count in page  is: " + str(intRowCount - 1))
        flag = False
        for t in range(1, PageCount + 1):
            # t=t+1
            # strt = str(t+1)
            # if t==PageCount-1:
            # break
            for i in range(2, intRowCount + 1):
                stri = str(i)
                strJCPNStage = objActions.getText("//table[@id='created-jpcn']/tbody/tr[" + stri + "]/td[7]", "xpath")
                if strJCPNStage == "Core CE Assessment":
                    EditIconExists = objActions.ObjectExists("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[2]//img[@class='editIcon iconLink']", "xpath")
                    # CoreCEAssessment_JPCNNumber = objActions.getText("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[3]")
                    CoreCEAssessment_JPCNNumber = MyConfigFiles.driver.find_element_by_xpath("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[3]").text
                    objActions.clickElement("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[2]//img[@class='editIcon iconLink']", "xpath")
                    if EditIconExists == True:
                        flag = True
                        print("Able to edit Closed JPCN")
                        break
            if flag == True:
                break
            elif t == PageCount:
                break
            else:
                time.sleep(2)
                objActions.clickElement("//a[text()='" + str(t + 1) + "']", "xpath")
                time.sleep(2)
        if flag == False:
            sys.exit("FAILED:: Could not find the JPCNNumber ")
        else:
            print("Core CE Assessment JPCN is " +CoreCEAssessment_JPCNNumber+ "and successfully clicked edit icon")
        return CoreCEAssessment_JPCNNumber



