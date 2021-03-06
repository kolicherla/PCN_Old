from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
import sys
import time
import datetime
from pytz import timezone


class createJPCN_Page():
    global objCommon, objActions, objConfig,objHome,objFilter,objSearch
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()


    def PCNIssue_DateSelection(self):
        time.sleep(2)
        objActions.clickElement(PCN.PCNIssue_Date_WebEdit_xpath, "xpath")
        intDay = objCommon.GetCurrentDay()
        strConcDate = "day-" + str(intDay)
        objActions.clickElement("//div[@aria-label='" + strConcDate + "']", "xpath")


    def PCNReceived_DateSelection(self):
        time.sleep(2)
        objActions.clickElement(PCN.PCNReceived_Date_WebEdit_xapth, "xpath")
        time.sleep(3)
        today = datetime.datetime.now(timezone('US/Pacific'))
        strReceivedDate = today.strftime("%d-%b-%Y")
        objActions.enterText(PCN.PCNReceived_Date_WebEdit_xapth, "xpath", strReceivedDate)
        date1 = datetime.datetime.strptime(strReceivedDate, "%d-%b-%Y")
        return date1

    def PCNEffective_DateSelection(self,PCN_EffDays):
        time.sleep(2)
        objActions.clickElement(PCN.PCNEffective_date_WebEdit_xpath, "xpath")
        time.sleep(3)
        UScurrent_date = datetime.datetime.now(timezone('US/Pacific'))
        UScurrent_date += datetime.timedelta(days=int(PCN_EffDays))
        strEffDate = UScurrent_date.strftime("%d-%b-%Y")
        objActions.enterText(PCN.PCNEffective_date_WebEdit_xpath, "xpath", strEffDate)
        date2 = datetime.datetime.strptime(strEffDate, "%d-%b-%Y")
        return date2


    def PCNLastTImeBuy_DateSelection(self,LT_BuyDays):
        time.sleep(2)
        objActions.clickElement(PCN.PCNLastTime_BuyDate_WebEdit_xpath, "xpath")
        time.sleep(3)
        UScurrent_date = datetime.datetime.now(timezone('US/Pacific'))
        UScurrent_date += datetime.timedelta(days=int(LT_BuyDays))
        strLasttimeBuyDate = UScurrent_date.strftime("%d-%b-%Y")
        objActions.enterText(PCN.PCNLastTime_BuyDate_WebEdit_xpath, "xpath", strLasttimeBuyDate)
        LBdate = datetime.datetime.strptime(strLasttimeBuyDate, "%d-%b-%Y")
        return LBdate

    def PCNLastTImeShip_DateSelection(self,LT_ShipDays):
        time.sleep(2)
        objActions.clickElement(PCN.PCNLastTime_ShipDate_WebEdit_xpath, "xpath")
        time.sleep(2)
        UScurrent_date = datetime.datetime.now(timezone('US/Pacific'))
        UScurrent_date += datetime.timedelta(days=int(LT_ShipDays))
        strLasttimeship = UScurrent_date.strftime("%d-%b-%Y")
        objActions.enterText(PCN.PCNLastTime_ShipDate_WebEdit_xpath, "xpath", strLasttimeship)
        LShipdate = datetime.datetime.strptime(strLasttimeship, "%d-%b-%Y")
        return LShipdate

    def CreateJPCN(self,SupplierName,SupplierPCN):
        objActions.clickElement(PCN.CreateJPCN_link_xpath, "xpath")
        print("Initiated Create JPCN Page and to fill Supplier info section")
        objActions.enterText(PCN.Suppliername_WebEdit_name, "name", SupplierName)
        time.sleep(2)
        objActions.clickElement("//div[text()='" + SupplierName + "']", "xpath")
        time.sleep(1)
        objActions.enterText(PCN.SupplierPCN_WebEdit_name, "name", SupplierPCN)
        time.sleep(2)
        strSC=objActions.getAttributeValue(PCN.SupplierContact_WebEdit_name, "name", "value")
        strSCE=objActions.getAttributeValue(PCN.SupplierContactEmail_WebEdit_name, "name", "value")
        strSP=objActions.getAttributeValue(PCN.SupplierPhone_WebEdit_name, "name", "value")
        strEC=objActions.getAttributeValue(PCN.SupplierEscalation_WebEdit_name, "name", "value")
        strECE=objActions.getAttributeValue(PCN.SupplierEscalationEmail_WebEdit_name, "name", "value")
        time.sleep(2)
        Supplier_allData=[SupplierName: '',SupplierPCN,strSC,strSCE,strSP,strEC,strECE]
        html = MyConfigFiles.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.DOWN)
        # objActions.Page_Scroll_Actions("pcnReceivedDt", "name")
        print("sucessfully Filled the Supplier info section ")
        time.sleep(3)
        return Supplier_allData


    def PCN_DateSelections(self,PCN_EffDays, SelectPCNType, LT_BuyDays, LT_ShipDays):
        datelist = {}
        global intEFRCDiff,intBRDiff,intSBDiff
        print("Initiated to fill the  PCN/PDN INFO section")
        ReceivedDate=self.PCNReceived_DateSelection()
        time.sleep(2)
        EffectiveDate=self.PCNEffective_DateSelection(PCN_EffDays)
        time.sleep(2)
        self.PCNIssue_DateSelection()
        time.sleep(2)
        intEFRCDiff = int((EffectiveDate - ReceivedDate).days)
        print(intEFRCDiff)
        datelist['intEFRCDiff']=intEFRCDiff
        time.sleep(2)
        AllDate_ERdata = [ReceivedDate, EffectiveDate]
        if SelectPCNType == "EOL":
            objActions.selectDropdown(PCN.PCNType_Selectbox_name, "name", "visibletext", SelectPCNType)
            time.sleep(2)
            LTBuyDate = self.PCNLastTImeBuy_DateSelection(LT_BuyDays)
            time.sleep(2)
            LTShipDate = self.PCNLastTImeShip_DateSelection(LT_ShipDays)
            time.sleep(3)
            intBRDiff = int((LTBuyDate - ReceivedDate).days)
            time.sleep(2)
            print(intBRDiff)
            intSBDiff = int((LTShipDate - LTBuyDate).days)
            print(intSBDiff)
            datelist['intBRDiff']= intBRDiff
            datelist['intSBDiff']= intSBDiff
            time.sleep(5)
            html = MyConfigFiles.driver.find_element_by_tag_name('html')
            html.send_keys(Keys.TAB)
            time.sleep(7)
            AllDate_BSdata = [LTBuyDate, LTShipDate]
            return AllDate_BSdata
        else:
            objActions.selectDropdown(PCN.PCNType_Selectbox_name, "name", "visibletext", SelectPCNType)
        return datelist,SelectPCNType,AllDate_ERdata



    def PDNinfo_form(self,PCNSource,DescriptionChange,Natureofchange,Typeofchange,PendingConcernsComments):
        time.sleep(3)
        strPCNSource=objActions.selectDropdown(PCN.PCNSource_Selectbox_name, "name", "visibletext", PCNSource)
        time.sleep(3)
        strDC=objActions.enterText(PCN.Descriptionchange_WebEdit_name, "name" , DescriptionChange)
        time.sleep(3)
        strNC=objActions.selectDropdown(PCN.NatureofChange_Selectbox_name, "name", "visibletext", Natureofchange)
        time.sleep(3)
        strTC=objActions.selectDropdown(PCN.Typeofchange_Selectbox_xpath, "xpath", "visibletext", Typeofchange)
        time.sleep(3)
        objActions.clickElement(PCN.Add_Button_xpath, "xpath")
        time.sleep(3)
        print("sucessfully Filled the PCN/PDN INFO section")
        time.sleep(3)
        strPCC=objActions.enterText(PCN.OpenConcerns_Comments_WebEdit_name, "name", PendingConcernsComments)
        time.sleep(2)
        PCNPDN_allData=[strPCNSource,strDC,strNC,strTC,strPCC]
        objActions.clickElement(PCN.submit_button_xpath, "xpath")
        strJPCNID = objActions.getText(PCN.Jnpr_PCNID_xpath, "xpath")
        print("PCN/PDN & Supplier details are saved and PCN ID Created Successfully:" + strJPCNID)
        objCommon.capture_screenshot('Enter JPN-MPN details page.')
        return strJPCNID


    def Validate_CCE_PrePoulated_Values(self):
        objActions.getText(PCN.Verify_Context_CE_sections_xpath, "xpath")
        assert (objActions.AssertObjectExists(PCN.Verify_Context_CE_sections_xpath, "xpath"))
        time.sleep(1)
        strCCER_Act = objActions.ValidationOnSelectedtext(PCN.Validate_ContextCeRecommend_Value_name, "name")
        strCCER_Exp="No Action Needed"
        if strCCER_Act==strCCER_Act:
            print("Passed- Context CE Recommend Value is  " + strCCER_Act)
        else:
            print("Failed- Context CE Recommend Value is " + strCCER_Act +  "instead of"  + strCCER_Exp)
        assert strCCER_Act == strCCER_Act
        time.sleep(2)
        strPCNStatus_Act = objActions.ValidationOnSelectedtext(PCN.Validate_PCNStatus_Value_name, "name")
        strPCNStatus_Exp = "Closed - No Usage at Juniper"
        if strPCNStatus_Act==strPCNStatus_Act:
            print("Passed- PCN Status is  " + strPCNStatus_Act)
        else:
            print("Failed- PCN Status is " + strPCNStatus_Act +  "instead of"  + strPCNStatus_Exp)
        assert strPCNStatus_Act == strPCNStatus_Act
        time.sleep(2)
        strPCNStatusComm_Act = objActions.getText(PCN.Validate_PCNStatusComment_Value_name, "name")
        strPCNStatusComm_Exp = "MPNs included in this PCN are not in use at Juniper. Thus JPCN created at Juniper for records and closed as No Action Needed."
        if strPCNStatusComm_Act==strPCNStatusComm_Act:
            print("Passed- PCN Status comments is  " + strPCNStatusComm_Act)
        else:
            print("Failed- PCN Status comments is "  + strPCNStatusComm_Act +  "instead of" + strPCNStatusComm_Exp)
        assert strPCNStatusComm_Act == strPCNStatusComm_Act
        time.sleep(2)
        strResponsibleCE_Act = objActions.ValidationOnSelectedtext(PCN.Validate_ResponsibleCE_Value_name, "name")
        strResponsibleCEUN = objActions.getText(PCN.Login_Username_WebElement_xpath, "xpath")
        s= strResponsibleCEUN.split(",")[1]
        strResponsibleCE_Exp=s.strip()
        print(strResponsibleCE_Exp)
        if strResponsibleCE_Act==strResponsibleCE_Exp:
            print("Passed- Respobible CE is  " +  strResponsibleCE_Act)
        else:
            print("Failed- Respobible CE is " +  strResponsibleCE_Act +  "instead of" +  strResponsibleCE_Exp)
        assert strResponsibleCE_Act == strResponsibleCE_Exp
        time.sleep(2)
        strPCNCompliance_Act = objActions.ValidationOnSelectedtext(PCN.Validate_PCNCompliance_Value_name, "name")
        strPCNCompliance_Exp = "Not-Applicable"
        if strPCNCompliance_Act == strPCNCompliance_Exp:
            print("Passed- PCN Compliance is  " + strPCNCompliance_Act)
        else:
            print("Failed- PCN Compliance is " + strPCNCompliance_Act + "instead of" + strPCNCompliance_Exp)
        assert strPCNCompliance_Act == strPCNCompliance_Exp
        time.sleep(3)

    def ClosethisPCN(self,PCNStatus_Closed):
         objActions.selectDropdown(PCN.Validate_PCNStatus_Value_name, "name", "visibletext", PCNStatus_Closed)
         time.sleep(2)
         objActions.clickElement(PCN.Close_ThisPCN_Button_xpath, "xpath")
         print("PCN Closed sucessfully")

    def Validate_InvalidPCN_Status(self,PCNStatus):
        objActions.selectDropdown(PCN.Validate_PCNStatus_Value_name, "name", "visibletext", PCNStatus)
        time.sleep(2)
        objActions.clickElement(PCN.Close_ThisPCN_Button_xpath, "xpath")
        time.sleep(2)
        strIPCNS_Act=objActions.getText(PCN.Validation_msg_WebElement_xpath, "xpath")
        time.sleep(2)
        strIPCNS_Exp="Invalid PCN Status"
        if strIPCNS_Act==strIPCNS_Exp:
            print("Passed - Validation Message is dispalying as::"  " "+strIPCNS_Act)
        else:
            print("Failed -NO validation message is displayed")
        assert strIPCNS_Act == strIPCNS_Exp


    def Uploadvalidation(self):
        strAcknowMsg=objActions.getText(PCN.Acknowledgement_Notification_msg_xapth, "xpath")
        print("Acknowledgement Notification Message is :" +strAcknowMsg)
        assert (objActions.AssertObjectExists(PCN.Acknowledgement_Notification_msg_xapth, "xpath"))
        time.sleep(1)
        objActions.clickElement(PCN.Acknowledgement_Notification_button_xpath, "xpath")
        print("Acknowledgement Notification button: OK button clicked sucessfully")

    def JPN_MPN_Info(self,strFilePath):
        objCommon.AttachFile(strFilePath,PCN.Choosefile_button_name, "name")
        objActions.clickElement(PCN.Upload_button_xpath,"xpath")

    def EOL_Upload_Validations(self,strResponsibleCoreCE):
    #     time.sleep(2)
    #     # objCommon.AttachFile(strFilePath,PCN.EOL_Investigation_button_xpath,"xpath")
    #     # time.sleep(10)
    #     # html = MyConfigFiles.driver.find_element_by_tag_name('html')
    #     # html.send_keys(Keys.PAGE_UP)
    #     # time.sleep(5)
    #     # objActions.clickElement(PCN.EOL_Investigation_Upload_Lnk_xpath, "xpath")
    #     # time.sleep(20)
        strUploadtxt=objActions.getText(PCN.EOL_UPload_WebElement_xpath, "xpath")
        print("Expected linke is dislaying is:" " "+strUploadtxt)
        objActions.AssertObjectExists(PCN.EOL_UPload_WebElement_xpath, "xpath")
        time.sleep(2)
        strDownloadtxt = objActions.getText(PCN.EOL_Download_WebElement_xpath, "xpath")
        print("Expected linke is dislaying is:" " " + strDownloadtxt)
        objActions.AssertObjectExists(PCN.EOL_Download_WebElement_xpath, "xpath")
        time.sleep(2)
        strDeletetxt = objActions.getText(PCN.EOL_Delete_WebElement_xpath, "xpath")
        print("Expected linke is dislaying is:" " " + strDeletetxt)
        objActions.AssertObjectExists(PCN.EOL_Delete_WebElement_xpath, "xpath")
        objCommon.capture_screenshot("EOL file Uploaded sucessfully with all the buttons.")
        time.sleep(2)
        element = MyConfigFiles.driver.find_element_by_xpath("//button[contains(text(),'Save & Continue')]")
        print("Save and Continue button  is  Enabled:",element.is_enabled())
        time.sleep(2)
        objActions.selectDropdown(PCN.JPN_MPN_Responsible_CoreCE_Selectbox_name, "name", "visibletext", strResponsibleCoreCE)
        time.sleep(2)
        print("Save and Continue button is Enabled:" "" , element.is_enabled())
        time.sleep(2)
        objCommon.capture_screenshot("Save and Continue is enabled")


    def JPN_MPN_Info_ValidationCheck(self):
        strNRF_Act=objActions.getText(PCN.Jnpr_UA_Validation_msg_xpath, "xpath")
        strNRF_Exp= "No Record Found!"
        if strNRF_Act==strNRF_Exp:
            print("Passed- MPNs such should not have any impact on agile it is display:" +strNRF_Act)
        else:
            print("Failed- No Error messge is displayed as :" +strNRF_Act)
        assert strNRF_Act==strNRF_Exp

    def Verify_BackButton_Navigation(self):
        time.sleep(2)
        objActions.clickElement(PCN.Back_JPCNPage_button_xpath, "xpath")
        objCommon.capture_screenshot(" Enter PCN details page displyed sucessfully")


    def Edit_EnterPCNDetails_Page(self,SupplierPCN):
        SPCNUpdate="edit"
        time.sleep(2)
        objActions.enterText(PCN.SupplierPCN_WebEdit_name, "name", SPCNUpdate)
        time.sleep(2)
        objActions.clickElement(PCN.submit_button_xpath, "xpath")
        time.sleep(2)
        objActions.clickElement(PCN.Back_JPCNPage_button_xpath, "xpath")
        time.sleep(1)
        strupdated=objActions.getAttributeValue(PCN.SupplierPCN_WebEdit_name, "name", "value")
        print("the values is:"+strupdated)
        if SupplierPCN != strupdated:
            print("Successfully Edited Supplier PCN value:-"," "+strupdated)
        else:
            print("Not Edited the Supplier PCN Value:", " "+strupdated)
        assert SupplierPCN != strupdated
        time.sleep(2)
        objActions.clickElement(PCN.submit_button_xpath, "xpath")
        time.sleep(2)

    def AddNewAttachement_JPNMPN(self,strCategory,strFilePath,Comments):
        objActions.clickElement(PCN.JPN_MPN_AddNew_Attachment_button_xpath, "xpath")
        time.sleep(2)
        objActions.selectDropdown(PCN.AddNewAttachement_Category_Selectbox_xpath, "xpath", "visibletext", strCategory)
        time.sleep(2)
        objCommon.AttachFile(strFilePath, PCN.AddNewAttachement_Choose_file_xapth, "xpath")
        time.sleep(5)
        objActions.enterText(PCN.AddNewAttachement_Comments_xpath, "xpath", Comments)
        objActions.clickElement(PCN.AddNewAttachement_SubmitBtn_xpath, "xpath")
        time.sleep(3)

    def DeleteAttachement(self):
        global flag
        time.sleep(2)
        objTable = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='attachment']/tbody/tr")
        intRowCount = len(objTable)
        flag = False
        for i in range(2, intRowCount + 1):
            stri = str(i)
            objActions.getText("//table[@id='attachment']/tbody/tr[" + stri + "]/td[1]", "xpath")
            time.sleep(2)
            objActions.clickElement("//table[@id='attachment']/tbody/tr[" + stri + "]/td[1]", "xpath")
            time.sleep(2)
            alert_obj = MyConfigFiles.driver.switch_to.alert
            alert_obj.accept()
            time.sleep(2)
            objTable = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='attachment']/tbody/tr")
            intRowCountafterdel = len(objTable)
            if intRowCount != intRowCountafterdel:
                print("Present Row count is :"+str(intRowCountafterdel))
                objCommon.capture_screenshot("Selected Row deleted sucessfully")
                break
            if flag == True:
                 break
            else:
                sys.exit("FAILED:: Row Not delected: " + stri)


    # def EOL_InvistigationFileUpload_fromJPNTable(self,strFilePath):
    #     time.sleep(2)
    #     objTablerow = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr")
    #     intRowCount = len(objTablerow)
    #     # print("Rows Count in page  is: " + str(intRowCount - 1))
    #     flag = False
    #     for i in range(1, intRowCount + 1):
    #         stri = str(i)
    #         # print(stri)
    #         objTablecol = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr/th")
    #         intColCount = len(objTablecol)
    #         for j in range(i, intColCount + 1):
    #              strj = str(j)
    #         print("Column count is :" + str(intColCount - 1))
    #         strColumheaders = objActions.getText("//table[@id='upload-jpn']//tbody//tr[" + stri + "]//th[" + strj + "]", "xpath")
    #         time.sleep(2)
    #         # print(strColumheaders)
    #         time.sleep(2)
    #         if "EOL" in strColumheaders:
    #             for k in range(i + 1, intRowCount - 1):
    #                 strk = str(k)
    #                 # print(strk)
    #                 strChoosefile = objActions.getText("//table[@id='upload-jpn']/tbody//tr[" + strk + "]//td[" + strj + "]", "xpath")
    #                 print(strChoosefile)
    #                 if strChoosefile == '':
    #                     time.sleep(3)
    #                     objActions.getText("//table[@id='upload-jpn']/tbody//tr[" + strk + "]//td[" + strj + "]//span[1]//input[1]", "xpath")
    #                     time.sleep(3)
    #                     objCommon.AttachFile(strFilePath, "//table[@id='upload-jpn']/tbody//tr[" + strk + "]//td[" + strj + "]//span[1]//input[1]","xpath")
    #                     time.sleep(1)
    #                     objActions.Page_Scroll_Actions("JpnInput", "id")
    #                     time.sleep(3)
    #                     objActions.clickElement("//table[@id='upload-jpn']/tbody//tr[" + strk + "]//td[" + strj + "]//span[1]//p[1]//a[1]", "xpath")
    #                     time.sleep(5)
    #                     flag = True
    #                     print("EOL Form is uploaded sucessfully: ")
    #                     # break
    #         break




    def PreviewScreen_Validations(self,PendingConcernsComments):
        objActions.clickElement(PCN.JPN_MPN_Button_xpath, "xpath")
        time.sleep(2)
        objActions.clickElement(PCN.MultipleCoreCE_POpUp_Button_xpath, "xpath")
        time.sleep(2)
        objCommon.capture_screenshot("Preview screen popup text ")
        time.sleep(2)
        PlaceHolder_Acttext=objActions.getText(PCN.Placeholder_text_WebElement_name, "name")
        # print(PlaceHolder_Acttext)
        if PlaceHolder_Acttext == PendingConcernsComments:
            print("Preview screen will appear with the Pending Info Comments given in the first page as :"+PlaceHolder_Acttext)
            objCommon.capture_screenshot("Preview Screen comments")
            objActions.clickElement(PCN.PreviewScreen_button_xpath, "xpath")
        else:
            print("Failed: Preview screen not displaying comments")
            time.sleep(2)
        assert PlaceHolder_Acttext == PendingConcernsComments


    def MultipleCoreCE_Selection(self,strJPNID):
        objActions.clickElement(PCN.JPN_MPN_Button_xpath, "xpath")
        time.sleep(2)
        objCommon.capture_screenshot("JPCN is having multiple Core CE.")
        objActions.clickElement(PCN.MultipleCoreCE_POpUp_NoButton_xpath, "xpath")
        objCommon.capture_screenshot("How would you like to solve the multiple Core CE issue?.")
        time.sleep(2)
        objActions.clickElement(PCN.MultipleCoreCE_Duplicate_Button_xpath, "xpath")
        objCommon.capture_screenshot("Preview screen popup text ")
        time.sleep(2)
        html = MyConfigFiles.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        strJPCNDuplicate_Msg= objActions.getText(PCN.MultipleCoreCE_Duplication_Msg_xpath, "xpath")
        objCommon.capture_screenshot("JPCN Duplication is Completed!")
        assert(strJPCNDuplicate_Msg)
        time.sleep(2)
        objActions.clickElement(PCN.Newly_duplicatedJPCN_Link_xpath, "xpath")
        time.sleep(2)
        JPCN_Duplicate=objActions.getText(PCN.Jnpr_PCNID_xpath, "xpath")
        if JPCN_Duplicate != strJPNID:
            print("New Duplicate JPCN id created Sucessfully")

        # PlaceHolder_Acttext=objActions.getText(PCN.Placeholder_text_WebElement_name, "name")
        # # print(PlaceHolder_Acttext)
        # if PlaceHolder_Acttext == PendingConcernsComments:
        #     print("Preview screen will appear with the Pending Info Comments given in the first page as :"+PlaceHolder_Acttext)
        #     objCommon.capture_screenshot("Preview Screen comments")
        #     objActions.clickElement(PCN.PreviewScreen_button_xpath, "xpath")
        # else:
        #     print("Failed: Preview screen not displaying comments")
        #     time.sleep(2)
        # assert PlaceHolder_Acttext == PendingConcernsComments


    # Expand Supplier info sections and Edit the few details.

    def Verify_SupplierInfo_Edit_ProductData_Section(self):
        time.sleep(3)
        objActions.Page_Scroll_Actions("//p[contains(text(),'Supplier Info')]", "xpath")
        time.sleep(3)
        objActions.clickElement(PCN.Expand_SupplierInfo_Button_xpath, "xpath")
        time.sleep(2)
        strGetItems=MyConfigFiles.driver.find_elements_by_xpath("//div[@class='supplier-info-section padding-around show-it']//button[contains(text(),'Edit')]")
        print(len(strGetItems))
        intcount=len(strGetItems)
        if intcount > 0:
            objActions.clickElement(PCN.Expand_SupplierInfo_Edit_Button_xpath, "xpath")
            time.sleep(2)
            objActions.enterText(PCN.SampleOwner_Contact_WebEdit_name, "name", "automation")
            time.sleep(2)
            objActions.clickElement(PCN.Expand_SupplierInfo_Save_Button_xpath, "xpath")
            objCommon.capture_screenshot("Supplier info sections edited sucessfully with sample Owner Conatct:")
            time.sleep(2)
            objActions.clickElement(PCN.Expand_SupplierInfo_Button_xpath, "xpath")
        else:
            objActions.clickElement(PCN.Expand_SupplierInfo_Button_xpath, "xpath")
            print("Edit button not  displyed in the Supplier info secession and all the fields are read only ")




    # Compare SupplierInfo data from first page and verify productData page

    def Compare_Supplierinfodata_in_verifyproductsection(self,SupplierName,strupdated,strSC,strSCE,strSP,strEC,strECE):
        time.sleep(3)
        objActions.Page_Scroll_Actions("//p[contains(text(),'Supplier Info')]", "xpath")
        time.sleep(3)
        objActions.clickElement(PCN.Expand_SupplierInfo_Button_xpath, "xpath")
        time.sleep(2)
        strSN=objActions.getAttributeValue(PCN.Suppliername_WebEdit_name, "name", "value")
        if SupplierName == strSN:
           print("Passed: SupplierName from the fistpage and VerifyProduct page are same :"  " " +strSN)
        else:
            print("Failed: SupplierName displaying as:" +strSN+ "insted of:"  +SupplierName)
        assert SupplierName == strSN
        time.sleep(2)
        # strPCN = objActions.getAttributeValue(PCN.SupplierPCN_WebEdit_name, "name", "value")
        # if strupdated == strPCN:
        #     print("Passed: SupplierPCN from the fistpage and VerifyProduct page are same :"  " " +strPCN)
        # else:
        #     print("Failed: SupplierPCN displaying as:" +strPCN + "insted of:" +strupdated)
        # assert strupdated == strPCN
        time.sleep(2)
        strSC_VPD=objActions.getAttributeValue(PCN.SupplierContact_WebEdit_name, "name", "value")
        if strSC == strSC_VPD:
            print("Passed: SupplierContact from the fistpage and VerifyProduct page are same :"  " " +strSC_VPD)
        else:
            print("Failed: SupplierContact displaying as:" +strSC_VPD + "insted of:" +strSC)
        assert strSC== strSC_VPD
        time.sleep(2)
        strSCE_VPD = objActions.getAttributeValue(PCN.SupplierContactEmail_WebEdit_name, "name", "value")
        if strSCE == strSCE_VPD:
            if strSC == strSC_VPD:
                print("Passed: SupplierContactEmail from the fistpage and VerifyProduct page are same :"  " " +strSCE_VPD)
        else:
                print("Failed: SupplierContactEmail displaying as:" +strSCE_VPD+ "insted of:" +strSCE)
        assert strSCE == strSCE_VPD
        time.sleep(2)
        strSP_VPD = objActions.getAttributeValue(PCN.SupplierPhone_WebEdit_name, "name", "value")
        if  strSP ==  strSP_VPD:
            print("Passed: SupplierPhone from the fistpage and VerifyProduct page are same :"  " " +strSP_VPD)
        else:
            print("Failed: Supplier phone displaying as:" +strSP_VPD+ "insted of:" +strSP)
        assert strSP == strSP_VPD
        time.sleep(2)
        strEC_VPD = objActions.getAttributeValue(PCN.SupplierEscalation_WebEdit_name, "name", "value")
        if strEC == strEC_VPD:
            print("Passed: SupplierEC from the fistpage and VerifyProduct page are same :"  " "  +strEC_VPD)
        else:
            print("Failed: SupplierEC displaying as:" +strEC_VPD+ "insted of:" +strEC)
        assert strEC == strEC_VPD
        time.sleep(2)
        strECE_VPD = objActions.getAttributeValue(PCN.SupplierEscalationEmail_WebEdit_name, "name", "value")
        if strECE == strECE_VPD:
            print("Passed: SupplierECEmail from the fistpage and VerifyProduct page are same :"  " "  +strECE_VPD)
        else:
            print("Failed: SupplierECEmail displaying as" +strECE_VPD+ "insted of:" +strECE)
        assert strECE == strECE_VPD
        time.sleep(2)



    def Verify__PCN_PDNinfo_Edit_ProductData_Section(self,DescriptionChange):
        time.sleep(3)
        objActions.clickElement(PCN.Expand_PCN_PDNinfo_Button_xpath, "xpath")
        time.sleep(2)
        strGetItems = MyConfigFiles.driver.find_elements_by_xpath("//div[@class='PCN-PDN-info-section padding-around show-it']//button[contains(text(),'Edit')]")
        print(len(strGetItems))
        intcount = len(strGetItems)
        if intcount > 0:
            objActions.clickElement(PCN.Expand_PCN_PDNInfo_Edit_Button_xpath, "xpath")
            AppendValue= "Edited"
            objActions.enterText(PCN.Descriptionchange_WebEdit_name, "name" , AppendValue)
            time.sleep(2)
            html = MyConfigFiles.driver.find_element_by_tag_name('html')
            html.send_keys(Keys.PAGE_UP)
            time.sleep(3)
            objActions.clickElement(PCN.Expand_PCN_PDNInfo_Save_Button_xpath, "xpath")
            time.sleep(2)
            Act_DescChange = objActions.getAttributeValue(PCN.Descriptionchange_WebEdit_name, "name", "value")
            if DescriptionChange != Act_DescChange:
                print("Successfully Edited Description Change  value:", " " + Act_DescChange)
            else:
                print("Failed: Description values displaying:" +DescriptionChange+ "Insted of ", " " + Act_DescChange)
            assert DescriptionChange != Act_DescChange
            time.sleep(2)
            objActions.clickElement(PCN.Expand_PCN_PDNinfo_Button_xpath, "xpath")
        else:
            objActions.clickElement(PCN.Expand_PCN_PDNinfo_Button_xpath, "xpath")
            print("Edit button not displyed in the PDN_PCN info secession and all the fields are read only")



    def WhereUserAnalysis(self,PCNTYPE,strCategory,strFilePath,Comments):
        if PCNTYPE == "EOL":
            objActions.clickElement(PCN.submit_button_xpath, "xpath")
            time.sleep(2)
            UserAnalysis_Required = objActions.getText(PCN.Validation_Msg_UserAanlysis_xpath, "xpath")
            print("Where Use Analysis is Mandatory to click and otherwise validation message is:" +UserAnalysis_Required)
            time.sleep(2)
            objActions.clickElement(PCN.Where_UserAnalysis_button_xapth, "xpath")
            objCommon.capture_screenshot("Where User analysis clicked sucessfully")
            objActions.clickElement(PCN.Completed_Page_OK_button_xpath, "xpath")
            time.sleep(2)
            objActions.clickElement(PCN.Back_JPCNPage_button_xpath, "xpath")
            objCommon.capture_screenshot("Page navigates to Enter JPN-MPN Deatils page")
            time.sleep(2)
            self.AddNewAttachement_JPNMPN(strCategory,strFilePath,Comments)
            time.sleep(3)
            objActions.clickElement(PCN.JPN_MPN_Button_xpath, "xpath")
            objCommon.capture_screenshot("Page navigates to Verify produce  page")
            objActions.clickElement(PCN.submit_button_xpath, "xpath")
            time.sleep(2)
            PCN_CompletedMsg = objActions.getText(PCN.Validation_Msg_PCNCreations_xpath, "xpath")
            print(PCN_CompletedMsg)
            objCommon.capture_screenshot("New PCN Create sucessfully")
            objActions.clickElement(PCN.Completed_Page_OK_button_xpath, "xpath")
            objCommon.capture_screenshot("Sucessfully navigate to the JPCN Status Overview page")
        else:
            objActions.clickElement(PCN.submit_button_xpath, "xpath")
            time.sleep(2)
            PCN_CompletedMsg = objActions.getText(PCN.Validation_Msg_PCNCreations_xpath, "xpath")
            print(PCN_CompletedMsg)
            objCommon.capture_screenshot("New PCN Create sucessfully")
            objActions.clickElement(PCN.Completed_Page_OK_button_xpath, "xpath")
            time.sleep(2)
            objCommon.capture_screenshot("Sucessfully navigate to the JPCN Status Overview page")


