import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/Login.ini")


class ReadConfig_Login():
    def getDevUrl(self):
        return config.get("Common Details", "dev_url")
