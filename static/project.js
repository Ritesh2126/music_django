$(document).ready(function () {
    $.getJSON('http://127.0.0.1:8000/categorydisplayjson/',{ajax:True},function(data) {
     alert(data)
       $.each(data,function(index,item){
         //alert(item)
         $('#cid').append($('<option>').text(item[1]))
        })
    })

})
