class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        for i in range(len(position)):
            position[i] = (position[i], speed[i])
        position.sort()
        for i in range(len(position)-1, -1, -1):
            time = ((target - position[i][0]) / position[i][1])
            fleet.append(time)
            if len(fleet) > 1 and fleet[-2] >= time:
                fleet.pop()
        return len(fleet)
        