frappe.ui.form.on('Opportunity', {
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
		case "azar@maasconsult.co":  frm.set_value("naming_series", "MFC-OPP-JED-.####"); break;
		case "asheer@maasconsult.co":  frm.set_value("naming_series", "MFC-OPP-ALK-.####"); break;
		case "baseeth@maasconsult.co":  frm.set_value("naming_series", "MFC-OPP-RUH-.####"); break;
		case "islam@maasconsult.co":  frm.set_value("naming_series", "MFC-OPP-MED-.####"); break;
		case "zuhayr@maasconsult.co":  frm.set_value("naming_series", "MFC-OPP-DMM-.####"); break;
		case "naveeduddin@maasconsult.co":  frm.set_value("naming_series", "MFC-OPP-OFMC-.####"); break;
		case "alam@maasconsultancy.com": frm.set_value("naming_series", "MFC-OPP-JUB-.####"); break;
	}
}