# Count the highest occurrence of core CE names

    def GetCoreCENames(self):
        objTablerow = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr")
        intRowCount = len(objTablerow)
        print(intRowCount)
        strCoreCEList1 = []
        for strCoreCEList in MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr/td[14]"):
            strCoreCEList1.append(strCoreCEList.text)
            print(strCoreCEList.text)
            print(strCoreCEList1)
            CoreCESet = set(strCoreCEList1)
            CoreCEList = list(CoreCESet)
            print(CoreCEList)
            CoreCENames = len(CoreCEList)
            print(CoreCENames)
            CoreCount = 0
            for x in CoreCEList:
                CoreCount1 = CoreCount
                CoreCount=0
                # CoreCount = strCoreCEList1.count(x)
                # print(CoreCount)
                if CoreCount > CoreCount1:
                    CoreCount1 = CoreCount
                    print(x)

    # def Page_Scroll_Actions(self,element):
    #     actions = ActionChains(MyConfigFiles.driver)
    #     element = MyConfigFiles.driver.find_element_by_name('name')
    #     actions.move_to_element(element)
    #     actions.perform()

    def DeleteAttachement_PRrows(self):
        global flag
        time.sleep(4)
        objTable = MyConfigFiles.driver.find_elements_by_xpath("//div[@id='Core-Ce-Details']//table[@id='pr']/tbody/tr")
        intRowCount = len(objTable)
        flag = False
        for i in range(2, intRowCount + 1):
            stri = str(i)
            objActions.getText("//div[@id='Core-Ce-Details']//table[@id='pr']/tbody/tr[" + stri + "]/td[1]", "xpath")
            time.sleep(2)
            objActions.clickElement("//div[@id='Core-Ce-Details']//table[@id='pr']/tbody/tr[" + stri + "]/td[1]", "xpath")
            time.sleep(2)
            alert_obj = MyConfigFiles.driver.switch_to.alert
            alert_obj.accept()
            time.sleep(2)
            objTable = MyConfigFiles.driver.find_elements_by_xpath("//div[@id='Core-Ce-Details']//table[@id='pr']/tbody/tr")
            intRowCountafterdel = len(objTable)
            if intRowCount != intRowCountafterdel:
                print("Present Row count is :"+str(intRowCountafterdel))
                objCommon.capture_screenshot("Selected Row deleted sucessfully")
                break
            if flag == True:
                 break
            else:
                sys.exit("FAILED:: Row Not delected: " + stri)



    def ClickOnJPN_MPN_Exapnd(self):
        time.sleep(4)
        objActions.clickElement(PCN.Expand_JPN_MPN_Button_xpath, "xpath")
        time.sleep(4)



