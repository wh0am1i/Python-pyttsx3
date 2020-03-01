import pyttsx3
import requests
import time

import schedule
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'


def get_data():
    resp = requests.get(url, headers=headers).json()
    today = resp['data']['chinaTotal']['today']
    total = resp['data']['chinaTotal']['total']
    return today, total


def say_data(today, total):
    engine = pyttsx3.init()
    now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    print(now)
    engine.say('截止北京时间' + now)
    engine.say('确诊病例较昨日新增' + str(today['confirm']) + '人')
    engine.say('疑似病例较昨日新增' + str(today['suspect']) + '人')
    engine.say('康复人数较昨日新增' + str(today['heal']) + '人')
    engine.say('死亡人数较昨日新增' + str(today['dead']) + '人')
    engine.say('截止北京时间' + now)
    engine.say('全国累计确诊病例' + str(total['confirm']) + '人')
    engine.say('全国累计疑似病例' + str(total['suspect']) + '人')
    engine.say('全国累计康复总人数' + str(total['heal']) + '人')
    engine.say('全国累计累计死亡人数' + str(total['dead']) + '人')
    engine.runAndWait()


def main():
    today, total = get_data()
    say_data(today, total)


if __name__ == '__main__':
    schedule.every().day.at("23:00").do(main)
    while True:
        schedule.run_pending()



