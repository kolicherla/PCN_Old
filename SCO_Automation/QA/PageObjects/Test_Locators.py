class PCN():
#chrome settings
    ClearBrowsingData_button_cssselector="* /deep/ #clearBrowsingDataConfirm"

#PCN Login page objects
    username_textbox_id = "userid"
    password_textbox_id = "password"
    submit_button_xpath = "//button[@type='submit']"
    logout_link_xpath = "//a[@href='/saml/logout']"

#PCN Home Page Tabs
    Switch_Roles_link_xpath = "//a[text()='Switch Roles']"
    Admin_link_xpath="//a[text()='Admin']"
    Reports_link_xpath="//a[text()='Reports']"
    Search_link_xpath="//a[text()='Search']"
    DashBoard_Button_xpath="//a[text()='Dashboard']"


#Switch to other roles Options
    ContextCE_WebElement_xpath = "//input[@value='ce']"
    Global_CM_WebElement_xpath = "//input[@value='gcm']"
    NPI_Material_PM_WebElement_xpath = "//span[text()='npi']"
    NPI_MPM_WebElement_xpath = "//span[text()='mpm']"
    Submit_SR_button_xpath="//button[@class='primary']"
    Cancel_Button_xpath="//div[@class='supplier-info-section padding-around show-it']//a[@class='button-cancel margin-right'][contains(text(),'Cancel')]"


#Enter PCN Details Page
    Suppliername_WebEdit_name="supName"
    SupplierPCN_WebEdit_name="supPcnId"
    SupplierContact_WebEdit_name="supContactName"
    SupplierContactEmail_WebEdit_name="supContactEmail"
    SupplierPhone_WebEdit_name="supContactPhone"
    SupplierEscalation_WebEdit_name="supEscalationContactName"
    SupplierEscalationEmail_WebEdit_name="supEscalationContactEmail"
    PCN_Quarter_name="quarter"
    PCN_SupplierStatus_name="supplierStatus"
    CreateJPCN_link_xpath="//a[text()='Create JPCN']"
    PCNIssue_Date_WebEdit_xpath = "//div[@class='react-datepicker__input-container']//input[@name='pcnIssueDt']"
    PCNReceived_Date_WebEdit_xapth="//div[@class='react-datepicker__input-container']//input[@name='pcnReceivedDt']"
    PCNEffective_date_WebEdit_xpath="//div[@class='react-datepicker__input-container']//input[@name='pcnEffectDt']"
    PCNLastTime_BuyDate_WebEdit_xpath="//div[@class='react-datepicker__input-container']//input[@name='lastTimeBuyDt']"
    PCNLastTime_ShipDate_WebEdit_xpath="//div[@class='react-datepicker__input-container']//input[@name='lastTimeShipDt']"
    PCNType_Selectbox_name="pcnType"
    PCNSource_Selectbox_name="pcnSource"
    Descriptionchange_WebEdit_name="changeDescription"
    NatureofChange_Selectbox_name="changeNature"
    Typeofchange_Selectbox_xpath="//div[@class='show-border padding-top padding-left padding-right padding-bottom']//select[@id='selectDrpDwn']"
    Add_Button_xpath="//button[@type='button']"
    PCNEffectiveDate_Next_Button_xpath="//button[@class='react-datepicker__navigation react-datepicker__navigation--next']"

