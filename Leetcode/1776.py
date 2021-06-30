from collections import deque
from typing import List


# Name: Car Fleet II
# Link: https://leetcode.com/problems/car-fleet-ii/
# Method: Grafical intuition, monotonic queue building from the end with cars to futher crash into
# Time: O(n)
# Space: O(n)
# Difficulty: Hard


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        coll_times = [-1 for _ in range(len(cars))]

        next_cars = deque()
        next_cars.append((cars[-1], len(cars) - 1))

        for idx in range(len(cars) - 2, -1, -1):
            car_now = cars[idx]

            # Not crashing into the car in front, don't care (and any further ones will crash into this one)
            while next_cars and self.calc_collision(car_now, next_cars[-1][0]) == -1:
                next_cars.pop()

            # Crashing into the next after after it itself has crashed
            if next_cars:
                while (
                    coll_times[next_cars[-1][1]] != -1
                    and self.calc_collision(car_now, next_cars[-1][0])
                    > coll_times[next_cars[-1][1]]
                ):
                    next_cars.pop()

                coll_times[idx] = self.calc_collision(cars[idx], next_cars[-1][0])

            next_cars.append((car_now, idx))
            idx -= 1
        return coll_times

    @staticmethod
    def calc_collision(back_car: List[int], front_car: List[int]) -> int:
        back_poz, back_speed = back_car
        front_poz, front_speed = front_car
        if front_speed >= back_speed:
            return -1
        else:
            return (front_poz - back_poz) / (back_speed - front_speed)
