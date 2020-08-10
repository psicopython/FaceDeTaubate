
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
});