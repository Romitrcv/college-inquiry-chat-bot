from googleapiclient.discovery import build
my_api_key = "AIzaSyA0eQqo5wF6_i8oVwSg-rbZHBe8uNNHDT8"
my_cse_id = "016248527696431796891:g3u5ie8wme4"

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
