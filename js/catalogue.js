$( document ).ready(function() {

    $('#all').click(function(event){
        $('.cat').removeClass('active');
        $(this).addClass('active');
        getItems("All");
    });
    
    $('#home').click(function(event){
        $('.cat').removeClass('active');
        $(this).addClass('active');
        getItems("Home");

    });
    
     $('#apparel').click(function(event){
        $('.cat').removeClass('active');
        $(this).addClass('active');
        getItems("Apparel");
    });
    
    $('#health').click(function(event){
        $('.cat').removeClass('active');
        $(this).addClass('active');
        getItems("Health");
    });
    
    $('.search').click(function(event){
        searchItems($('.keyword').val());
    })

});

function getItems(category){
    $.getJSON("http://localhost:1234/getAll/"+category,function(str){
        //var obj = $.parseJSON(str);
        var pos = str.lastIndexOf(',');
        str = str.substring(0,pos) + str.substring(pos+1);
        var obj = $.parseJSON(str);
        displayItems(obj);
    });
}

function searchItems(keywords){
    $.getJSON("http://localhost:1234/search/"+keywords,function(str){
        var pos = str.lastIndexOf(',');
        str = str.substring(0,pos) + str.substring(pos+1);
        var obj = $.parseJSON(str);
        displayItems(obj);
    });
}

function displayItems(obj){

var containerStr = "";
var imageStr = "";
var dataStr = "";
 $.each(obj, function(key, value){
        imageStr="";
        dataStr="";
        containerStr += '<div class="col-sm-6 col-md-5"><div class="thumbnail"><div class="caption">';
$.each(value,function(key,value){
                if(key=="imageLink"){
                    imageStr+='<img src="'+value+'" width="300px" height="200px" float="left" /> <br />';
                }
                if(key!="_id" && key!="imageLink"){
                    dataStr += key + " : " + value + "<br />"            
                }
            });
        containerStr += imageStr + dataStr + "</div></div></div>"
 });
 $('#main').html(containerStr);       
}
    