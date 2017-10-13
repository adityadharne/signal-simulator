class Signal:
    """
    Signal class
    """
    def signal_transition(self):
        """
        Checks and controls transitions to maintain order
        """

        if self.signal_now == "green":
            self.signal_now = "yellow"
        elif self.signal_now == "yellow":
            self.signal_now = "red"
        elif self.signal_now == "red":
            self.signal_now = "green"

    def __init__(self, green_duration=1, yellow_duration=1, red_duration=1, direction=1):
        """
        Initializing instance of Signal class
        :param green_duration: Time for green signal
        :param yellow_duration: Time for yellow signal
        :param red_duration: Time for red signal
        """
        with open('green.txt', 'r') as green:
            green_signal = green.read()
        with open('yellow.txt', 'r') as yellow:
            yellow_signal = yellow.read()
        with open('red.txt', 'r') as red:
            red_signal = red.read()

        green_signal = 'GREEN  '
        #if direction == 1:
        #   green_signal = 'RIGHT_GREEN  '
        #if direction == 0:
        #    green_signal = 'LEFT_GREEN  '
        #red_signal = 'RED  '
        #yellow_signal = 'YELLOW  '

        self.signal_now = 'red'
        self.ascii_signals = {"green": green_signal, "yellow": yellow_signal, "red": red_signal}
        self.signals_duration = {"green": green_duration, "yellow": yellow_duration, "red": red_duration}

