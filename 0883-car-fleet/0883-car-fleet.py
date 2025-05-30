class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        fleets = 0
        fleet_time = 0
        sorted_pair = sorted(pair, reverse = True)
        for p,s in sorted_pair:
            current_fleet_time = (target - p) / s
            if current_fleet_time > fleet_time:
                fleets += 1
                fleet_time = current_fleet_time
        return fleets
            