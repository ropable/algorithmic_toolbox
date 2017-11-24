# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []

    while segments:
        # Safe move: take the segment with the smallest end coord.
        s = min(segments, key=lambda x: x.end)
        points.append(s.end)
        # Separate any segments still not covered by this point.
        segments = [i for i in segments if i.start > s.end]

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
