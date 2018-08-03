from googleapiclient.discovery import build
my_api_key = "vvhhggfgdfgdfgchvhjbjj-khjkhfhg"  #CREATE YOUR OWN
my_cse_id = "446567767868868776564535437" #CREATE YOUR OWN

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    if 'items' in res:    
        return res['items']
    else:
        return None
def glasearch(s):

    results= google_search(s,my_api_key,my_cse_id,num=10) 
    #print(  results)
    if results is not None:    
        for result in results:
            return (result['title'] + "\n" + result['snippet']+ "\n" +"visit :: "+result['link'])
            #print(result['snippet'])
            #print(result['article']['articlesection'])
            #print("visit :: "+result['link'])
            break
    else :
        return ("not found")
