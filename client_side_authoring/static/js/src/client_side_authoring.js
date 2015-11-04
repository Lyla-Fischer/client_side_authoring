/* Javascript for ClientSideAuthoringXBlock. */
function ClientSideAuthoringXBlock(runtime, element) {

    var handlerUrl = runtime.handlerUrl(element, 'save_authoring');

    var updatePreview = function(data){
            $('textarea[name=html]').text(data.html);
            $('textarea[name=css]').text(data.css);
            $('textarea[name=javascript]').text(data.javascript);
            console.log(data);
    };

    // process the form
    $('form').submit(function(event) {
        var formData = {
            'html'              : $('textarea[name=html]').val(),
            'css'               : $('textarea[name=css]').val(),
            'javascript'        : $('textarea[name=javascript]').val()
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

    var javascript_textarea = CodeMirror.fromTextArea($('textarea[name=javascript]').get(0), {
        mode:  "javascript",
        lineNumbers: true
      });
    console.log(javascript_textarea)

    var css_textarea = CodeMirror.fromTextArea($('textarea[name=css]').get(0), {
        mode:  "css",
        lineNumbers: true
      });
    console.log(css_textarea)
    
    var html_textarea = CodeMirror.fromTextArea($('textarea[name=html]').get(0), {
        mode:  "xml",
        lineNumbers: true
      });
    console.log(html_textarea)


}
