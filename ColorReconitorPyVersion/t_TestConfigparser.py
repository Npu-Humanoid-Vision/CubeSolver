import configparser
import numpy as np

# by using config[section][key] = value to change the value won't affect other params :-)
# tested by Alex Beng

if __name__ == "__main__":
    config = configparser.ConfigParser()

    # config["233"] = {'244': '1',
    #                  '255': '2'}
    # with open("../BackupSource/test.ini", "w") as r:
    #     config.write(r)
    

    # config.read("../BackupSource/test.ini")
    # config["233"]["244"] = '2'
    # print(config["233"]["255"])

    # with open("../BackupSource/test.ini", "w") as r:
    #     config.write(r)

    test_np = np.array([[0, 1, 1], [2, 3, 3]], dtype="float64")
    test_np[0][1] /= 2
    print(test_np)