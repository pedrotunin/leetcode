from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def howLong(p: int, s: int) -> float:
            return (target - p) / s

        pos_speed = sorted(list(zip(position, speed)), reverse=True)

        times = [howLong(p, s) for p, s in pos_speed]

        last = times[0]
        res = 1
        for i, time in enumerate(times):
            if time > last:
                res += 1
                last = time

        return max(1, res)
