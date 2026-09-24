from ledger import load_ledger, save_ledger


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
            ledger.record_bill(in_amount,in_category,in_date,in_note)
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
