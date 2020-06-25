function getToBlogs(){
	if(nickname.length > 2){
		$(location).prop('href','/blogs?nickname="'+nickname+'"')
	}
	else {
		$(location).prop('href','/login')
	}
}

$('#menu').click(function (){
	$('#links').toggle(500)
})



function  get_blogs_data(){
			url = '/server?dataName="homeBlogData"'
			$.post(url).done(set_data)
}

function set_data(obj){
	b_data = eval(obj)
	for(i in b_data){
		var cont = '<tr>\n' +
					'<td><a href="'+b_data[i].links+'" class="link">'+b_data[i].content+'</a></td>\n' +
			'</tr>'
		$('#firstBlog').after(cont)

	}
	// $('#firstBlog').after("lalala")
	// 		return eval(obj)
}


locStr = (location.href)
paras = locStr.split('?')[1]
if (paras){
	nickname = paras.split('=')[1]
	nickname = nickname.replace('%22','').replace('%22','')

	console.log(nickname)
	//hide login btn
	$('#loginIcon').attr('href','/userPage')
	$('#loginIcon').text(nickname)
	//
	// userLink = `
	// 				<li><a href="/userPage" id="userHead">`+nickname+`</a></li>
	// `
	// $('#sb').after(userLink)
	// $('#loginIcon').hide()

}
