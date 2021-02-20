from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    start, end = [], []
    for time in intervals:
        start.append(time[0])
        end.append(time[1])

    start.sort()
    end.sort()
    i, j = 0, 0
    max_room, room_n = 0, 0

    while i < len(intervals):
        room_n += 1
        if end[j] <= start[i]:
            room_n -= 1
            j += 1
        i += 1
        max_room = max(max_room, room_n)

    return max_room


if __name__ == '__main__':
    assert minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert minMeetingRooms([[7, 10], [2, 4]]) == 1
