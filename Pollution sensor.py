class PollutionSensor:
    """
    A class to represent a pollution sensor.

    Attributes:
    - data: A dictionary to store pollution data with time as keys.
    
    Methods:
    - add(time, value): Add pollution data at a specific time.
    - delete(operation_time, target_time): Delete pollution data between two times.
    - query(time): Query the total pollution up to a specific time.
    """

    def __init__(self):
        self.data = {}

    def add(self, time=int, value=float):
            """
            Add pollution data at a specific time.

            Parameters:
            - time: The time at which the pollution data is recorded.
            - value: The pollution value to be added.
            """

            if time in self.data:
                self.data[time] += value
            else:
                self.data[time] = value

    def delete(self, operation_time=int, target_time=int):
        """
        Delete pollution data between two times.

        Parameters:
        - operation_time: The time at which the delete operation is performed.
        - target_time: The time before which the pollution data is deleted.
        """

        try:
            if target_time in self.data and target_time < operation_time:
                self.data[operation_time] = self.data.get(operation_time, 0) - self.data.get(target_time, 0)
            else:
                raise ValueError("Error: target_time must be less than operation_time for delete operation.")
        except ValueError as e:
            print(e)

    def query(self, time=int):
        """
        Query the total pollution up to a specific time.
        
        Parameters:
        - time: The time up to which the total pollution is queried.
        
        Returns:
        - total_pollution: The total pollution up to the specified time.
        """

        total_pollution = 0
        for t, v in self.data.items():
            if t <= time:
                total_pollution += v
        return total_pollution
    
sensor = PollutionSensor()
sensor.add(-3, -2)
sensor.add(4, 1)
sensor.delete(2,-3)
sensor.add(-4, -2)
sensor.delete(3 , -4)

print(sensor.query(5))  