# Copyright (c) 2024, malikhamzaali48@gmail.com and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.utils import cint


def execute(filters=None):
	if not filters:
		filters = {}

	days_since_last_connect = filters.get("days_since_last_connect")

	if cint(days_since_last_connect) <= 0:
		frappe.throw(_("'Days Since Last Connect' must be greater than zero"))

	columns = get_columns()
	customers_connects_list = get_data()

	data = []
	for cust in customers_connects_list:
		if cust.days_since_last_connect >= cint(days_since_last_connect):
			data.append(cust)
	return columns, data


def get_columns():
	columns = [
		{
			"fieldname": "date",
			"fieldtype": "Date",
			"label": _("Date"),
			"width": 120,
		},
		{
			"fieldname": "time",
			"fieldtype": "Time",
			"label": _("Time"),
			"width": 100,
		},
		{
			"fieldname": "customer_name",
			"fieldtype": "Link",
			"label": _("Customer"),
			"options": "Customer",
			"width": 250,
		},
		{
			"fieldname": "connect_type",
			"fieldtype": "Data",
			"label": _("Connect Type"),
			"width": 120,
		},
		{
			"fieldname": "value_created",
			"fieldtype": "Data",
			"label": _("Value Created"),
			"width": 300,
		},
		{
			"fieldname": "remarks",
			"fieldtype": "Data",
			"label": _("Remarks"),
			"width": 500,
		},
	]

	return columns


def get_data():
	return frappe.db.sql("""select
			date, time, customer_name,
			connect_type, value_created, remarks,
			count(distinct(name)) as num_of_connect,
			max(date) as last_connect_date,
			DATEDIFF(CURRENT_DATE, max(date)) as days_since_last_connect
		from `tabCustomer Connect`
		group by customer_name
		order by days_since_last_connect desc
	""", as_dict=True)
