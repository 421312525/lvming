'''
@author:lvming
@time:2021/6/30
'''
import requests
import unittest
from ddt import data
import json
# url = 'https://uuap.baidu.com/login'
# data = {
#     'username':'v_lvming@baidu.com',
#     'password':'Yingying520',
# }
# res = requests.post(url=url,json=data)
# print(res.json)
class MeetAPiCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url1 = 'http://meeting.baidu.com/h5/book'
        cls.headers1 = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'BAIDUID=063177E415E2A2C9C9574C8F9CB8E281:FG=1; PSTM=1623473034; BIDUPSID=66884A0A2E083A5B7991362E1456979E; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=110085_127969_128699_146869_164870_171704_173293_174661_175553_175609_175756_176120_176158_176341_176678_176927_177086_177167_177225_177378_177400_177413_177417_177485_177586_177727_177734_177787_177943_178040_178076_178329_178384_178494_178628_178708_178772_178947_178992_179227_179347; BDSFRCVID=OqKOJeC62i3qmB5ecanbKww7smK55qjTH6-J9KsviESzsW6f2T5cEG0POM8g0KubLClVogKK0mOTHv-F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJIO_KPKtC83fP36qR6sMJ8thmT22-usbCtJ2hcH0KLKsU3cX4u-btt_0aJi-b-f-Kji_C5h2fb1M66_y5bEQn_lXhQwQfJvyTvn3h5TtUJo8DnTDMRh-RKSyxryKMnitIj9-pnKHlQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuD6-2DjvWDG0s-bbfHJIDWRTLHJOoDDv90bocy4LdjG50JboL0JT-3bjxaqvbfI3Rhf4hjJ_q3-AqexI8W57qBl5RMtORMRL435ojQfbQ0-nuqP-jW5Ta2pOsQJ7JOpkxhfnxyb5DQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6IHfRAHVIIhfCvbfP0k5boO5J8Q52T22-us5RRd2hcH0KLKjDbMjToDbtt_0MOi-b-f-2kt5JjaBMb1M66_0no-Lf705U8fQjvNajFjXp5TtUtWeCnTDMRh-l8lX-QyKMnitIj9-pnKHlQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuD6_WjTvBDH-s-bbfHjQ3B4JVajrjDnCr0bozXUI8LNDH0hbWBDKq0ROqLPQvfP06KPcvjjLLMRO7tDrZWn70K-juBPjFVlOyWbJx-UL1Db3yW6vMtg3t3tQJWJToepvoD-cc3MkBqtjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtJAjoCP5tDt3fP36q6_ahtFhqxby26n9-m39aJ5nJDoEhPjzL6oq-P_H-4Rf-5beam0t_4j_QpP-KqFwynb-MfL92lbUttKHQnT2Kl0MLp7Ybb0xynoDXMtj3xnMBMPjamOnaPLE3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-XDj3WDNOP; Hm_lvt_dd36164a9e003e90b07c432151422139=1623736963,1624240287,1624416476,1624845921; BSG_B_TOKEN=UGAku9bg5vV8BcXMmWftqyp4vbNIBVOI9UQgWdLFZv7UU4IEX4zvHPg1BCh/mlAN9YO5XKhY1gW4jxxPm22VOg==; H_PS_PSSID=34099_34222_31660_33848_34113_34073_33607_34135_34111_34215; BDUSS=NXampZZHFPSnRhR0lhNjFXbjhmUC1sUzBrfjY5RXVyU0Z2R0FHZUJMRGNGd1ZoRVFBQUFBJCQAAAAAAAAAAAEAAACgEqXRd2txYTAwMDAwMTMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANyK3WDcit1gcj; UUAP_P_TOKEN=PT-617491298593898496-WoKXtutvkA-uuap; UUAP_TRACE_TOKEN=0f0f381d5eac5b8bf2abb3867e1383dc; delPer=0; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; PSINO=6; JSESSIONID=7EAABD1DAD2C4BD1A3E7CD35726B9194; Hm_lpvt_dd36164a9e003e90b07c432151422139=1625192002',
            'Host': 'meeting.baidu.com',
            'Origin': 'http://meeting.baidu.com',
            'Pragma': 'no-cache',
            'Referer': 'http://meeting.baidu.com/index.html'
        }
    def test_meet_book1(self):
        self.data1={
            'roomKey':'10113559',
            'description':'吕明于2021-07-09 14:00在上江虹的会议室',
            'peopleNum':'16',
            'startTime':'1625810400000',
            'endTime':'1625814000000',
            't':'1625193000000'
        }
        res1 = requests.post(url=self.url1,json=self.data1,headers=self.headers1)
        return res1.text

    def test_meet_book2(self):
        self.data1={
            'roomKey':'10113559',
            'description':'吕明于2021-07-09 15:00在上江虹的会议室',
            'peopleNum':'16',
            'startTime':'1625814000000',
            'endTime':'1625817600000',
            't':'1625193000000'
        }
        res1 = requests.post(url=self.url1,json=self.data1,headers=self.headers1)
        return res1.text

    def test_meet_book3(self):
        self.data1={
            'roomKey':'10113559',
            'description':'吕明于2021-07-09 16:00在上江虹的会议室',
            'peopleNum':'16',
            'startTime':'1625817600000',
            'endTime':'1625821200000',
            't':'1625193000000'
        }
        res1 = requests.post(url=self.url1,json=self.data1,headers=self.headers1)
        return res1.text

    def test_meet_book4(self):
        self.data1={
            'roomKey':'10113559',
            'description':'吕明于2021-07-09 17:00在上江虹的会议室',
            'peopleNum':'16',
            'startTime':'1625821200000',
            'endTime':'1625824800000',
            't':'1625193000000'
        }
        res1 = requests.post(url=self.url1,json=self.data1,headers=self.headers1)
        return res1.text

    def test_meet_book5(self):
        self.data1={
            'roomKey':'961',
            'description':'吕明于2021-07-09 14:00在南乡子的会议室',
            'peopleNum':'15',
            'startTime':'1625810400000',
            'endTime':'1625814000000',
            't':'1625193000000'
        }
        res1 = requests.post(url=self.url1,json=self.data1,headers=self.headers1)
        return res1.text

    def test_meet_book6(self):
        self.data1 = {
            'roomKey': '961',
            'description': '吕明于2021-07-09 15:00在南乡子的会议室',
            'peopleNum': '15',
            'startTime': '1625814000000',
            'endTime': '1625817600000',
            't': '1625193000000'
        }
        res1 = requests.post(url=self.url1, json=self.data1, headers=self.headers1)
        return res1.text

    def test_meet_book7(self):
        self.data1 = {
            'roomKey': '961',
            'description': '吕明于2021-07-09 16:00在南乡子的会议室',
            'peopleNum': '15',
            'startTime': '1625817600000',
            'endTime': '1625821200000',
            't': '1625193000000'
        }
        res1 = requests.post(url=self.url1, json=self.data1, headers=self.headers1)
        return res1.text

    def test_meet_book8(self):
        self.data1 = {
            'roomKey': '961',
            'description': '吕明于2021-07-09 17:00在南乡子的会议室',
            'peopleNum': '15',
            'startTime': '1625821200000',
            'endTime': '1625824800000',
            't': '1625193000000'
        }
        res1 = requests.post(url=self.url1, json=self.data1, headers=self.headers1)
        return res1.text

if __name__ == '__main__':
    unittest.main()