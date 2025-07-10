import configparser

config = configparser.RawConfigParser()
config.read("Configuration/Login.ini")

class ReadConfig_Login:
    def getDevUrl(self):
        return config.get('Common Details', 'dev_url')

    def getUserName(self):
        return config.get('Login Details', 'username')

    def getPassword(self):
        return config.get('Login Details', 'password')

