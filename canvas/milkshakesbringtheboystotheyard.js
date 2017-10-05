let width  = 600;
let height = 600;
let runner = document.getElementById("blade");
let boxcontext = runner.getContext("2d");

//create paddle
paddle = {
	height: 10,
	width : 80,
	x     : width / 2 - 40,
	y     : height - 100
};
//gameloop

boxcontext.rect(paddle.x,paddle.y,paddle.width,paddle.height);
boxcontext.stroke();
