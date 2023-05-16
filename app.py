import datetime as dt

date_format = '%d.%m.%Y'
now = dt.datetime.now()
td = now.date()
print(now)
print(td)
class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date = date
        self.comment = comment

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        records = []
    def add_record(self, Record):
        records.append(Record)
    
class CashCalculator(Calculator):
    def get_today_stats(self):
        sum = 0
        for r in records:
            if r.date == now.date():
                sum += r.amount
        print(f"Сегодня, {now.date()}, потрачено {sum} руб")
        







# для CashCalculator 
r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")


    
