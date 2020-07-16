window.onload = function(){
    console.log('DOM loaded');
    $('.btn_restore').on('click', function(event){
        event.preventDefault();
        console.log(event);
        $.ajax({
           type: "POST",
           url: event.target.pathname,
           data :{
                'csrfmiddlewaretoken' : csrf_token,
           },
           success: function(data) {
                 console.log(data);
                 $('.btn_from_'+data.pk).removeClass('no_display');
                 $('.btn_to_'+data.pk).addClass('no_display');
                 $('.item_'+data.pk).removeClass('no_active');
           }
         });
    })
    $('.pr_del').on('click', function(event){
        event.preventDefault();
        console.log(event);
        $.ajax({
           type: "POST",
           url: event.target.pathname,
           data :{
                'csrfmiddlewaretoken' : csrf_token,
           },
           success: function(data) {
                 console.log(data);
                 $('.btn_from_'+data.pk).addClass('no_display');
                 $('.btn_to_'+data.pk).removeClass('no_display');
                 $('.item_'+data.pk).addClass('no_active');
           }
         });
    })
}
