/*<![CDATA[*/
jQuery(document).ready(function() {
    var options = {
        target: "#ajaxwrapper",
        beforeSubmit: maskForm,
        success: unMaskForm
    }
    jQuery('#contactform').ajaxForm(options)
})


function maskForm() {
    jQuery("#maskwrapper").mask("Saving...")
}
function unMaskForm() {
    jQuery("#maskwrapper").unmask()
};
/*]]>*/