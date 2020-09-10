import time


class GetTime(object):

    def __init__(self):
        self.i = 1
        self.time = None

    def get_date(self):
        if self.i == 1:
            self.time = time.strftime("%Y%m%d", time.localtime())
            self.i = 2
            return self.time
        else:
            return self.time

    @staticmethod
    def get_time_now():
        return time.strftime("%Y%m%d%H%M", time.localtime())