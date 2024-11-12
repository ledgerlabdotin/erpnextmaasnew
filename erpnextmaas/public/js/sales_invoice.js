frappe.ui.form.on("Sales Invoice", {
	refresh: function (frm) {
		if (frm.doc.docstatus == 1) {
			const item_codes = ["OBG", "OBS", "SOB"];
			const exists = frm.doc.items.some((item) =>
				item_codes.includes(item.item_code)
			);

			if (exists) {
				frm.add_custom_button(
					__("Onboarding"),
					function () {
					frm.trigger("make_onboarding");
					},
					__("Create")
				);
			}
		}
	},
	make_onboarding: function (frm) {
		frappe.model.open_mapped_doc({
			method: "erpnextmaas.erpnextmaas.hook_events.sales_invoice.make_onboarding",
			frm: frm,
		});
	},
});
