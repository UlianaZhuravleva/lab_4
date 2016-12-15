import time


class timer:
    def __enter__(self):
        self.begin_time=time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        self.end_time=time.time()
        print(round(self.end_time-self.begin_time,1))
