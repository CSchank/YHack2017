from datetime import datetime

def calcAge(birthday):
    born = datetime.strptime(birthday[0:10], "%Y-%m-%d")

    today = datetime.now()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

print(calcAge("1997-05-02T00:00:00Z"))