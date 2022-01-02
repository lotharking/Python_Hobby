$(document).ready(function(){
    // ajax for call in post
    $("#like_heart").on("click",function(e){
        // e.preventDefault();
        var id = $(this).data("id");
  
        $.ajax({
        //   url: 'posts/likes2/',
          url: $(this).data("url"),
          data: {
            'pk': id
          },
          dataType: 'json',
          success: function (data) {
            if (data['like']) {
                $('#success_like').removeClass("far fa-heart").addClass("fas fa-heart");
            }
            else {
                $('#success_like').removeClass("fas fa-heart").addClass("far fa-heart");
            }
            var body = '<i id="value_like">' + data['value'] +'</i>'
            $('#value_like').html( body );
          }
        });
    })
})