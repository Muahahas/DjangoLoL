<script>
      $(document).ready(function(){
        $("#hide").click(function(){
            $("progress").hide();
        });
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
    </script>