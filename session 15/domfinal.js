// var find = document.getElementById('song_container');
// console.log(find);
// var find1 = document.getElementsByClassName('song');
// console.log(find1);
// var title = document.getElementsByClassName('title');
// var artist = document.getElementsByClassName('artist');
// console.log(title);
// console.log(artist);
var delbuttons = document.getElementsByClassName('del');
for ( var i = 0; i < delbuttons.length; i++ ){
    var delbutton = delbuttons[i];
    delbutton.addEventListener('click', function(e){
        var del = e.target;
        var parent = del.parentNode;
        parent.remove();
    });
}
var edit = document.getElementsByClassName('edit');
for ( var i = 0; i < edit.length; i++ ) {
    var editbutton = edit[i];
    editbutton.addEventListener('click', function(f){
        var show = f.target;
        sss= show.parentNode.getAttribute('song_id');
        console.log(sss)
    });
}
var more = document.getElementsByClassName('more');
for ( var i = 0; i < more.length; i++ ) {
    var infor = more[i];
    infor.addEventListener('click', function(o){
        var illustrate = o.target;
        illustrate1 = illustrate.parentNode.getAttribute('song_id');
        // var find1 = document.getElementsByClassName('song');
        var find1 = illustrate.parentNode.getElementsByClassName("more")[0];
        var find2 = illustrate.parentNode.getElementsByClassName("artist")[0];
        var find3 = illustrate.parentNode.parentNode.hasAttribute(illustrate);
        console.log(find1);
        console.log(find2);
        console.log(find3);
        console.log(illustrate1);
    });
}


// var id = document.getElementById('song_container');
// var idd = id.target.getAttribute('song_id');
// console.log(idd) 


