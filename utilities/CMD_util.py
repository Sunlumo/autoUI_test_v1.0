import os


def cmd_runner(command):
    d = os.popen(command)
    print(d.read())
    return d.read()

cmd_runner("allure --version")