
      $(document).ready(function(){
        $("#show").click(function(){
          $("#show").hide();
          $("progress").show();
          $.ajax({
            url: "/generar/",
            success: function(response) {
              window.location.href = '/succesfulcreated'   
            },
          });
        });
      });
