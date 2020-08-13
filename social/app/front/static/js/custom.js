
$(document).ready(function(){
	$('.btn-senha').click(function(){
		if($('.senha').attr('type') == 'password'){
			$('.senha').attr('type','text')
			$('.lab-senha').html('Ocultar Senha')
		}else{
			$('.senha').attr('type','password')
			$('.lab-senha').html('Mostrar Senha')
		}
	});
	$("#new_img").change(function() {
	  carregar_foto_perfil(this);
	});
    var imagesPreview = function(input, local) {
		$(local).empty()
        if (input.files) {
            var filesAmount = input.files.length;

            for (i = 0; i < filesAmount; i++) {
                var reader = new FileReader();

                reader.onload = function(event) {
                	var img = '<div class="img_edit_item" ><figure><img src="'+event.target.result+'"></figure></div>'
						
						
                    $(local).append(img).appendTo(local);
                }

                reader.readAsDataURL(input.files[i]);
            }
        }

    };

    $('#input-file').on('change', function() {
        imagesPreview(this, '.img_preview');
    });
	
});


function carregar_foto_perfil(input) {
  if (input.files && input.files[0]) {
  	
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#perfil_img').attr('src', e.target.result);
	  $('#perfil_img_alert').remove()
    }
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
   else {
   	$('#perfil_img').attr('src','/static/img/perfil/user_img.png');
   	$('#perfil_img_label').append('<span id="perfil_img_alert" class="alert alert-warning">Nenhuma foto selecionada,<br> usaremos a imagem padrão!</span>');
	}
   	
   }