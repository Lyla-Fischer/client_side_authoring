/* Javascript for CustomHtmlXBlock. */
function CustomHtmlXBlock(runtime, element) {
    
    var saveUrl = runtime.handlerUrl(element, 'save_html');

    $('form').attr("action", saveUrl);

    $(function ($) {
        tinymce.init({selector:'textarea'});
    });
}