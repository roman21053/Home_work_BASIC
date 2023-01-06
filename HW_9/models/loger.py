from datetime import datetime


class CustomManager:
    def __init__(self, name_file, mode="r"):
        self.name_file = name_file
        self.file = open(name_file, mode)
        self.time_open = datetime.now()
        self.open_logs = open('./logs/logs.txt', 'a')

    def __enter__(self):
        log_open = f'{self.time_open} {self.name_file} OPEN\n'
        self.open_logs.write(log_open)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        time_close = datetime.now()
        log_close = f'{time_close} {self.name_file} CLOSE\n'
        self.open_logs.write(log_close)
        self.open_logs.close()

