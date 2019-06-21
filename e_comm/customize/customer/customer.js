console.log("********************* JS file Called****************************")
frappe.ui.form.on('Customer', {
	refresh: function(frm) {
    console.log("********************* On refresh ****************************")

	},
  onload: function(frm){
    //console.log("====================== onload ===============");
  },

  validate: function(frm){
    console.log("++++++++++++  validation called in js+++++++++++++")
  }
});
