import requests
import errorhandling as err

def search_place(key,query):
    
    url_search ="https://maps.googleapis.com/maps/api/place/textsearch/json"
    search = {"key":key,"query":query}
    search_req = requests.get(url_search,params=search)
    print("status code search:",search_req.status_code)

    search_json = search_req.json()
        
    err.error_handling(search_json["status"])
    place_id = search_json["results"][0]["place_id"]
    return  place_id


def search_details(key,place_id):
        
    url_detail = "https://maps.googleapis.com/maps/api/place/details/json"
    details = {"key":key,"place_id":place_id}
    detail_req = requests.get(url_detail,params=details)

    print("status code details:",detail_req.status_code)
    detail_json = detail_req.json()
    err.error_handling(detail_json["status"])

    return detail_json
    

def searchapi(key,query,param='search'):
    try: 
        #key="AIzaSyDYaa_ZG2qePyaEzKUyPyno9dOc3nNyySA"
        #query="Trans Studio Bandung"
        place_id= search_place(key,query)
        details= search_details(key,place_id)
        if param=='search':
            return details
        
        elif param=='url':
            return details["result"]["url"]
        
        elif param=='address':
            return details["result"]["adr_address"]

        elif param=='geometry':
            return details["result"]["geometry"]

        
        
    except err.ZeroResultError as e:
        message = {'results':
        {
            'status_code':200,
            'status':e.status,
            'message':e.msg,
        }, 'html_attributions':[]
        }
        return message

    except err.OverQueryError as e:
        message = {'results':
        {
            'status_code':200,
            'status':e.status,
            'message':e.msg,
        }, 'html_attributions':[]
        }
        return message

    except err.RequestDeniedError as e:
        message = {'results':
        {
            'status_code':200,
            'status':e.status,
            'message':e.msg,
        }, 'html_attributions':[]
        }
        return message

    except err.InvalidRequestError as e:
        message = {'results':
        {
            'status_code':200,
            'status':e.status,
            'message':e.msg,
        }, 'html_attributions':[]
        }
        return message
    
    except err.UnknownError as e:
        message = {'results':
        {
            'status_code':200,
            'status':e.status,
            'message':e.msg,
        }, 'html_attributions':[]
        }
        return message

    except err.NotFoundError as e:
        message = {'results':
        {
            'status_code':200,
            'status':e.status,
            'message':e.msg,
        }, 'html_attributions':[]
        }
        return message
