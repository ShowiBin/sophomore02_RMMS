

function checkSignUp(){
    console.log('777')
    username = $('#username').val()
    pwd = $('#pwd').val()
    name = $('#name').val()
    age = $('#age').val()

    console.log(username)
    console.log(pwd)
    console.log(name)
    console.log(age)
    if (check(username)&&check(pwd)){
        if(name == '' || age == '' || age < 0|| age > 150){
            alert('U data get sth wrong!Check it!!')
        }
        else {

            url = '/serverSignUp?username="'+username+'"&pwd="'+
                pwd+'"&name="'+name+'"&age="'+age+'"'
            $.post(url).done(function (nickname) {
                console.log(nickname)
                if (nickname.toString() == '0'||nickname == undefined){
                    alert('Server Error!')
                }
                else {
                    alert('Welcome to BiaoYanBu_Home')
                    $(location).prop('href','/home?nickname='+nickname)
                }
            })
        }

    }
    else{
        alert('U data get sth wrong!Check it!!')
    }
}

function check(data){
    if (!data){
        return false
    }
    len = data.length
    if(len == 0||len>20){
        return false
    }
    else {
        return true
    }
}