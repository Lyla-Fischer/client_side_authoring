/* Javascript for ClientSideAuthoringXBlock. */
function ClientSideAuthoringXBlock(runtime, element) {

    var handlerUrl = runtime.handlerUrl(element, 'save_authoring');

    var updatePreview = function(data){
            console.log(data); 
    };

    // process the form
    $('form').submit(function(event) {
        var formData = {
            'html'              : $('textarea[name=html]').val(),
            'css'               : $('textarea[name=css]').val(),
            'javascript'        : $('textarea[name=javascript]').val()
        };

        console.log(formData);

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

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });


}
