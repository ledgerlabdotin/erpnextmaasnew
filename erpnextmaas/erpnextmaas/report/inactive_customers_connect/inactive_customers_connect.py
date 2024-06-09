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
		if cust.days_since_last_connect and cust.days_since_last_connect >= cint(days_since_last_connect):
			data.append(cust)
		elif not cust.days_since_last_connect:
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
	query = """select
				cc.date, cc.time, cust.name, cust.customer_name,
				cc.connect_type, cc.value_created, cc.remarks,
				count(distinct(cc.name)) as num_of_connect,
				max(cc.date) as last_connect_date,
				DATEDIFF(CURRENT_DATE, max(cc.date)) as days_since_last_connect
			from `tabCustomer` as cust
			left join `tabCustomer Connect` as cc on cc.customer_name=cust.name
			group by cust.name
			order by days_since_last_connect desc
		"""
	return frappe.db.sql(query, as_dict=True)
