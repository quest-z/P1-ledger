from bill import Bill
from ledger import Ledger

def test_total_amount():
    """记两笔，总支出应该是 35"""
    ledger = Ledger()
    ledger.record_bill(10, "交通", "2026-09-20", "公交")
    ledger.record_bill(25, "饮食", "2026-09-20", "午饭")
    assert ledger.total_amount() == 35

def test_summary_category():
    ledger = Ledger()
    ledger.record_bill(20,"交通","2026-09-20","无")
    ledger.record_bill(10,"交通","2026-9-20","无")
    ledger.record_bill(25,"饮食","2026-09-24","无")
    result=ledger.summary_all("category")
    assert result == {'交通': 30, '饮食': 25}

def test_to_dict_round_trip():
    bill = Bill(10,"交通","2026-09-20","无")
    data=bill.to_dict()
    data2=Bill(**data)
    assert bill.amount == data2.amount
    assert bill.category == data2.category
    assert bill.date == data2.date
    assert bill.note == data2.note