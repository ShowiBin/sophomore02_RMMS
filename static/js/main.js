
function getToBlogs(){
	try{
		if(nickname){
			hr = '/blogs?nickname="'+nickname+'"'
		}
		else {
			hr = '/login'
		}
	}
	catch (e) {
		hr = '/login'
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
	console.log(obj)
	b_data = eval(obj)
	for(i in b_data){
		var cont = '<tr>\n' +
					'<td><a href="/sorry" class="link">'+b_data[i][2].slice(0,40)+'...'+'</a></td>\n' +
			'</tr>'
		$('#firstBlog').after(cont)

	}
	// $('#firstBlog').after("lalala")
	// 		return eval(obj)
}









function  get_events_data(){
			url = '/server?dataName="events"'
			$.post(url).done(set_events_data)
}

function set_events_data(obj) {
	console.log(obj)
	b_data = eval(obj)
	for(i in b_data){
		var cont = '<tr>\n' +
					'<td><a href="/sorry" class="link">'+b_data[i][2].slice(0,40)+'...'+'</a></td>\n' +
			'</tr>'
		$('#firstevents').after(cont)

	}

}

get_events_data()

//main
get_blogs_data()



locStr = (location.href)

locStr = decodeURI(locStr)
paras = locStr.split('?')[1]
console.log(paras)
if (paras){
	nickname = paras.split('=')[1]
	console.log(nickname)
	// nickname = nickname.replace('%22','').replace('%22','')

	console.log(nickname)
	//hide login btn
	$('#loginIcon').attr('href','/userPage')
	console.log('nickname02:'+nickname)
	$('#loginIcon').text(nickname)
	$('#blogs_href').attr('href','/blogs'+'?nickname='+nickname)
	//
	// userLink = `
	// 				<li><a href="/userPage" id="userHead">`+nickname+`</a></li>
	// `
	// $('#sb').after(userLink)
	// $('#loginIcon').hide()


}




//
// //fo home iamges
// $('#img1').hide()
// $('#img2').hide()
// $('#img3').hide()
// // $('#img4').hide()
//
// nowImg = 'img4'
//
// setInterval(showImg,4000)
// function showImg(){
// 	if (nowImg == 'img1'){
// 		$('#img1').slideUp()
// 		$('#img2').slideDown()
// 		nowImg = 'img2'
// 	}
// 	else if (nowImg == 'img2'){
// 		$('#img2').slideUp()
// 		$('#img3').slideDown()
// 		nowImg = 'img3'
// 	}
// 	else if (nowImg == 'img3'){
// 		$('#img3').slideUp()
// 		$('#img4').slideDown()
// 		nowImg = 'img4'
// 	}
// 	else if (nowImg == 'img4'){
// 		$('#img4').slideUp()
// 		$('#img1').slideDown()
// 		nowImg = 'img1'
// 	}
// }


//定义变量获取屏幕视口宽度
var windowWidth = $(window).width();
if(windowWidth < 640){
	// do something
	$('.navImg').hide()
}
if(windowWidth >= 640){
	// do something
	$('.navImg_mobile').hide()
}


