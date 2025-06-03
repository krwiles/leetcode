from collections import deque
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        key_set = set()
        box_queue = deque(initialBoxes)
        box_set = set(initialBoxes)
        candy = 0

        # Loop through the queue
        while box_queue:
            box = box_queue.popleft()  # pop box from queue

            if candies[box] == 0:  # Box has been visited
                continue
            if status[box] == 0 and box not in key_set:  # Box unopenable
                continue

            # Take candy from box and set to open
            candy += candies[box]
            candies[box] = 0
            status[box] = 1

            # Check contained boxes
            for b in containedBoxes[box]:
                box_set.add(b)  # Add to box set
                if status[b] == 1 or b in key_set:  # If openable, add to queue
                    box_queue.append(b)

            # Check contained keys
            for key in keys[box]:
                key_set.add(key)  # Add to key set
                if status[key] == 0 and key in box_set:  # If unopened box is available, add to queue
                    box_queue.append(key)

        return candy
