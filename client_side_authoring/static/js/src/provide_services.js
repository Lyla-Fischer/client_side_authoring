function evalInContext(js, context) {
    return function() { return eval(js); }.call(context);
}
function ProvideServices(runtime, element) {
    var services = {"save_handler_url" : runtime.handlerUrl(element, 'save_student_data'),
    				"get_data_handler_url" : runtime.handlerUrl(element, 'get_student_data')}
	// TODO: make this cleaner. authored_javascript is defined in client_side_authoring.py with string manipulation while using add_javascript
    evalInContext(authored_javascript, services);
}
