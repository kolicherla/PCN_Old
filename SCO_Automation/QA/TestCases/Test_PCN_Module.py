from QA.BusinessLogic.CreateJPCN_Page import createJPCN_Page
from QA.BusinessLogic.Login_Page import login_Page
from QA.Utilities.CommonLib import CommonFunctions
from QA.BusinessLogic.JPCNStatusOverview_Page import JPCNstatusoverview_Page
from QA.BusinessLogic.SwitchToOtherRoles_Page import SwitchToRoles_Page
from QA.BusinessLogic.InitialAssessment_Page import InitilaAssessment_Page
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.ClosureAssessment_Page import ClosureAssessment_Page
from QA.BusinessLogic.CompletedAssessment_Page import CompleteAssessment_Page
from QA.BusinessLogic.Search_Page import Search_Page
import pytest
import time


class Test_PCN():
    global objLogin, objCreateJPCN, objCommon,objJPCNStatusOverview, objSwitchToRoles, objHome,objInitalAssessment,objClosureAssessment,objCompleteAssessment,objSearch
    objLogin=login_Page()
    objCreateJPCN=createJPCN_Page()
    objCommon = CommonFunctions()
    objJPCNStatusOverview=JPCNstatusoverview_Page()
    objSwitchToRoles=SwitchToRoles_Page()
    objHome=Home()
    objInitalAssessment=InitilaAssessment_Page()
    objClosureAssessment=ClosureAssessment_Page()
    objCompleteAssessment=CompleteAssessment_Page()
    objSearch=Search_Page()

    # PCN login and  Switch roles to ContextCE for Creating PCN
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    def test_TC001_PCN_Switchtootherroles(self, setup, TestData):
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")

    #************************** NON-IMPACT FLOW**************************************************************
    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC001_PCN_Switchtootherroles"])
    def test_TC002_PCN_CreateJPCN(self, setup, TestData):
        self.test_TC001_PCN_Switchtootherroles(setup, TestData)
        objCreateJPCN.CreateJPCN(TestData['SupplierName'], TestData['SupplierPCN'])
        datelist=objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'],TestData['PCNTYPE'],TestData['LT_BuyDays'],TestData['LT_ShipDays'])
        # objCreateJPCN.PCNType_Dropdown_selections(TestData['PCNTYPE'],TestData['PDNLSDays'],TestData['PDNLBDays'])
        strJPNID=objCreateJPCN.PDNinfo_form(TestData['PCNSource'] ,TestData['DescriptionChange'],TestData['Natureofchange'],TestData['Typeofchange']
                                            ,TestData['PendingConcernsComments'])
        return strJPNID ,datelist



    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC002_PCN_CreateJPCN"])
    def test_TC003_PCN_Horizon_PrePCN_Validations(self, setup, TestData):
        self.test_TC002_PCN_CreateJPCN(setup, TestData)
        objCreateJPCN.Validate_CCE_PrePoulated_Values()
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Open'])
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Reopen'])
        objCreateJPCN.ClosethisPCN(TestData['PCNStatus_Closed'])

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC003_PCN_Horizon_PrePCN_Validations"])
    def test_TC004_PCN_InformationalNotice_Validations(self, setup, TestData):
        self.test_TC003_PCN_Horizon_PrePCN_Validations(setup,TestData)

   #**************************************NO-IMPACT FLOW*************************************************
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC002_PCN_CreateJPCN"])
    def test_TC005_PCN_ProcessChange_Validations(self, setup, TestData):
        strJPNID=self.test_TC002_PCN_CreateJPCN(setup, TestData)
        objCreateJPCN.JPN_MPN_Info('NoImpactFound1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.JPN_MPN_Info_ValidationCheck()
        objCreateJPCN.Validate_CCE_PrePoulated_Values()
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Open'])
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Reopen'])
        objCreateJPCN.ClosethisPCN(TestData['PCNStatus_Closed'])


    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC005_PCN_ProcessChange_Validations"])
    def test_TC006_PCN_DesignChange_Validations(self, setup, TestData):
        strJPNID=self.test_TC005_PCN_ProcessChange_Validations(setup,TestData)
        return strJPNID

    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC005_PCN_ProcessChange_Validations"])
    def test_TC007_PCN_EOL_Validations(self, setup, TestData):
        strJPNID = self.test_TC005_PCN_ProcessChange_Validations(setup, TestData)
        return strJPNID


# ********************************PCN Flow-Create Stage For Process Change************************************************************
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC002_PCN_CreateJPCN"])
    def test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(self, setup, TestData):
        [strJPNID,datelist] = self.test_TC002_PCN_CreateJPCN(setup, TestData)
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page(TestData['SupplierPCN'])
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations(TestData['PendingConcernsComments'])
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section(TestData['DescriptionChange'])
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        return strJPNID,datelist

 # ********************************PCN Flow-Create Stage For Design Changee************************************************************
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change"])
    def test_TC009_PCN_CreatePCN_For_PCNTYPE_Design_Change(self, setup, TestData):
        [strJPNID, datelist] = self.test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(setup, TestData)
        return strJPNID ,datelist

    # ********************************PDN Flow-Create Stage For EOL************************************************************
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change"])
    def test_TC010_PCN_CreatePDN_For_PCNTYPE_EOL(self, setup, TestData):
        [strJPNID, datelist] = self.test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(setup, TestData)
        return strJPNID,datelist

 # ***************************************PCN Initial Assessment Workflow-Create Stage*************************************************
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
# @pytest.mark.dependency(depends=["Test_PCN::test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change"])
    def test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(self, setup, TestData):
        [strJPNID,datelist] = self.test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(setup, TestData)
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section(TestData['DescriptionChange'])
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'],TestData['CCERC']
                                                                ,TestData['PCNTYPE'],TestData['ASQNeeded'],TestData['ASQNComments'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['PR'], TestData['Deviation'], TestData['DeviationStatus'], TestData['Seventeneleveen'], TestData['JPN'], TestData['MPN']
                                                           ,TestData['HTR'], TestData['MCOECO'], TestData['QPET'], TestData['Comments'], TestData['JuniperAssembly'])
        objInitalAssessment.QualDataReview_Attachement('QualReport',TestData['QualReportStatus'], TestData['QualReportComments'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'],datelist['intEFRCDiff'], 'intBRDiff','intSBDiff',TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        return strJPNID,datelist

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC012_PCN_InitialAssessment_For_DesignChangePCNType_Verify_Morethan90days(self, setup, TestData):
        self.test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(setup, TestData)

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC013_PCN_InitialAssessment_For_DesignChangePCNType_Verify_lessthan90days(self, setup, TestData):
        self.test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(setup, TestData)

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC014_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_lessthan90days(self, setup, TestData):
        self.test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(setup, TestData)

# PDN work flow with Combinations of (Last Time Buy Date) - (PCN Received Date) and (Last Time Ship Date) - (Last Time Buy Date) >= 180
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC015_PCN_PDN_InitialAssessment_For_EOLPCNType_Verify_Morethan180days(self, setup, TestData):
        [strJPNID, datelist] = self.test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(setup, TestData)
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section(TestData['DescriptionChange'])
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'], TestData['CCERC']
                                                                ,TestData['PCNTYPE'], TestData['ASQNeeded'],TestData['ASQNComments'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['PR'], TestData['Deviation'], TestData['DeviationStatus'], TestData['Seventeneleveen']
                                                           ,TestData['JPN'], TestData['MPN'], TestData['HTR'], TestData['MCOECO'], TestData['QPET']
                                                           ,TestData['Comments'], TestData['JuniperAssembly'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'],TestData['QualReportComments'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'],datelist['intEFRCDiff'], datelist['intBRDiff']
                                                                                     ,datelist['intSBDiff'], TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()

# PDN work flow with Combinations of (Last Time Buy Date) - (PCN Received Date) and (Last Time Ship Date) - (Last Time Buy Date) < 180
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC015_PCN_PDN_InitialAssessment_For_EOLPCNType_Verify_Morethan180days"])
    def test_TC016_PCN_PDN_InitialAssessment_For_EOLPCNType_Verify_lessthan180days(self, setup, TestData):
        self.test_TC015_PCN_PDN_InitialAssessment_For_EOLPCNType_Verify_Morethan180days(setup, TestData)

 # PDN work flow with Combinations of (Last Time Buy Date) - (PCN Received Date) and (Last Time Ship Date) - (Last Time Buy Date) < 180
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
        # @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC017_PCN_CoreSE_SendBack_For_ProcessChangePCNType(self, setup, TestData):
        [strJPNID, datelist]=self.test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(setup, TestData)
        # objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objJPCNStatusOverview.SendBack_with_AssignBacktoContextCE(TestData['AssginbackComments'])
        return strJPNID, datelist

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC017_PCN_CoreSE_SendBack_For_ProcessChangePCNType"])
    def test_TC018_PCN_Reassign_Assessment(self, setup, TestData):
        [strJPNID, datelist] = self.test_TC017_PCN_CoreSE_SendBack_For_ProcessChangePCNType(setup, TestData)
        objSwitchToRoles.SwitchToRole("Context CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.Reassign_Assessment()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section(TestData['DescriptionChange'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['PR'], TestData['Deviation'],TestData['DeviationStatus']
                                                           , TestData['Seventeneleveen'] , TestData['JPN'], TestData['MPN'], TestData['HTR'],
                                                           TestData['MCOECO'], TestData['QPET'] , TestData['Comments'], TestData['JuniperAssembly'])
        objInitalAssessment.Complete_Assessment()
        return strJPNID,datelist

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC018_PCN_Reassign_Assessment"])
    def test_TC019_PCN_CompletedCoreCE_Assessment(self, setup, TestData):
        [strJPNID, datelist] = self.test_TC018_PCN_Reassign_Assessment(setup, TestData)
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section(TestData['DescriptionChange'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['PR'], TestData['Deviation'], TestData['DeviationStatus'], TestData['Seventeneleveen']
                                                           , TestData['JPN'], TestData['MPN'], TestData['HTR'],  TestData['MCOECO'], TestData['QPET']
                                                           , TestData['Comments'], TestData['JuniperAssembly'])
        objCreateJPCN.ClickOnJPN_MPN_Exapnd()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.DeleteAttachement_PRrows()
        objJPCNStatusOverview.Validation_OnCoreCE_ManadtoryFields('MPN4', TestData['QRAS'], TestData['QRRC'], TestData['CoreCERecommendations']
                                                                  , TestData['CoreCeREComments'], TestData['ReasonforNC'])
        objJPCNStatusOverview.Goabck_button()
        objJPCNStatusOverview.CoreCE_PCN_ChangeComplianceSelect_Validations(TestData['ReasonforNC'])
        objJPCNStatusOverview.Goabck_button()
        objInitalAssessment.Complete_Assessment()
        objInitalAssessment.Submit_OnWarringWindow()
        return strJPNID, datelist

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC019_PCN_CompletedCoreCE_Assessment"])
    def test_TC020_PCN_ContextCE_ClosureAssessment(self, setup, TestData):
        [strJPNID, datelist] = self.test_TC019_PCN_CompletedCoreCE_Assessment(setup, TestData)
        # objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objClosureAssessment.Closure_Assesement_DashBorad_Link()
        objJPCNStatusOverview.SelectJCPN(strJPNID)#JPCN-100100085
        objClosureAssessment.ValidationcheckFor_JPNMPNInfor_Section()
        objClosureAssessment.ValidationcheckFor_CONTEXTCE_DETAILS_Section_ClosureAssessment(TestData['PCNStatus_Reopen'])
        objClosureAssessment.ValidationcheckFor_CONTEXTCE_DETAILS_Section_ClosureAssessment(TestData['PCNStatus_Open'])
        objClosureAssessment.EDit_PR_Section_ClosureAssessment(TestData['PCNStatus_Closed'],  TestData['pcnComments'], TestData['pcnClosedComments'])
        objCompleteAssessment.Verify_CompleteAssessment(strJPNID)
        return strJPNID, datelist

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC019_PCN_CompletedCoreCE_Assessment"])
    def test_TC021_PCN_SolvingMultiple_CoreCE_Problem(self, setup, TestData):
        [strJPNID, datelist] = self.test_TC002_PCN_CreateJPCN(setup, TestData)
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.MultipleCoreCE_Selection(strJPNID)

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC019_PCN_CompletedCoreCE_Assessment"])
    def test_TC022_PCN_ContextCE_ClosureAssessment_EOL(self, setup, TestData):
        [strJPNID, datelist] = self.test_TC020_PCN_ContextCE_ClosureAssessment(setup, TestData)
        return strJPNID, datelist





















