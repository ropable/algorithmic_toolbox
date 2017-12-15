# python3
import sys
from collections import deque


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque([])

    def process(self, request):
        # First, pop from the front all the packets that should be finished when the
        # request should join the buffer.
        while self.finish_time and self.finish_time[0] <= request.arrival_time:
            self.finish_time.popleft()

        # For each request, try to store its finish time in the finish_time queue.
        # Check if there is room in the buffer.
        if len(self.finish_time) == self.size:  # There is no room in the buffer.
            return Response(True, -1)

        # If self.finish_time is empty when a request arrives, it will start processing immediately.
        if len(self.finish_time) == 0:  # Empty queue.
            self.finish_time.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        else:
            # If finish_time was not empty, packet will start when the last element in the buffer finishes.
            # Append the new request's finish time to the queue.
            self.finish_time.append(self.finish_time[-1] + request.process_time)
            # Return the finish time of the request before this one (will be its start time).
            return Response(False, self.finish_time[-2])


def read_requests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, sys.stdin.readline().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def process_requests(requests, buff):
    responses = []
    for request in requests:
        responses.append(buff.process(request))
    return responses


def print_responses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


if __name__ == "__main__":
    size, count = map(int, sys.stdin.readline().split())
    requests = read_requests(count)
    buff = Buffer(size)
    responses = process_requests(requests, buff)
    print_responses(responses)
