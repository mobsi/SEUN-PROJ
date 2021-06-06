from datetime import datetime, timedelta
from collections import namedtuple
from functools import reduce

import calendar
import re

def nmo(a, b):
	l, b0 = 1, b % 12
	while ((a + l) % 12) != b0:
		l += 1
	return l

def num(obj, num=0):
	try:
		num = float(obj)
	except ValueError as e:
		num = float(obj.replace(',', '') or 0.0)
	return num;

srv_charge = 100_000 / 12

empty_slots = ['<empty>'] * 15

slots = [
	'name',
	'date_of_poss',
	'plot_no',
	'poss',
	'tenant',
	'amount',
	'y2019_2020',
	'y2020_2021',
	'y2021_2022',
	'owing',
	'phone',
	'actual_date_of_poss'
] + empty_slots

TenantRecord = namedtuple('TenantRecord', slots, rename=True)

class Tenant(TenantRecord):
	@property
	def credit(self):
		fields = filter(lambda k: re.match('y\\d+', k), TenantRecord._fields)
		amount = reduce(lambda o, i: o + i, [num(getattr(self, k)) for k in fields])

		return round(amount, 2)
	
	@property
	def debit(self):
		if not self.date_of_poss.strip():
			return None

		dop = datetime.strptime(self.date_of_poss.strip(), '%m/%d/%Y')
		amount = 0.0
		period = 3

		if dop.month < 5:
			amount += ((5 - dop.month) * srv_charge)

		while period:
			# TODO ndays = (calendar.isleap(dop.year) and 366) or 365
			nxt = dop + timedelta(days=365)

			if nxt > datetime.now():
				nxt = datetime.now()
				mo_count = nmo(dop.month, nxt.month) - 1
				dop_mo_days = calendar.monthrange(dop.year, dop.month)[1]
				nxt_mo_days = calendar.monthrange(nxt.year, nxt.month)[1]

				if dop.day == 1:
					mo_count += 1
				if nxt.day == nxt_mo_days or (nxt.day + dop.day) >= dop_mo_days:
					mo_count += 1
				amount += (mo_count * srv_charge)
				period = 1
			else:
				amount += 100_000
			period -= 1
			dop = nxt

		return round(amount - self.credit, 2)