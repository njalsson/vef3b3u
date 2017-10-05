let width  = 600;
let height = 600;
let runner = document.getElementById("blade");
let boxcontext = runner.getContext("2d");
let isthegamerunning = true;
let rightPressed = false;
let leftPressed = false;

//create paddle
paddle = {
	height: 10,
	width : 80,
	x     : width / 2 - 40,
	y     : height - 100
};

document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = true;
    }
    else if(e.keyCode == 37) {
        leftPressed = true;
    }
}
function keyUpHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = false;
    }
    else if(e.keyCode == 37) {
        leftPressed = false;
    }
}
//gameloop
function drawpaddle(){

	boxcontext.beginPath();
	boxcontext.rect(paddle.x,paddle.y,paddle.width,paddle.height);
	boxcontext.fillStyle ="#ffa500";
	boxcontext.fill();
	boxcontext.closePath();
}
function drawball(){
	//..
}
function drawbricks(){
	//..
}
function draw(){
	boxcontext.clearRect(0,0,600,600);
	drawpaddle();

	if(rightPressed && paddle.x < canvas.width-paddle.width) {
        paddle.x += 7;
    }
    else if(leftPressed && paddle.x > 0) {
        paddle.x -= 7;
    }


	//...
}
setInterval(draw(), 10);




