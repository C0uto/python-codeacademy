import datetime as dt
import custom_module
from decimal import Decimal
from random import choice
from random import randint

current_date_time = dt.datetime.now()
print(current_date_time)

year = randint(1900,3000)

base_cost = Decimal('1.00')
cost_multiplier = abs(current_date_time.year - year)
cost = base_cost * cost_multiplier

travels = choice(['Lisboa', 'Londres', 'Nova Iorque', 'Tokio'])

print(custom_module.generate_time_travel_message(year, travels ,cost))

