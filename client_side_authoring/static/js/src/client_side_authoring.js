function ClientSideAuthoringXBlock(runtime, element) {

    var javascript_textarea = CodeMirror.fromTextArea($('textarea[name=javascript]', element).get(0), {
        mode:  "javascript",
        lineNumbers: true
      });

    var css_textarea = CodeMirror.fromTextArea($('textarea[name=css]', element).get(0), {
        mode:  "css",
        lineNumbers: true
      });
    
    var html_textarea = CodeMirror.fromTextArea($('textarea[name=html]', element).get(0), {
        mode:  "xml",
        lineNumbers: true
      });

    var handlerUrl = runtime.handlerUrl(element, 'save_authoring');

    var updatePreview = function(data){
            $('.html_editor').val(data.html);
            $('.css_editor').val(data.css);
            $('.javascript_editor').val(data.javascript);
            console.log(data);
    };

    $('form').submit(function(event) {
        var formData = {
            'html'              : $('.html_editor', element).val(),
            'css'               : $('.css_editor', element).val(),
            'javascript'        : $('.javascript_editor', element).val()
        };

        $.ajax({
            type        : 'POST', 
            url         : handlerUrl, 
            data        : JSON.stringify(formData), 
            dataType    : 'json', 
            encode      : true,
            success     : updatePreview
        });
        // stop the form from submitting the normal way and refreshing the page
        event.preventDefault();
    });
}
