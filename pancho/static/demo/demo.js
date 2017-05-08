$(document).ready(function() {
	$('#color-changer').find('a').on('click', function(e) {
		e.preventDefault();

		$('#css').attr('href', 'css/' + $(this).attr('class') + '.css');
	});
});