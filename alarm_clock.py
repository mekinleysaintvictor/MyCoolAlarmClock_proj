class AlarmClock:
    def __init__(self, current_time = "10:00am", alarm_time = "8:00am", alarm_status = "on"):
        self.current_time = current_time
        self.alarm_time = alarm_time
        self.alarm_status = alarm_status

    #Getter and setter for current time
    def get_current_time(self):
        return self.current_time

    def set_current_time(self, time):
        self.current_time = time

    #Getter amd setter for alarm time
    def get_alarm_time(self):
        return self.alarm_time

    def set_alarm_time(self, time):
        self.alarm_time = time

    #Getter and toggle functions for alarm
    def get_alarm_status(self):
        return self.alarm_status

    def toggle_alarm_on(self):
        self.alarm_status = "on"

    def toggle_alarm_off(self):
        self.alarm_status = "off"
