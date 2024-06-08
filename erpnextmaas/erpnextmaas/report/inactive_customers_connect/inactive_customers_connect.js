// Copyright (c) 2024, malikhamzaali48@gmail.com and contributors
// For license information, please see license.txt

frappe.query_reports["Inactive Customers Connect"] = {
	"filters": [
		{
			fieldname: "days_since_last_connect",
			label: __("Days Since Last Connect"),
			fieldtype: "Int",
			default: 10,
		},
	]
};
