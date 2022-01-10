$(document).ready(function(){
    // ajax for call in post
    $(".like-link").on("click",function(e){
        var id = $(this).data("id");
  
        $.ajax({
          url: $(this).data("url"),
          data: {
            'pk': id
          },
          dataType: 'json',
          success: function (data) {
            if (data['like']) {
                $('.like-toggle[data-id=' + id + ']').removeClass("far fa-heart").addClass("fas fa-heart");
            }
            else {
                $('.like-toggle[data-id=' + id + ']').removeClass("fas fa-heart").addClass("far fa-heart");
            }
            var body = '<i id="value_like">' + data['value'] +'</i>'
            $('.like-count[data-id=' + id + ']').html(body);
          }
        });
    })
})