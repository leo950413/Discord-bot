import requests
import requests.exceptions
flag = "flag{this_is_a_fake_flag}"

def ch6(url:str)->str:
    try:
        res = requests.get(url)
        if res.status_code==200:
            if res.text.find("Hello world")!=-1:
                requests.get(url,params={"flag":flag})
            return True
        else:
            return True
        
        
    except ConnectionError:
        return "Connection error"
    except requests.exceptions.MissingSchema:
        return "Not a valid url"
    except requests.exceptions.ConnectTimeout:
        return "Time out error"
    except Exception as e:
        return e
    