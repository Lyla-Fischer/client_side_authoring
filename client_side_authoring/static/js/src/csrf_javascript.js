/**
Add this javascript file to your xblock and the following html to the form element in order to pass back the csrf token to the django middleware

    <div style="display:none">
        <input class="csrf_token_input" type="hidden" name="csrfmiddlewaretoken">
    </div>
    
**/
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $(function ($) {
        var csrftoken = getCookie('csrftoken');
        $(".csrf_token_input").attr('value', csrftoken);
    });