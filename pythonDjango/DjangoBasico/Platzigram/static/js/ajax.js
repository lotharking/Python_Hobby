$(document).ready(function(){
    $("#like_heart").on("click",function(e){
        e.preventDefault();
        
        $.ajax({
            type: 'get',
            url: "{% url 'posts:likes2' post.pk %}",
      
            datatype:'json',
            success: function(data){
                      alert(n)
                      console.log(data)
                      console.log(n)
                      },
            error: console.log("SSS"),
      
          }); 

        // $ajax({
        //     url: $(this).attr('href'),
        //     type: $(this).attr('method'),
        //     data: $(this).serializer(),

        //     success: function(jason){
        //         console.log(json)
        //     }
        // })
    })
})