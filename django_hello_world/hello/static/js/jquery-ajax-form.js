/*<![CDATA[*/
jQuery(document).ready(function() {
    var options = {
        target: "#ajaxwrapper",
        beforeSubmit: maskForm,
        success: unMaskForm
    }
    jQuery("#contactform").submit(function(e){
        jQuery(this).ajaxSubmit(options);
        return false;
        e.preventDefault();
    })
});
function maskForm() {
    jQuery("#ajaxwrapper").mask("Saving...")
}
function unMaskForm() {
    jQuery("#ajaxwrapper").unmask()
}
/*]]>*/