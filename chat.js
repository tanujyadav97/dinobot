$(document).ready(function(){

    $('button').click(function() {
      
       var mess=document.getElementById("message").value;
       $("#chatlist").append('<li class="type2">'+mess+'</li>');

       $.ajax({
            type: "POST",
            url: "http://localhost:8080/dinobot/python_files/addmess.php",
            data: { message: mess }
              }).done(function( msg ) {
                    //alert( "Data Saved: " + msg );

                    $("#chatlist").append('<li class="type1">'+msg+'</li>');
                });    

     });

});    