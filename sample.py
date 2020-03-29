import time

class Sample(object):
    def do_something(self):
        self._take_a_long_time()
        return 'Hello, World!'
    def _take_a_long_time(self):
        time.sleep(10)