#Enter JPN-MPN Details page
    Jnpr_PCNID_xpath="//span[contains(text(),'JPCN-')]"  
    Verify_Context_CE_sections_xpath="//p[contains(text(),'Context CE Details')]"
    Validate_ContextCeRecommend_Value_name="contextCeRecommend"
    Validate_PCNStatus_Value_name="pcnStatus"
    Validate_PCNStatusComment_Value_name="pcnStatusComment"
    PCNStatusClose_Comments_name="pcnCloseComment"
    Validate_ResponsibleCE_Value_name="respCE"
    Validate_PCNCompliance_Value_name="pcnCompliance"
    Close_ThisPCN_Button_xpath="//button[contains(text(),'Close this PCN')]"
    Login_Username_WebElement_xpath="//span[@class='user-name']"
    Validation_msg_WebElement_xpath="//li[contains(text(),'Invalid PCN Status')]"
    Validation_msg_ClosureAssesment_WebElement_xapth="//span[contains(text(),'Invalid pcn status')]"
    Choosefile_button_name="myFile"
    Upload_button_xpath="//button[@class='button-upload primary']"
    Acknowledgement_Notification_msg_xapth="//p[contains(text(),'Juniper Use Analysis is in progress. You will be i')]"
    Acknowledgement_Notification_button_xpath="//button[contains(@class,'secondary primary')]"
    Jnpr_UA_Validation_msg_xpath="//span[text()='No Record Found!']"
    Jnpr_AfterUpload_Impactedflow_Validation_Msg_xpath="//span[@class='padding-left-small']"
    Back_JPCNPage_button_xpath="//button[contains(text(),'Back')]"
    EOL_Investigation_Upload_Lnk_xpath="//tr[2]//td[15]//span[1]//p[1]//a[1]"
    EOL_Investigation_button_xpath="//tr[2]//td[15]//span[1]//input[1]"
    EOL_UPload_WebElement_xpath="//a[contains(text(),'Upload |')]"
    EOL_Download_WebElement_xpath="//a[contains(text(),'Download')]"
    EOL_Delete_WebElement_xpath="//a[contains(text(),'| Delete')]"
    JPN_MPN_Button_xpath="//button[contains(text(),'Save & Continue')]"
    JPN_MPN_AddNew_Attachment_button_xpath="//a[contains(text(),'Add New Attachment')]"
    JPN_MPN_Responsible_CoreCE_Selectbox_name="respCoreCE"
    AddNewAttachement_Category_Selectbox_xpath="//div[@class='dialog']//select[@id='selectDrpDwn']"
    AddNewAttachement_Choose_file_xapth="//table[@class='font-size-regular']//tbody//tr//td//div//input"
    AddNewAttachement_Comments_xpath="//textarea[@placeholder='type comments...']"
    AddNewAttachement_SubmitBtn_xpath="//button[contains(text(),'Submit')]"
    AddNewAttachement_delete_button_xpath="//img[contains(@class,'font-size-regular')]"
    MultipleCoreCE_POpUp_Button_xpath="//button[contains(text(),'Yes!')]"
    MultipleCoreCE_POpUp_NoButton_xpath="//button[contains(text(),'No!')]"
    MultipleCoreCE_Duplicate_Button_xpath="//button[contains(text(),'Duplicate the current JPCN')]"
    MultipleCoreCE_Duplication_Msg_xpath="//p[contains(text(),'JPCN Duplication is Completed!')]"
    Newly_duplicatedJPCN_Link_xpath="//a[contains(text(),'View the newly duplicated JPCN(s) here')]"
    Placeholder_text_WebElement_name="ackEmailAddlNote"
    PreviewScreen_button_xpath="//button[contains(text(),'Send Email')]"
    OpenConcerns_Comments_WebEdit_name="pendingConcernComment"
    Expand_SupplierInfo_Button_xpath="//p[contains(text(),'Supplier Info')]/img[@class='plus-icon icon-pull-right font-size-large']"
    Expand_PCN_PDNinfo_Button_xpath="//p[contains(text(),'PCN/PDN Info')]"
    Expand_SupplierInfo_Edit_Button_xpath="//div[@class='supplier-info-section padding-around show-it']//button[contains(text(),'Edit')]"
    Expand_PCN_PDNInfo_Edit_Button_xpath="//div[@class='PCN-PDN-info-section padding-around show-it']//button[contains(text(),'Edit')]"
    Expand_SupplierInfo_Save_Button_xpath="//div[@class='supplier-info-section padding-around show-it']//button[contains(text(),'Save')]"
    Expand_PCN_PDNInfo_Save_Button_xpath="//div[@class='PCN-PDN-info-section padding-around show-it']//button[contains(text(),'Save')]"
    SampleOwner_Contact_WebEdit_name="supSampleOwnerContact"
    Validation_Msg_UserAanlysis_xpath="//li[contains(text(),'Where use analysis is run mandatory.')]"
    Where_UserAnalysis_button_xapth="//button[text()='Where Use Analysis']"
    Validation_Msg_PCNCreations_xpath="//div[@class='confirm-message-container']"
    Completed_Page_OK_button_xpath="//button[text()='OK']"
    JPCNStatus_Overivew_Button_xpath="//button[text()='Send Back']"
    AssignBack_Comments_WebEdit_xpath="//p[contains(text(),'Assign Back to Context CE')]/parent::div//textarea[contains(@name,'coreCeSendBackComment')]"
    JPCN_Analyis_Stage_Status_xpath="//p[contains(@class,'font-size-small text-color-grey-dark icon-pull-right')]"
    Expand_JPN_MPN_Button_xpath="//p[contains(text(),'JPN-MPN info')]"



#DASHBOARD ELEMENTS
    DashBoard_CreateItem_WebElement_xpath="//span[text()='Create']"
    ContextCE_TablePage_Count_xpath="//div[@class='showing-pages']"
    DashBoard_InitialAssessment_WebElement_xpath="//span[text()='Initial Assessment']"
    DashBoard_CoreCEAssessment_WebElement_xpath="//span[text()='Core CE Assessment Pending']"
    DashBoard_ReassignAssessment_WebElement_xpath="//span[text()='Reassign Assessment']"
    DashBoard_CoreCECompAssessment_WebElement_xpath="//span[text()='Core CE Assessment Completed']"
    DashBoard_ContextCE_ClosureAssessment_WebElement_xapth="//span[text()='Closure Assessment']"
    DashBoard_ContextCE_CompleteAssessment_WebElement_xapth="//span[text()='Completed Assessment']"
