from time import ticks_ms, ticks_diff
import machine


class LoggerInMemory:

    _levels = {
        "DEBUG": 1,
        "INFO": 2,
        "WARN": 3,
        "ERROR": 4
    }

    last_log_time_ms = 0

    def __init__(self, level, print_output=True):
        self.print_output = print_output
        level = level.upper()
        if level not in self._levels:
            raise ValueError('Unknown log level: ' + level)
        self.level_numeric = self._levels[level]
        self.rtc = machine.RTC()
        self.logs = []  # Store logs in a list

    def init(self, start_time, print_output):
        self.last_log_time_ms = start_time
        self.print_output = print_output
        self.info("logger initialized")

    def set_level(self, level):
        level = level.upper()
        if level not in self._levels:
            raise ValueError('Unknown log level: ' + level)
        self.level_numeric = self._levels[level]

    def set_print_output(self, print_output):
        self.print_output = print_output

    def debug(self, msg):
        self._log("DEBUG", msg)

    def info(self, msg):
        self._log("INFO", msg)

    def warn(self, msg):
        self._log("WARN", msg)

    def error(self, msg):
        self._log("ERROR", msg)

    def _log(self, level, msg):
        level = level.upper()
        if not self._filter_on_level(level):
            return

        current_time_ms = ticks_ms()
        elapsed_time_ms = ticks_diff(current_time_ms, self.last_log_time_ms)
        self.last_log_time_ms = current_time_ms

        log_entry = f"{self._format_time(self.rtc.datetime())} {level}: {msg} ({elapsed_time_ms}ms)"
        self.logs.append(log_entry)  # Append the log entry to the list

        if self.print_output:
            print(log_entry)

    def _filter_on_level(self, level):
        return self._levels[level] >= self.level_numeric

    @staticmethod
    def _format_time(timestamp):
        microseconds = timestamp[7] // 1000
        return f'{timestamp[0]:04d}-{timestamp[1]:02d}-{timestamp[2]:02d} {timestamp[4]:02d}:{timestamp[5]:02d}:{timestamp[6]:02d}.{microseconds:03d}'

    def get_logs(self):
        return self.logs  # Return the list of logs

    def clear_logs(self):
        self.logs.clear()  # Clear the log list

    def print_logs(self):
        for log in self.logs:
            print(log)


# Initialize the in-memory logger
log = LoggerInMemory("INFO")
