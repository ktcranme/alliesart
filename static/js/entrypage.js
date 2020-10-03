function init(){
	fetch('/get-images/')
	.then(res => {
		return res.json();
	}).then(data => {
		console.log(data);
		create_images(data);
	}).catch((err) => {
		console.log("Error fetching the tournamentSearch API: "+err)
	});
}

function create_images(files){
	var images_str = ""

	for(var i = 0; i < files.length; i++)
	{
		images_str += "<img class='center' src='"+files[i]+"' alt='...'><br>";
	}

	
	$('#images_div').html(images_str);
}

function Upload_Submitted(){
	console.log($('#upld_code1').val());

	var fd = new FormData();
	fd.append('upload_code1', $('#upld_code1').val());
	fd.append('upload_cose2', $('#upld_code2').val());
	fd.append('img_file', document.getElementById('FileInputControl').files[0])


	fetch('/post-image/', {
		method: 'POST',
		body: fd
	})
	.then(res => {
		return res.json();
	}).then(data => {
		console.log(data);
		if(data == "Success")
		{
			location.reload();
		}
		else
		{
			$('#response').html("Nope");
			$('#response').css("color","FireBrick");
			$('#response').show();
		}
	}).catch((err) => {
		console.log("Error fetching the tournamentSearch API: "+err)
	});
}