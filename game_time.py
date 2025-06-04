import time


class GameElapsedTime:
    """
    Simple class to have an in-game clock.
    """
    def __init__(self):
        self.start_time = time.time()
        self.elapsed_time = None
        self.pause_time_start = None

    def accumulate(self):
        """
        Called on each update to accumulate time.
        :return:
        """
        self.elapsed_time = time.time() - self.start_time
        return self.elapsed_time

    def get_time_string(self):
        """
        Used to get a nice formatted string to display
        :return: The time formatted as a string.
        """
        seconds = self.elapsed_time
        minutes = 0
        hours = 0

        if seconds % 60 == 0:
            return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        else:
            minutes = seconds // 60
            seconds = seconds % 60
            if minutes >= 60:
                hours = minutes // 60
                minutes = minutes % 60
            return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def pause(self):
        self.pause_time_start = time.time()

    def resume(self):
        pause_elapsed_time = time.time() - self.pause_time_start
        self.start_time += pause_elapsed_time