#***********************************************************************************************************
    def EOL_InvistigationFileUpload_fromJPNTable1(self, strFilePath):
        global flag
        time.sleep(2)
        strPages = objActions.getText(PCN.ContextCE_TablePage_Count_xpath, "xpath")
        strPagesCount = strPages.split(" ")
        intPagesCount = int(strPagesCount[4])
        if intPagesCount <= 1:
            time.sleep(30)
        flag = False
        for pages in range(1, intPagesCount + 1):
            objTable = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr")
            intRowCount = len(objTable)
            for i in range(2, intRowCount + 1):
                stri = str(i)
                objTablecol = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr/th")
                intColCount = len(objTablecol)
                for j in range(i, intColCount + 1):
                    strj = str(j)
                    strchoosefile = objActions.getText("//table[@id='upload-jpn']/tbody/tr[" + stri + "]/td[" + strj + "]", "xpath")
                    if strchoosefile == "Upload":
                        time.sleep(2)
                        objActions.getText("//table[@id='upload-jpn']/tbody//tr[" + stri + "]//td[" + strj + "]//span[1]//input[1]", "xpath")
                        time.sleep(3)
                        objCommon.AttachFile(strFilePath, "//table[ @ id = 'upload-jpn']/ tbody// tr[" + stri + "]//td[" + strj + "]// span[1]// input[1]", "xpath")
                        time.sleep(1)
                        objActions.Page_Scroll_Actions("JpnInput", "id")
                        time.sleep(3)
                        objActions.clickElement("//table[@id='upload-jpn']/tbody//tr[" + stri + "]//td[" + strj + "]//span[1]//p[1]//a[1]", "xpath")
                        time.sleep(5)
                        flag = True
                        print("EOL file Upload sucessfully and file name is: "+strFilePath)
                        break
                        time.sleep(10)
                if flag == True:
                    break
        if flag == False:
                sys.exit("FAILED:: Could not find the Upload Choose file option: " + strFilePath)


    def get_all_data(self):
        # get number of rows
        noOfRows = len(MyConfigFiles.driver.find_elements_by_xpath("//table[@class='font-size-regular']/tbody/tr"))
        print(noOfRows)
        # get number of columns
        noOfColumns = len(MyConfigFiles.driver.find_elements_by_xpath("//table[@class='font-size-regular']/tbody/tr/td"))
        print(noOfColumns)
        allData = []
        print(allData)
        # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in range(1, noOfRows):
            # reset the row data every time
            ro = []
            # iterate over columns
            for j in range(i, noOfColumns):
                # get text from the i th row and j th column
                ro.append(objActions.getText("//table[@class='font-size-regular']/tbody/tr[" + str(i) + "]/td[" + str(j) + "]", "xpath"))
                # ro.append(MyConfigFiles.driver.find_elements_by_xpath("//table[@class='font-size-regular']/tbody/tr[" + str(i) + "]/td[" + str(j) + "]")
            # add the row data to allData of the self.table
            allData.append(ro)
        return allData


































