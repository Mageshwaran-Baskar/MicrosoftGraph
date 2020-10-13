import json
import msal
import requests
import pandas

# Globals
token = None
graphApiVersion = "beta"
uri = "https://graph.microsoft.com/{v}/{r}"
headers = None

# Functions
def authenticate():
    global token
    global headers
    authority = "https://login.microsoftonline.com/c31b7b8a-865c-48c3-ad28-17d9d0f8c8c1"
    appID = "0844e608-6f27-463a-9887-8b25855268a6"
    appSecret ="c.0~BWGw2CHWqWy026~~M3IJr3UnT5uFg9"
    scope = ["https://graph.microsoft.com/.default"]

    app = msal.ConfidentialClientApplication(
        appID, authority=authority, client_credential = appSecret)
    token = app.acquire_token_silent(scope, account=None)
    if not token:
        token = app.acquire_token_for_client(scopes=scope)
        headers = {'Authorization': 'Bearer ' + token['access_token']}
    return 

def query(v, r, Format=True):
    dest = uri.format(v=v, r=r)
    result = requests.get(dest, headers=headers).json()
    return result
    if Format:
        print(pandas.json_normalize(result["value"]))
    else:
        return result["value"]


def users(Format=True):
    result = requests.get("https://graph.microsoft.com/v1.0/users", headers=headers).json()
    return result
    if Format:
        print(pandas.json_normalize(result["value"]))
    else:
        return result["value"]


def userMahesh(Format=True):
    result = requests.get("https://graph.microsoft.com/v1.0/users/Mahesh.Baskar@mageshshines1995gmail.onmicrosoft.com", headers=headers).json()
    return result
    if Format:
        print(pandas.json_normalize(result["value"]))
    else:
        return result["value"]
