import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/Login.ini")


class ReadConfig_Login():

    def getDevUrl(self):
        return config.get("Common Details", "dev_url")

    def getusername(self):
        return config.get("Login Details", "username")

    def getpassword(self):
        return config.get("Login Details", "password")