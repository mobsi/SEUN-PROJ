import csv
from datetime import date, datetime
from functools import reduce
from tenant import Tenant

with open('data.csv', newline='') as sheet:
	rd = csv.reader(sheet, delimiter=",")

	next(rd)

	rd = filter(lambda t: t.date_of_poss.strip(), map(Tenant._make, rd))

	for tenant in sorted(rd, key=lambda t: t.debit, reverse=True):
		print(f'{tenant.name.title()} = {tenant.debit}')