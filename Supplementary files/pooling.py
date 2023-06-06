import multiprocessing
import time

class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        self.id = id
    def run(self):
        time.sleep(1)
        print (f"I'm the process with id {self.id}")

if __name__ == '__main__':
    processes = list(Process(i) for i in range(3))
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(type(processes))
