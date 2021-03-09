import argparse

class Server:
    def __init__(self, ppm):
        self.process_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_process() * 60 / self.process_rate



class Request:
    def __init__(self, time):
        self.timestamp = time
    def get_stamp(self):
        return self.timestamp
    def get_process(self):
        return self.process
    def wait_time(self, current_time):
        return current_time - self.timestamp

def Queue(csv_reader):
    from csv import reader
    with open("requests.csv") as file:
        csv_reader = reader(file)
        return csv_reader

def simulationOneServer(num_seconds, process_per_minute):
    main_server = Server(process_per_minute)
    server_queue = Queue(csv)
    waiting_times = []
    for current_second in range(num_seconds):
        if (not main_server.busy()) and (not server_queue.is_empty()):
            next_task = server_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            main_server.startNext(next_task)
        main_server.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." %(average_wait, server_queue.size()))


if __name__ == "__main__":
    """Main entry point"""

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="datafile needed", type=str, required=True)
    args = parser.parse_args()
    main(args.file)

    csvfile = ""
    results = simulationOneServer(csvfile)
    print(results)

#File will not run, I think the need for Queue() in the textbook code is throwing me off too much and I can't figure it out.