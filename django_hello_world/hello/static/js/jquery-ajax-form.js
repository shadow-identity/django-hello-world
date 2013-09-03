/*<![CDATA[*/
jQuery(function() {
      var form = jQuery("#contactform");
      form.submit(function(e) {
          jQuery("#mask").mask("Saving...")
          jQuery("#sendwrapper").prepend('<span>Sending message, please wait... </span></br>')
          jQuery("#ajaxwrapper").load(
              form.attr('action') + ' #ajaxwrapper',
              form.serializeArray(),
              function(responseText, responseStatus) {
                  jQuery("#mask").unmask()
              }
          );
          e.preventDefault();
      });
  });
/*]]>*/