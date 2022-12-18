import time
from abc import ABCMeta, abstractmethod
from abstract import Observer, Observable

class Account(Observable):
    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}
        
    def login(self, name, ip ,time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({
                "name":name,
                "ip":ip,
                "region":region,
                "time":time
            })
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip
    
    def __getRegion(self, ip):
        ipRegions = {
            "101.47.18.91": "杭州",
            "67.218.147.69":"洛杉磯"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region
    
    def __isLongDistance(self, name, region):
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region

class SmsSender(Observer):
    def update(self, observable, object):
        print("[SMS Confirm]" + object["name"] + "您好！您的登入訊息有以下的紀錄。最近一次登入訊息：\n 登入地區：" + object["region"] + "\n 登入IP：" + object["ip"] + "\n 登入時間：" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))
        
class MailSender(Observer):
    def update(self, observable, object):
        print("[Mail Confirm]" + object["name"] + "您好！您的登入訊息有以下的紀錄。最近一次登入訊息：\n 登入地區：" + object["region"] + "\n 登入IP：" + object["ip"] + "\n 登入時間：" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))
        
def testLogin():
    account = Account()
    account.addObserver(SmsSender())
    account.addObserver(MailSender())
    account.login("Tony","101.47.18.91", time.time())
    account.login("Tony","67.218.147.69", time.time())

testLogin()