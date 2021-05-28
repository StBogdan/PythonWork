from collections import defaultdict
from typing import Dict, Tuple

# Name: Design Underground System
# Link: https://leetcode.com/problems/design-underground-system/
# Method: 2 dictionaries, started journeys and a dict of pairwise of averages
# Time: O(1)
# Space: O(n)
# Difficulty: Medium


Id = int
Station = str
Time = int
Journey = Tuple[Station, Station]


class UndergroundSystem:
    def __init__(self):
        self.completed_journeys: Dict[Journey, Tuple[int, int]] = defaultdict(
            lambda: (0, 0)
        )
        self.started_journey: Dict[Id, Tuple[Station, Time]] = {}

    def checkIn(self, id: Id, station_name: Station, start_time: Time) -> None:
        self.started_journey[id] = (station_name, start_time)

    def checkOut(self, id: int, station_name: str, end_time: int) -> None:
        end_station = station_name
        start_station, start_time = self.started_journey[id]

        del self.started_journey[id]
        self._update_travel_time((start_station, end_station), end_time - start_time)

    def _update_travel_time(
        self, journey: Tuple[Station, Station], new_journey_time: int
    ):
        start_s, end_s = journey
        avg_now, journeys = self.completed_journeys[(start_s, end_s)]

        new_avg = (avg_now * journeys + new_journey_time) / (journeys + 1)

        self.completed_journeys[(start_s, end_s)] = (new_avg, journeys + 1)

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        average_travel_time, _ = self.completed_journeys[(start_station, end_station)]
        return average_travel_time
