# MicrosoftGraph

Requirment : Call any of the Microsoft Graph API(Authentication is must) from python code

The below steps need to be followed to achive the requirement:

1)Firstly need to create a App in Azure Directory

2)All the required permissions need to be granted for the App to have previlages to access AD accounts ; Follow the below link for required permissions  
https://docs.microsoft.com/en-us/graph/api/user-list-messages?view=graph-rest-1.0&tabs=http

3)We can now start with python and call the Microsoft Graph API's
  a) Authentication : MSAL is the module we are going to use here
    MSAL Python, an in-memory token cache that persists for the duration of the app session, is provided by default when you create an instance of       ClientApplication
    
    The below parameters are required to fetch the token and Authenticate 
        
    authority : https://login.microsoftonline.com/<tenent Id> 
    appID 
    appSecret
    scope : ["https://graph.microsoft.com/.default"]
    
    tenent Id, appID , appSecret can be found in App overview
    
  b) Method query in .py file autoauth helps us with custom query 
     ex : autoauth.query('v1.0','users')

  c) Method users fetch's all the AD users and method userMahesh provides the details about the user Mahesh 

Usefull Links :
https://towardsdatascience.com/querying-microsoft-graph-api-with-python-269118e8180c

https://oofhours.com/2020/09/05/using-microsoft-graph-from-python/

https://docs.microsoft.com/en-us/graph/api/user-list-messages?view=graph-rest-1.0&tabs=http

https://windowstechpro.com/insufficient-privileges-to-complete-the-operation-using-azure-application/

https://stackoverflow.com/questions/43301218/authenticating-with-azure-active-directory-on-powershell
