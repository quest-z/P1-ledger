import json

FILENAME = "ledger.json"


class Bill:
    def __init__(self,amount,category,date,note):
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    def to_dict(self):
        return vars(self)


    def __str__(self):
        return f"账单数目:{self.amount};类别:{self.category},日期:{self.date};备注:{self.note}"

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


def main():
    ledger = load_ledger()
    while True:
        print("====记账本====")
        print("1:记一笔  2:全部账单  3:按类别汇总  4:按日期汇总  5:总支出  6:退出")
        choice = input("> ").strip()
        if choice == "1":
            try:
                in_amount=float(input("数目:"))
            except ValueError:
                print("请输入合法值")
                continue
            in_category=input("类别:")
            in_date=input("日期:")
            in_note=input("备注:")
            new_bill=Bill(in_amount,in_category,in_date,in_note)
            ledger.add_bill(new_bill)
        elif choice == "2":
            ledger.list_all()
        elif choice == "3":
            for k,total in ledger.summary_all("category").items():
                print(f"{k}:{total}")
        elif choice == "4":
            for k,total in ledger.summary_all("date").items():
                print(f"{k}:{total}")
        elif choice == "5":
            print(ledger.total_amount())
        elif choice == "6":
            save_ledger(ledger)
            print("已保存,再见!")
            break
        else:
            print("请输入正确选项")



if __name__ == "__main__":
    main()
