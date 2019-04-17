import json
import requests


def get_url(url):
    name_id = url.split('=')[1]
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
               "referer": "http://music.163.com/song?id=572973442"}

    params = "zHLgssC+A+oe7XgY8d3knWJcLPf4iJs4L18zszLyY+JcISWlEQaoxHgsQW36eX2lGCXPKDL02tEE2ElEEo3nD9FBWJ08f298431b3k0Q9a5KTsCAsKxeGbiR3qErgcNR6HytECQjhjshLisM+zHtCBgOikdJ0zCqmEWYZftad/EcoK7D7izPmsLy2y6eXj/38JpnB5tcq6x6K559DDAJS9+KPqpTzUcXjszgCSGnFI4="
    encSecKey = '''3af514f8ce67c8d04f554b9af432dbd819ac4ee51c48e47af2e2a5c03cef2b2e33b3e713e93dd5b6d5eb949f96be6a17654aaaa4b10f05e9a9cbf451f4d2d4c657f6798ff0ddb8f6066c46aefe364696a540e10cb933ec64c1dafe13e6c6cfa16f3e58005171877f05c43911fbaf194fd04da78c0a7729bcbd496d5979ca5609'''
    data = {
        "params": params,
        "encSecKey": encSecKey
    }

    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)

    res = requests.post(target_url, headers=headers, data=data)

    return res


def get_comment(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json["hotComments"]
    with open('hot_comments.txt', 'w', encoding='utf-8') as f:
        for each in hot_comments:
            f.write(each['user']['nickname'] + ': \n\n')
            f.write(each['content'] + '\n')
            f.write('-----------------------------\n')

def main():
    url = "https://music.163.com/#/song?id=572973442"
    res = get_url(url)
    get_comment(res)

if __name__ == '__main__':
    main()