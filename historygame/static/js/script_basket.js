window.onload = function(){
    console.log('DOM loaded');
    $('.basket_list').on('change', 'input[type=number]', function(event){
        $.ajax({
            url:'/basket/change/'+event.target.name + '/on/' + event.target.value + '/product/quantity/',
            success: function(data) {
                $('.purchase_amount').html(data.purchase_amount);
                let str_ = '.product_cost_pk_'+String(data.pk);
                $(str_).html(data.product_cost);
                console.log(event.target.value)
                if (event.target.value == "0") {
                    $('.item_'+String(data.pk)).remove();
                }
            }
        })
    })
}