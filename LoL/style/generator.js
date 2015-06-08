$(document).ready(function(){
        $("#show").click(function(){
          $("#avis").hide();
          $("#show").hide();          
          $("#wait").slideToggle("fast");
          $("#progress").show()
          $.ajax({
            url: "/generar/",
            success: function(response) {
              $("#wait").hide();
              $("#progress").hide();
              $("#created").slideToggle("fast");
            },
          });
        });
      });
