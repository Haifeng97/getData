import urllib.parse
import urllib.request


def getHtml(url,values):
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    data = urllib.parse.urlencode(values)
    req = urllib.request.Request(url, data)
    req.add_header("user-agent", user_agent)
    req.add_header('Accept', '*/*')
    req.add_header('Accept-Encoding', 'gzip, deflate')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Host', 'pvc.zol.com.cn')
    req.add_header('Referer', 'http://detil.zol.com.cn/')
    response_result = urllib.request.urlopen(url+'?'+data).read()
    html = response_result.decode('gbk')
    return html
def request(url):
    print('request')
    value= {
        'refer': 'http://detail.zol.com.cn/',
        'url': url
    }
    result = getHtml(url,value)
    return result
def get1(url):
    req = urllib.request.Request(url)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    req.add_header("user-agent", user_agent)
    response_result = urllib.request.urlopen(url).read()
    html = response_result.decode('gbk')
    return html