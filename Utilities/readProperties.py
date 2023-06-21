import configparser
from datetime import datetime

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

class ReadConfig():
    @staticmethod #to access directly to the class without an object
    def getAplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    def getEmail():
        email = config.get('common info', 'email')
        return email



