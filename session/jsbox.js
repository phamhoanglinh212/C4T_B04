function myFunction() {
    var elmnt = document.getElementById("box");
    var heightBox = "Height including padding: " + elmnt.clientHeight + "px";
    var widthBox = "Width including padding: " + elmnt.clientWidth + "px";
    console.log(heightBox);
    console.log(widthBox);
}
myFunction();