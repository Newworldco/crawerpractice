import requests
import bs4
import re


def open_url(url):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    res = requests.get(url, headers=headers)

    return res


def find_date(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    content = soup.find(class_="fjlist-box boxstyle1")
    target = content.find_all("li")
    for each in target:
        data.append(each.text.strip() + '\n')

    return data


    # print(data)


def main():
    url = "https://www.anjuke.com/fangjia/quanguo2019/"
    res = open_url(url)
    dates = find_date(res)

    with open("2019年各城市房价.txt", "w", encoding="utf-8")as file:
        for each in dates:
            file.write(each)



if __name__ == '__main__':
    main()