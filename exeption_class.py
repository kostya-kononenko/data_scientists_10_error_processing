class ExceptionPrintSendData(Exception):
    """ Клас виключення при відправки даних на принтер"""

    def __init__(self, *args):
        self.messages = args[0] if args else None

    def __str__(self):
        return f'Помилка: {self.messages}'


class PrintDate:
    def print(self, data):
        self.send_data(data)
        print(f'Друкуємо: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('Принтер не відповідає')

    def send_to_print(self, data):
        return False


