import json
from bill import Bill
FILENAME = "ledger.json"


class Ledger:
    def __init__(self):
        self.bills = []

    def add_bill(self,bill):
        self.bills.append(bill)

    def list_all(self):
        for bill in self.bills:
            print(bill)


    def summary_all(self,key):
        """按照不同属性'category''date'计算金额,返回类别支出"""
        summary={}
        for bill in self.bills:
            k=getattr(bill,key)
            summary[k]=summary.get(k,0)+bill.amount
        return summary

    def total_amount(self):
        """返回总支出"""
        return sum(bill.amount for bill in self.bills)

    def record_bill(self,amount,category,date,note):
        bill = Bill(amount,category,date,note)
        self.add_bill(bill)

def save_ledger(ledger):
    data = [b.to_dict() for b in ledger.bills]
    with open(FILENAME,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

def load_ledger():
    ledger = Ledger()
    try:
        with open(FILENAME,"r",encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return ledger
    for d in data:
        bill = Bill(**d)
        ledger.add_bill(bill)
    return ledger
