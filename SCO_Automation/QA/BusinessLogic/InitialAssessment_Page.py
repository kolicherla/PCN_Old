from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from QA.BusinessLogic.CreateJPCN_Page import createJPCN_Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from pathlib import Path
import sys

import time

class InitilaAssessment_Page():
    global objCommon, objActions, objConfig,objHome,objFilter
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()


    def InitialAssessment_ContextCE_Details(self,CCER,priorityType,CCERC,PCNTYPE,ASQNeeded,ASQNComments):
        time.sleep(2)
        objActions.selectDropdown(PCN.ContextCE_Recommendation_SelectBox_name, "name", "visibletext", CCER)
        time.sleep(2)
        objActions.enterText(PCN.ContextCE_RecommendationComments_WebEdit_name, "name", CCERC)
        objActions.selectDropdown(PCN.Priority_Type_selectBox_name, "name", "visibletext", priorityType)
        time.sleep(2)
        if PCNTYPE == 'EOL':
           time.sleep(2)
           objActions.selectDropdown(PCN.IA_Alternative_SourceQN_SelectBox_name, "name", "visibletext", ASQNeeded)
           time.sleep(2)
           objActions.enterText(PCN.IA_FFF_Alternative_SourceComments_WedEdit_name, "name", ASQNComments)
        #    assert PCNTYPE == 'EOL'
        # else:
        #     print("PCNType is not EOL"+PCNTYPE)

    def InitialAssessment_AddNewRecord(self,PR,Deviation,DeviationStatus,Seventeneleveen,JPN,MPN,HTR,MCOECO,
                                       QPET,Comments,JuniperAssembly):
        objActions.clickElement(PCN.IA_AddNewRecord_WebElement_xpath, "xpath")
        time.sleep(2)
        objActions.enterText(PCN.AddNewRecord_PR_WebEdit_name, "name", PR)
        objActions.enterText(PCN.AddNewReocrd_Deviation_WebEdit_name, "name", Deviation)
        objActions.selectDropdown(PCN.AddNewRecord_DeviationStatus_selectBox_name, "name", "visibletext",  DeviationStatus)
        time.sleep(3)
        objActions.enterText(PCN.AddNewRecord_710_711_WebEdit_name, "name", Seventeneleveen)
        objActions.enterText(PCN.AddNewRecord_JPN_WebEdit_name, "name", JPN)
        objActions.enterText(PCN.AddNewRecord_MPN_WebEdit_name, "name", MPN)
        objActions.enterText(PCN.AddNewRecord_HTR_WebEdit_name, "name", HTR)
        time.sleep(2)
        objActions.enterText(PCN.AddNewRecord_ECOMCO_WebEdit_name, "name", MCOECO)
        # objActions.enterText(PCN.AddNewRecord_ECOMCO_Status_WebEdit_name, "name", MCOECOStatus)
        objActions.enterText(PCN.AddNewRecord_qpet_WebEdit_name, "name", QPET)
        time.sleep(2)
        objActions.enterText(PCN.AddNewRecord_Comment_WebEdit_name, "name", Comments)
        objActions.enterText(PCN.AddNewRecord_JA_WebEdit_name, "name", JuniperAssembly)
        time.sleep(3)
        objActions.clickElement(PCN.AddNewAttachement_SubmitBtn_xpath, "xpath")


    def QualDataReview_Attachement(self,strFilePath,QualReportStatus,QualReportComments):
        time.sleep(2)
        objCommon.AttachFile(strFilePath, PCN.QualDataReview_Attachement_xpath, "xpath")
        objActions.clickElement(PCN.QualDataReview_Upload_xpath, "xpath")
        time.sleep(3)
        objActions.selectDropdown(PCN.QualReport_AcceptStaus_name, "name", "visibletext", QualReportStatus)
        time.sleep(3)
        objActions.enterText(PCN.QualReport_ReviewComments_name, "name", QualReportComments)
        time.sleep(2)

    def Complete_Assessment(self):
        time.sleep(2)
        objActions.clickElement(PCN.Complete_Assessment_Button_xpath, "xpath")
        time.sleep(2)

    def Submit_OnWarringWindow(self):
        time.sleep(2)
        objActions.clickElement(PCN.submit_button_xpath, "xpath")
        time.sleep(2)




    def InitialAssessment_Checking_AutoPopulationOfPCNCompliance(self,PCNTYPE,intEFRCDiff,intBRDiff,intSBDiff,ReasonforNC):
        time.sleep(2)
        objActions.ValidationOnSelectedtext(PCN.IA_PCNCompliance_SelectBox_name, "name")
        if (PCNTYPE ==('Process Change' or 'Design Change')):
            strPCNComplience = objActions.ValidationOnSelectedtext(PCN.IA_PCNCompliance_SelectBox_name, "name")
            if intEFRCDiff >= 90:
                if strPCNComplience == "Compliant":
                    print("Where:" +PCNTYPE+ "and Effective and Received date >=90 then PCN Compliance is Autopopulates to :" " "+strPCNComplience)
                    objCommon.capture_screenshot("PCN Compliance as: Compliant ")
                else:
                    print("PCNComplience dropdown displaying as :" " " +strPCNComplience+ "insted of : Compliant")
                    assert strPCNComplience == "Compliant"
            elif intEFRCDiff < 90:
                 if strPCNComplience == "Non-Compliant":
                    time.sleep(2)
                    objActions.selectDropdown(PCN.Reasonfor_NonCompliance_SelectBox_name, "name", "visibletext", ReasonforNC)
                    time.sleep(2)
                    print("Where:" +PCNTYPE+ "and Effective and Received date < 90 then PCN Compliance is Autopopulates to :" " "+strPCNComplience)
                    objCommon.capture_screenshot("PCN Compliance as: Non-Compliant ")
                 else:
                    print("PCNComplience dropdown displaying as :" " " +strPCNComplience+ "insted of: Non-Compliant ")
                    assert strPCNComplience == "Non-Compliant"
        elif PCNTYPE == 'EOL':
             strPCNComplience = objActions.ValidationOnSelectedtext(PCN.IA_PCNCompliance_SelectBox_name, "name")
             if intBRDiff >= 180:
                 if strPCNComplience == "Compliant":
                     print("Where:" + PCNTYPE + "and Effective and Received date >=180 then PCN Compliance is Autopopulates to :" " " + strPCNComplience)
                     objCommon.capture_screenshot("PCN Compliance as: Compliant ")
                 else:
                     print("PCNComplience dropdown displaying as :" " " + strPCNComplience + "insted of : Compliant")
                     assert strPCNComplience == "Compliant"
             elif intBRDiff < 180:
                  if strPCNComplience == "Non-Compliant":
                      time.sleep(2)
                      objActions.selectDropdown(PCN.Reasonfor_NonCompliance_SelectBox_name, "name", "visibletext",  ReasonforNC)
                      time.sleep(2)
                      print("Where:" + PCNTYPE + "and Effective and Received date < 180 then PCN Compliance is Autopopulates to :" " " + strPCNComplience)
                      objCommon.capture_screenshot("PCN Compliance as: Non-Compliant ")
                  else:
                      print("PCNComplience dropdown displaying as :" " " + strPCNComplience + "insted of: Non-Compliant ")
                      assert strPCNComplience == "Non-Compliant"
             elif intSBDiff >= 180:
                 if strPCNComplience == "Compliant":
                     print("Where:" + PCNTYPE + "and Effective and Received date >=180 then PCN Compliance is Autopopulates to :" " " + strPCNComplience)
                     objCommon.capture_screenshot("PCN Compliance as: Compliant ")
                 else:
                     print("PCNComplience dropdown displaying as :" " " + strPCNComplience + "insted of : Compliant")
                     assert strPCNComplience == "Compliant"
             elif intSBDiff < 180:
                  if strPCNComplience == "Non-Compliant":
                      time.sleep(2)
                      objActions.selectDropdown(PCN.Reasonfor_NonCompliance_SelectBox_name, "name", "visibletext", ReasonforNC)
                      time.sleep(2)
                      print("Where:" + PCNTYPE + "and Effective and Received date < 180 then PCN Compliance is Autopopulates to :" " " + strPCNComplience)
                      objCommon.capture_screenshot("PCN Compliance as: Non-Compliant ")
                  else:
                      print("PCNComplience dropdown displaying as :" " " + strPCNComplience + "insted of: Non-Compliant ")
                      assert strPCNComplience == "Non-Compliant"
        else:
            print("Failed: PCN Compliance not displaying Expected values  and  conditions are not satisfied")
            objCommon.capture_screenshot("No Such element found")











# def days_between(self,strReceivedDate,strEffDate):
    #     PCNCalc = abs(int(strReceivedDate - strEffDate).days)
    #     return PCNCalc

    # def days_between(d1, d2):
    #     d2 = datetime.strptime(d2, "%28-%FEB-%Y")
    #     d1 = datetime.strptime(d1, "%d-%m-%Y")
    #     return abs((d2 - d1).days




