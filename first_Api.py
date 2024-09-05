import requests
def fetch_Joke(): 
    url="https://api.freeapi.app/api/v1/public/randomjokes?     limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response=requests.get(url)
    api_Data=response.json()
    if(api_Data["success"] and "data" in api_Data):
        userData=api_Data["data"]["data"]
        joke=userData[0]["content"]
        joke1=userData[1]["content"]
        return joke , joke1 
    else:
        raise Exception ("Error 404")
        
def main():
    try:
        joke,joke1=fetch_Joke()
        print(f"joke:{joke} \n joke1:{joke1}")
    except exception as e:
        print(str(e))
if __name__=="__main__":
        main()