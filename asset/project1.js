$(document).ready(function (){
    $('#cid').append($('<option>').text('-Select Category-'))

     //$('#btn').click(function(){
     $('#stext').keyup(function(){

    $.getJSON('http://127.0.0.1:8000/searchsongjson/',{ajax:true,pat:$('#stext').val()},function (data) {

        //alert(data)

       htm=""
        htm+="<div class='row'>"






       $.each(data,function(index,item){
         htm+="<div class='col-md-4'>"
		 htm+="<div class='category-item' style='margin:5px;'>"
		 htm+="<img src='/static/"+item[11]+"' >"
		 htm+="<div class='ci-text'>"
		 htm+="	<h4>"+item[3]+"</h4>"
		 htm+="	<p>"+item[8]+"</p>"
		 htm+="</div>"
             htm+="<a href='/playsong?sg="+item+"' class='ci-link'><i class='fa fa-play'></i></a>"
			htm+="</div>"
			htm+="</div>"


       })
        htm+="<div>"
    $('#result').html(htm)

    })


    })


    $.get('http://127.0.0.1:8000/categorydisplayalljson/',{ajax:true},function (data) {

       // alert(data)

       $.each(data,function(index,item){
        //   alert(item)
        $('#cid').append($('<option>').text(item[1]).val(item[0]))


       })


    })





     $('#cid').change(function () {

         $.getJSON('http://127.0.0.1:8000/displaysubcategoryjson/', {
             ajax: true,
             cid: $('#cid').val()
         }, function (data) {

             //alert(data)
             $('#subid').empty()
             $('#subid').append($('<option>').text('-Select SubCategory-'))

             $.each(data, function (index, item) {
                // alert(item)
                 $('#subid').append($('<option>').text(item[2]).val(item[0]))

             })


         })
     })



})
