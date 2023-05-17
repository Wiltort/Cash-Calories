import datetime as dt

date_format = '%d.%m.%Y'
now = dt.datetime.now()
td = now.date()

class Record:
    def __init__(self, amount, date='', comment):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = td
        else:
            self.date = dt.datetime.strptime(date, date_format).date()
        

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, Record):
        self.records.append(Record)
    def get_today_stats(self):
        tsumma = 0
        for r in self.records:
            if r.date == td:
                tsumma += r.amount
        return tsumma
    def get_week_stats(self):
        wsumma = 0
        today = dt.date.today()
        week_ago = today - dt.timedelta(days = 7)
        for r in self.records:
            if week_ago<=r.date<=today:
                wsumma += r.amount
        return wsumma

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        diff = self.limit - self.get_today_stats()
        if self.get_today_stats() < self.limit:
            print(f"Сегодня можно съесть что-нибудь ещё, но с общей
                  калорийностью не более {diff} кКал")
        else:
            print("Хватит есть!")
    

    
class CashCalculator(Calculator):
    USD_RATE = 80
    EUR_RATE = 88
    def get_today_cash_remained(self,currency):
        diff = self.limit - self.get_today_stats()
        if currency == rub:
            rate = 1
        elif currency = usd:
            rate = USD_RATE
        else:
            rate = EURO_RATE
        diff = diff/rate
        if diff>0:
            print(f"На сегодня осталось {diff} {currency}")
        elif diff == 0:
            print("Денег нет, держись")
        else:
            print("Денег нет, твой долг - {-diff} {currency}")
        