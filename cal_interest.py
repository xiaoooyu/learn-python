from sys import argv
from datetime import datetime
from datetime import date

script, principle, principle_with_interest, begin_date = argv

today = date.today()
begin = datetime.strptime(begin_date, "%m/%d/%Y").date()

diff_day = abs((today - begin).days)

pwi_value = float(principle_with_interest)
p_value = float(principle)

print (pwi_value - p_value) / p_value / diff_day * 365

# print diff_day





