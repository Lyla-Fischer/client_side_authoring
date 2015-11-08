// function evalInContext(js, context) {
//     //# Return the results of the in-line anonymous function we .call with the passed context
//     return function() { return eval(js); }.call(context);
// }
function ProvideServices(runtime, element) {
    // var services = {save_handler_url: runtime.handlerUrl(element, 'save_html')};
    // console.log("first draft " + save_handler_url);
    var save_handler_url = runtime.handlerUrl(element, 'save_student_data');
    var get_data_handler_url = runtime.handlerUrl(element, 'get_student_data');
    eval(authored_javascript);
    // evalInContext(authored_javascript, services);
}