#Initial Assessment Elements
    Expand_JPN_MPNinfo_Button_xpath="//p[contains(text(),'JPN-MPN info')]"
    ContextCE_Recommendation_SelectBox_name="ceRecommendation"
    ContextCE_RecommendationComments_WebEdit_name="ceRecommendationComment"
    Priority_Type_selectBox_name="priorityType"
    IA_AddNewRecord_WebElement_xpath="//a[contains(text(),' Add New Record')]"
    AddNewRecord_PR_WebEdit_name="prId"
    AddNewReocrd_Deviation_WebEdit_name="deviation"
    AddNewRecord_DeviationStatus_selectBox_name="deviationStatus"
    AddNewRecord_JPN_WebEdit_name="jpn"
    AddNewRecord_MPN_WebEdit_name="mpn"
    AddNewRecord_710_711_WebEdit_name="sevenTenOrSevenEleven"
    AddNewRecord_HTR_WebEdit_name="htr"
    AddNewRecord_ECOMCO_WebEdit_name="mcoEco"
    AddNewRecord_qpet_WebEdit_name="qpet"
    AddNewRecord_Comment_WebEdit_name="comment"
    AddNewRecord_JA_WebEdit_name="jnprAssembly"
    AddNewRecord_ECOMCO_Status_WebEdit_name="mcoEcoStatus"
    Reasonfor_NonCompliance_SelectBox_name="nonComplianceReason"
    Complete_Assessment_Button_xpath="//button[contains(text(),'Complete the Assessment')]"
    QualDataReview_Attachement_xpath="//input[@class='file-upload font-size-regular']"
    QualDataReview_CoreCE_Attachement_xpath="//div[@id='Core-Ce-Details']//input[@class='file-upload font-size-regular']"
    QualDataReview_Upload_xpath="//button[@class='button-upload g-margin-left-10']"
    QualDateReview_CoreCe_Upload_xpath="//div[@id='Core-Ce-Details']//button[@class='button-upload g-margin-left-10']"
    QualReport_AcceptStaus_name="ceQualReportAcceptStatus"
    QualReport_ReviewComments_name="ceQualReportComment"
    IA_PCNCompliance_SelectBox_name="pcnCompliance"
    Compliance_CoreCE_SelectBox_xpath="//div[@id='Core-Ce-Details']//select[contains(@name,'pcnCompliance')]"
    IA_Reason_NonCompliance_SelectBox_name="nonComplianceReason"
    PCNReason_NonCompliance_CoreCE_SelectBox_xpath="//div[@id='Core-Ce-Details']//select[contains(@name,'nonComplianceReason')]"
    IA_Alternative_SourceQN_SelectBox_name="alternateSrcQualNeed"
    IA_FFF_Alternative_SourceComments_WedEdit_name="alternateSrcComment"
    QualReport_AcceptStaus_CoreCE_xpath="//div[@id='Core-Ce-Details']//select[contains(@name,'coreCeQualReportAcceptStatus')]"
    QualReport_ReviewComments_CoreCE_xpath="//div[@id='Core-Ce-Details']//textarea[contains(@name,'coreCeQualRptComment')]"
    CoreCe_Recommendation_name="coreCeRecommendation"
    CoreCe_Recommendation_comments_name="coreCeRecommendationComment"
    CoreCE_Justifications_name="coreCEJustification"
    CoreCE_ChangeStatus_xapth="//p[contains(text(),'Do you agree with the')]"
    CoreCE_Gobackmsg_xpath="//p[contains(text(),'PCN EOL Compliance')]"
    Goback_Button_xpath="//a[contains(text(),'Go Back')]"
    JPN_MPN_EOL_Download_WebElement_xapth="//a[contains(text(),'Download)]"
    Close_Assessment_WebElement_xpath="//button[contains(text(),'Close the Assessment')]"
    Close_Assessment_Warning_WebElement_xpath="//p[contains(text(),'ECO/MCO is not yet released and the JPCN cannot be closed now')]"
    Close_Assessment_PREdit_WebElement_xpath="//div[@class='up-6px']//img"
    Completed_Assessement_PageHeader_WebElement_xpath="//p[contains(text(),'Completed Assessment')]"

#Search Page

    Search_Button_xpath="//button[@class='primary primary']"
    #Search_Button_xpath="//a[contains(text(),'Search')]"
    Right_Arrow_xpath_firsttime="//div[@class='content']//li[4]//a[1]"
    Right_Arrow_xpath_NextTime="//div[@class='content']//li[6]//a[1]"
    Right_Arrow_xpath_WhenTwoPages="//div[@class='content']//li[3]//a[1]"
    PCNType_SearchPage_name="pcnType"
    Search_TablePage_Count_xpath="//div[@class='showing-pages']"
    Edit_Button_SearchPage_xpath="//button[@class='secondary primary']"
    EditComments_TextBox_xpath="//input[@placeholder='Enter comments']"
    SupplierQueryResolvedDate_xpath="//div[@class='PCN-PDN-info padding-bottom']//tr[7]//td[1]//div[2]//div[1]//div[1]//input[1]"











