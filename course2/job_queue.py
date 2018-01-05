# python3
from queue import PriorityQueue


class Thread(object):
    def __init__(self, idx):
        self.idx = idx
        self.free_time = 0

    def __lt__(self, other):
        # Comparison: if free_time is equal, fall back to comparing idx.
        if self.free_time == other.free_time:
            return self.idx < other.idx
        else:
            return self.free_time < other.free_time


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        '''
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]
        '''
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        queue = PriorityQueue()

        # Instantiate thread queue.
        for i in range(self.num_workers):
            queue.put(Thread(i))

        # Iterate through jobs, getting the next available thread from the front of the queue.
        for i in range(len(self.jobs)):
            thread = queue.get()
            #print('Job {}: got thread {}, free at {}, finish at {}'.format(i, thread.idx, thread.free_time, thread.free_time + self.jobs[i]))
            self.assigned_workers[i] = thread.idx
            self.start_times[i] = thread.free_time
            thread.free_time += self.jobs[i]
            queue.put(thread)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
