from datetime import *

class Technic():
    def __init__(self, name, date_buy, guarantee):
        self.name = name
        self.date_buy = date_buy
        self.guarantee = guarantee

    def is_guarantee(self):
        date_buy = datetime.strptime(self.date_buy, "%d.%m.%Y")
        now = datetime.now()
        return (now - date_buy).days > int(self.guarantee)

    def get_info(self):
        print(f"Name: {self.name}\nDate of buy: {self.date_buy}\nGuarantee: {self.guarantee}\n")