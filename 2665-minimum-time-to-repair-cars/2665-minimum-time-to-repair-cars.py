class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = max(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2
            #total cars can be repaired in mid time
            total_cars = 0
            for rank in ranks:
                total_cars += int((mid/rank) ** 0.5)

                #total_cars repaired > cars, try smaller value
            if total_cars >= cars:
                right = mid
            else:
                left = mid + 1
        return left