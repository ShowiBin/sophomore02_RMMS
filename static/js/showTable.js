
// insertB = $('.insertBlock')
// insertB.slideUp()//hide the block first
locStr = (location.href)

locStr = decodeURI(locStr)
paras = locStr.split('?')[1]

obj = locStr.split('=')[1]
$('.inserBlock').hide()

let times = 0
function insert(obj){
    // `data inserting block`
    insertB = $('.inserBlock')
    insertB.hide()
    // $('body').append(singUpHtml.responseText)
    url = '/getCols?obj='+obj
    console.log(times)
    if (times !== 0 ) {
        insertB = $('.inserBlock')

        insertB.slideDown()
    }
    if (times === 0){//动态请求
        times=1
        $.post(url).done(function (data) {
            console.log(data)
            data = eval(data)
            console.log(data)
            insertFrom = $('#lalala')
            elem = ''

            console.log(data[0].toString())
            for(let i = 0 ; i < data.length;i++){
                elem=elem+data[i].toString()+":<textarea id = 'input"+i+"' style='right:0%'></textarea><br>"
            }
            console.log(elem)
            insertFrom.append(elem)
            times+=1
            insertB = $('.inserBlock')

            insertB.slideDown()

            })
    }
}



$('#hideInsertB').click(function () {
    $('.inserBlock').slideUp()
})


//给搜索按钮写函数=============================
function selectData() {
    cond = $('#cond').val()
    cond = "'" + cond + "'"//2020/7/9
    // cond = cond.split('&')[0]
    obj = obj.split('&')[0]
    console.log(cond)
    if(cond == '' ){
        alert('请正确输入')
    }
    else{
        // function turn(target) {
        attr4search = $('#attr4Sear').val()
        cond = attr4search + '=' + cond
        url = '/showTable?obj='+obj+'&cond='+cond
        console.log(url)
        $(location).prop('href',url)
    }

}

$('#searchBtn').click(selectData)


//=============================


//add function on submit insert button============================
function insertData() {
    obj = obj.split('&')[0]
    console.log(obj)
    let dataForinput=''
    if(obj == 'Good'){
        for(let i = 0 ; i < 14 ; i++){
            dataForinput+=("'"+$('#input'+i.toString()).val()+"'"+';')//2020/7/9
            console.log(dataForinput)
        }
        // dataForinput+=$('')
        insertOp()
    }
    else{
        url = '/getCols?obj='+obj.split('&')[0]
        // console.log(times)

        $.post(url).done(function (data_) {
            var lengthofdata = eval(data_).length
            // console.log(data_.length)
            for(let i = 0 ; i < lengthofdata ; i++){
                dataForinput+=("'"+$('#input'+i.toString()).val()+"'"+';')//2020/7/9
            }
            console.log(dataForinput)
            insertOp()
        })
    }
    function insertOp() {
        url = '/insertData?obj=' + obj + '&data="' + dataForinput + '"'
        $.post(url).done(function (data) {
            console.log(data)
            if (data == 1) {
                console.log('isOk')
                alert('成功！')
                for (let i = 0; i < 14; i++) {
                    $('#input' + i.toString()).val('')
                }
                    window.location.reload()
            } else {
                alert('数据插入失败，请检查数据是否正确。')
            }
        })

    }

    // console.log($('#input1').val())
    // $('.inserBlock').children().each(function () {
    //     console.log('1')
    //     console.log($(this).text())
    // })
}
$('#submit').click(insertData)
//===============================================================




//删除按钮==============================
function sureDelData(sureDel,condition) {
    if(sureDel){
        url = '/delData?obj='+obj.split('&')[0]+'&cond='+condition
        $.post(url).done(function (res) {
            console.log(res)
            if (res == '1'){
                console.log('isOk')
                // alert('数据删除成功！')
                // for(let i = 0 ; i < 14 ; i++){
                //     $('#input'+i.toString()).val('')
                        // }
            }
            else {
                alert('数据删除失败，请联系开发者：2787913282@qq.com。')
            }
        })

    }
    else {
        console.log('user end an operation')
    }
}
function del(condition) {
    sureDel = confirm('确定删除满足条件：'+condition+'的数据')
    sureDelData(sureDel,condition)
    if(sureDel)
    {window.location.reload()}
    // window.location.reload()


}
//===============================================================



//========修改函数
function update(updateCond) {
    var ifUpdate = confirm('请仔细确认是否修改，修改不可逆！')
    if (ifUpdate){

        // `data inserting block`
        // insertB = $('.inserBlock')
        // insertB.hide()
        // $('body').append(singUpHtml.responseText)
        url = '/getCols?obj='+obj.split('&')[0]+'&data=True&cond='+updateCond
        console.log(updateCond)
        if (times !== 0 ) {
            $.post(url).done(function (data) {
                // console.log(data)
                data = eval(data)
                console.log(data)
                info = data[1][0]
                data = data[0]
                insertFrom = $('#lalala')
                // elem = ''
                console.log(info)
                // console.log(data[0].toString())
                // for(let i = 0 ; i < data.length;i++){
                //     elem=elem+data[i].toString()+":<textarea id = 'input"+i+"' style='right:0%'></textarea><br>"
                // }
                for(let i = 0 ; i < info.length;i++){
                    $('#input'+i).val(info[i])
                }
                // console.log(elem)
                // insertFrom.append(elem)
                times+=1
                insertB = $('.inserBlock')

                insertB.slideDown()
                addData(data,info)

                })
        }
        if (times === 0){
            times=1
            $.post(url).done(function (data) {
                console.log(data)
                console.log(data)

                data = eval(data)
                // console.log(data)
                info = data[1][0]
                data = data[0]
                console.log('data:',data)
                console.log('info:',info)

                insertFrom = $('#lalala')
                elem = ''

                // console.log(data[0].toString())
                for(let i = 0 ; i < data.length;i++){
                    elem=elem+data[i].toString()+":<textarea id = 'input"+i+"' style='right:0%'></textarea><br>"
                }

                // console.log(elem)
                insertFrom.append(elem)
                times+=1
                insertB = $('.inserBlock')

                insertB.slideDown()
                addData(data,info)
                })

        }
        function addData(data,info){
            for(i = 0 ; i < data.length;i++){
                    $('#input'+i).val(info[i])
                }
        }




        sureDelData(ifUpdate,updateCond)
    }
}



//====================
//======================完善统计数据
// // if($('#tonji').text() !== '0') {
//     $('#tonji').text((eval($('#tonji').text()) + 1).toString())
// // }