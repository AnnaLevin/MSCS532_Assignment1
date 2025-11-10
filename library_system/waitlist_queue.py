# waitlist_queue.py
from collections import deque
waiting_list = deque()

def add_to_waitlist(user):
    waiting_list.append(user)

def next_in_line():
    if waiting_list:
        return waiting_list.popleft()
    return None
