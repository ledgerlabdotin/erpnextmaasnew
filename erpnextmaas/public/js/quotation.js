frappe.ui.form.on('Quotation', {
	refresh: function (frm) {
		if (frm.is_new()) {
			setseries(frm, frappe.session.user);
		}
	},
	validate: function (frm) {
		if (frm.is_new()) {
			setseries(frm, frappe.session.user);			
		}
	}
});   
   
function setseries(frm, user) {
	switch (user) {
		case "azar@maasconsult.co":  frm.set_value("naming_series", "MFC-JED-"); break;
		case "asheer@maasconsult.co":  frm.set_value("naming_series", "MFC-ALK-"); break;
		case "baseeth@maasconsult.co":  frm.set_value("naming_series", "MFC-RUH-"); break;
		case "islam@maasconsult.co":  frm.set_value("naming_series", "MFC-MED-"); break;
		case "zuhayr@maasconsult.co":  frm.set_value("naming_series", "MFC-DMM-"); break;
		case "naveeduddin@maasconsult.co":  frm.set_value("naming_series", "MFC-OFMC-"); break;
		case "alam@maasconsultancy.com": frm.set_value("naming_series", "MFC-JUB-"); break;
	}
}