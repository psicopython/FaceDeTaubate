
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
	
	$("#foto").change(function() {
	  readURL(this);
	});
	
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#img_preview').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}
