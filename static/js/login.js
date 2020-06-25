function addSingUp() {
    console.log('lll')
    singUpHtml = $.get('/signup').done(function () {
        console.log(typeof singUpHtml.responseText)
        console.log(singUpHtml.responseText)
        signB = $('#singUpBlock')
        signB.hide()
        $('#content').append(singUpHtml.responseText)
        signB.slideDown()
    })
}

function checkAndLogin() {
    username = $('#username').val()
    pwd = $('#pwdContent').val()
    console.log(username)
    console.log(pwd)
    if(username.length < 4 ||pwd.length < 4){
        alert('giao?')
    }
    else {
        url = '/serverLogin?username="'+username+'"&pwd="'+pwd+'"'
        $.post(url).done(function (data) {
            console.log(data)
            data = eval(data)
            data = data[0]
            console.log(data['isOk'])
            if (data['isOk'] == 1){
                console.log('isOk')
                $(location).prop('href','/home?nickname="'+data["nickname"]+'"')
            }
            else {
                alert('Username or password is wrong,try it again!')
                $('#pwdContent').val('')
            }
        })
    }
}


ad_Timer = 0
setInterval(function () {
    // if(ad_Timer%2 == 0){
    //     $('#homeWelcome').hide();
    // }
    // else {
    //     $('#homeWelcome').show();
    // }
    // ad_Timer++;
},500)



//main

$('#singUpBtn').click(addSingUp)

$('#loginBtn').click(checkAndLogin)

