from typing import Optional

import data
from data import Rectangle


# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: data.Point, p2: data.Point)->Rectangle:
    if p1.x > p2.x:
        x1 = p1.x
        x2 = p2.x
    else:
        x1 = p2.x
        x2 = p1.x

    if p1.y > p2.y:
        y2 = p1.y
        y1 = p2.y
    else:
        y2 = p2.y
        y1 = p1.y

    top_left = data.Point(x2, y2)
    bot_right = data.Point(x1, y1)

    return data.Rectangle(top_left, bot_right)
    """    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0"""
# Part 2
def shorter_duration_than(dur1: data.Duration, dur2: data.Duration)->bool:
    return dur1.minutes < dur2.minutes or (dur1.minutes == dur2.minutes and dur1.seconds < dur2.seconds)

# Part 3
def songs_shorter_than(songs: list[data.Song], dur: data.Duration)->list[data.Song]:
    songs_shorter = []

    for song in songs:
        if shorter_duration_than(song.duration, dur):
            songs_shorter.append(song)
    return songs_shorter

# Part 4
def running_time(songs: list[data.Song], nums: list[int])->data.Duration:
    tot_sec = 0
    tot_min = 0

    for idx in range(len(songs)):
        for num in nums:
            if idx == num:
                temp_dur = songs[idx]
                tot_min += temp_dur.duration.minutes
                tot_sec += temp_dur.duration.seconds

    while tot_sec > 59:
        tot_sec -= 60
        tot_min += 1

    return data.Duration(tot_min, tot_sec)

# Part 5
#Check the route list and make a new list of each two elements
#then compare the lists with the nested lists in city_links
def validate_route(city_links: list[list[str]], route: list[str])->bool:
    for i in range(len(route)-1):
        link = [route[i], route[i + 1]]
        reverse_link = [route[i + 1], route[i]]
        if (link not in city_links) and (reverse_link not in city_links):
            return False
    return True

# Part 6
def largest_repetition(integers: list[int])->Optional[int]:
    if integers == []:
        return None
    count = 1
    start_idx = 0
    largest_idx = 0
    longest_count = 0

    for idx in range(len(integers)-1):
        if integers[idx] == integers[idx + 1]:
            count += 1
        else:
            start_idx = idx + 1
            count = 1
        if count > longest_count:
            longest_count = count
            largest_idx = start_idx
    return largest_idx