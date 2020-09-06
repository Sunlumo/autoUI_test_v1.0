import time


class GetTime(object):

    def __init__(self):
        self.i = 1
        self.time = None

    def get_time(self):
        if self.i == 1:
            self.time = time.strftime("%Y%m%d%H%M", time.localtime())
            self.i = 2
            return self.time
        else:
            return self.time

    def get_time_now(self):
        return time.strftime("%Y%m%d%H%M", time.localtime())
