from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pathlib import Path
import sys

import time

class JPCNstatusoverview_Page():
    global objCommon, objActions ,objConfig,objFilter,objHome
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()

    def ClickContextCE_Create_Items(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_CreateItem_WebElement_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on Create Item Sections')

    def ClickContextCE_InitialAssessment_Items(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_InitialAssessment_WebElement_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on InitialAssessment Sections')

    def ClickDashboard_Link(self):
        time.sleep(3)
        html = MyConfigFiles.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_Button_xpath, "xpath")
        assert (objActions.AssertObjectExists(PCN.DashBoard_Button_xpath, "xpath"))
        print("Dashboard link clicked sucessfully")

    def ClickCoreCE_AssesmnetPending_Items(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_CoreCEAssessment_WebElement_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on CoreCE Assessment Item Sections')
        time.sleep(3)




    def SelectJCPN(self,JCPNInput):
        global flag
        time.sleep(2)
        # self.ClickContextCE_Create_Items()
        strPages=objActions.getText(PCN.ContextCE_TablePage_Count_xpath,"xpath")
        strPagesCount=strPages.split(" ")
        intPagesCount=int(strPagesCount[4])
        if intPagesCount <= 1:
            time.sleep(30)
        # print("Number of pages displayed: "+str(intPagesCount))
        flag=False
        for pages in range(1,intPagesCount+1):
            objTable=MyConfigFiles.driver.find_elements_by_xpath("//table[@id='created-jpcn']/tbody/tr")
            intRowCount=len(objTable)
            # print("Rows Count in page "+str(pages)+" is: "+str(intRowCount-1))
            for i in range(2,intRowCount+1):
                stri=str(i)
                strJCPN=objActions.getText("//table[@id='created-jpcn']/tbody/tr["+stri+"]/td[2]","xpath")
                # print(strJCPN)
                if strJCPN==JCPNInput:
                    time.sleep(2)
                    objActions.clickElement("//table[@id='created-jpcn']/tbody/tr["+stri+"]/td[2]","xpath")
                    flag=True
                    # print("JPCN is displayed on Page: "+str(pages))
                    break
                    time.sleep(10)
            if flag==True:
                break
            else:
                time.sleep(3)
                objActions.clickElement("//a[text()='"+str(pages+1)+"']","xpath")
                time.sleep(4)
        if flag==False:
            sys.exit("FAILED:: Could not find the JPCNNumber: "+JCPNInput)

    def SendBack_with_AssignBacktoContextCE(self,AssginbackComments):
        time.sleep(2)
        objActions.clickElement(PCN.JPCNStatus_Overivew_Button_xpath, "xpath")
        time.sleep(3)
        objActions.enterText(PCN.AssignBack_Comments_WebEdit_xpath, "xpath", AssginbackComments)
        time.sleep(2)
        assert (objActions.AssertObjectExists(PCN.submit_button_xpath, "xpath"))
        objActions.clickElement(PCN.submit_button_xpath, "xpath")
        objCommon.capture_screenshot("Sendback to Context CE")

    def Reassign_Assessment(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_ReassignAssessment_WebElement_xpath, "xpath")

    def Validation_OnCoreCE_ManadtoryFields(self,strFilePath,QRAS,QRRC,CoreCERecommendations,CoreCeREComments,ReasonforNC):
        time.sleep(2)
        # objCommon.AttachFile(strFilePath, PCN.QualDataReview_CoreCE_Attachement_xpath, "xpath")
        # time.sleep(3)
        # objActions.clickElement(PCN.QualDateReview_CoreCe_Upload_xpath, "xpath")
        # time.sleep(4)
        time.sleep(2)
        objActions.selectDropdown(PCN.QualReport_AcceptStaus_CoreCE_xpath, "xpath", "visibletext", QRAS)
        time.sleep(3)
        objActions.enterText(PCN.QualReport_ReviewComments_CoreCE_xpath, "xpath", QRRC)
        time.sleep(2)
        objActions.selectDropdown(PCN.CoreCe_Recommendation_name, "name", "visibletext", CoreCERecommendations)
        time.sleep(2)
        objActions.enterText(PCN.CoreCe_Recommendation_comments_name, "name", CoreCeREComments)
        time.sleep(3)
        self.CoreCE_PCN_ChangeComplianceSelect_Validations(ReasonforNC)
        time.sleep(2)
        strMsg1=objActions.getText(PCN.CoreCE_ChangeStatus_xapth, "xpath")
        strMsg2=objActions.getText(PCN.CoreCE_Gobackmsg_xpath, "xpath")
        strValidationMsg= strMsg1 + strMsg2
        time.sleep(2)
        print("Display Validations message" +strValidationMsg)
        time.sleep(2)


    def Goabck_button(self):
        time.sleep(3)
        objActions.clickElement(PCN.Goback_Button_xpath, "xpath")
        time.sleep(3)
        # self.CoreCE_PCN_ChangeComplianceSelect_Validations(ReasonforNC)

    def Submit_CoreCE_Assessment(self):
        objActions.clickElement(PCN.submit_button_xpath, "xpath")
        time.sleep(3)
        objActions.clickElement(PCN.DashBoard_CoreCECompAssessment_WebElement_xpath, "xpath")
        time.sleep(3)
        self.SelectJCPN()
        time.sleep(3)
        JPCNStatus=objActions.getText(PCN.JPCN_Analyis_Stage_Status_xpath, "xpath")
        print("JPCN Analyis stage is completed sucessfully" +JPCNStatus)
        objCommon.capture_screenshot("JPCN Closed sucessfully")



    def CoreCE_PCN_ChangeComplianceSelect_Validations(self,ReasonforNC):
        time.sleep(3)
        # strPCNComplience = objActions.getText(PCN.PCNCompliance_CoreCE_SelectBox_xpath, "xpath")
        strPCNComplience = objActions.ValidationOnSelectedtext(PCN.Compliance_CoreCE_SelectBox_xpath, "xpath")
        print(strPCNComplience)
        time.sleep(2)
        if strPCNComplience == "Compliant":
            time.sleep(2)
            objActions.selectDropdown(PCN.Compliance_CoreCE_SelectBox_xpath, "xpath", "visibletext", "Non-Compliant")
            time.sleep(2)
            objActions.selectDropdown(PCN.PCNReason_NonCompliance_CoreCE_SelectBox_xpath, "xpath", "visibletext", ReasonforNC)
        else:
            time.sleep(2)
            objActions.selectDropdown(PCN.Compliance_CoreCE_SelectBox_xpath, "xpath", "visibletext", "Compliant")
            time.sleep(2)
            objActions.enterText(PCN.CoreCE_Justifications_name, "name", "Justificaion")
            time.sleep(3)
        objActions.clickElement(PCN.Complete_Assessment_Button_xpath, "xpath")


















