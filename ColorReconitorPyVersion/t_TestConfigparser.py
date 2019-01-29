import configparser

# by using config[section][key] = value to change the value won't affect other params :-)
# tested by Alex Beng

if __name__ == "__main__":
    config = configparser.ConfigParser()

    # config["233"] = {'244': '1',
    #                  '255': '2'}
    # with open("../BackupSource/test.ini", "w") as r:
    #     config.write(r)
    

    config.read("../BackupSource/test.ini")
    config["233"]["244"] = '2'
    print(config["233"]["255"])

    with open("../BackupSource/test.ini", "w") as r:
        config.write(r)