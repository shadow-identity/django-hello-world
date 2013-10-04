/*<![CDATA[*/
jQuery(document).ready(function () {
    var options = {
        target: "#ajaxwrapper",
        beforeSubmit: maskForm,
        success: unMaskForm
    };
    jQuery('#contactform').ajaxForm(options)
});


var maskForm = function () {
    jQuery("#maskwrapper").mask("Saving...")
};
var unMaskForm = function () {
    jQuery("#maskwrapper").unmask()
};
/*]]>*/