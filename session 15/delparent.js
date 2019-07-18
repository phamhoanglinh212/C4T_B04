var deleteButs = document.getElementsByClassName('del');
for (var i = 0; i < deleteButs.length; i++) {
    var deleteBut = deleteButs[i];
    deleteBut.addEventListener('click', function(e){
        var del = e.target;
        var parent = del.parentNode;
        parent.remove();
    });
}