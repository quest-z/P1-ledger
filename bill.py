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