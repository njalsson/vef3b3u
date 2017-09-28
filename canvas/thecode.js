
let canvas = document.getElementById('thecanvas');
let ctx = canvas.getContext("2D");

ctx.beginPath();
ctx.rect(20, 40, 50, 50);
ctx.fillStyle = "#FF0000";
ctx.fill();
ctx.closePath();
