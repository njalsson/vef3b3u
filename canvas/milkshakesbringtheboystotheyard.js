let canvas   = document.getElementById("blade");
let ctx      = canvas.getContext("2d");
let phonenumber = "";


arrayOfBalls      = [];
arrayOfSmallBalls = [];
// make ten rings at the top and have a ball 
//at the bottom that sends a ball to the top and
//clicks one of the balls, number of the ball gets 
//added to a phone number
console.log('oeu')
//class constructor to create the ball.
class balls {
    constructor(radius,x,y){
        this.radius = radius;
        this.x      = x;
        this.y      = y;
    }

    static distance(a,b){
        const dx = a.x - b.x;
        const dy = a.y - b.y;

        return Math.hypot(dx,dy);
    }
}
//creating the balls and adding them to an array.
for (let i = 0; i < 10; i++) {
    let ball = new balls(25,30 + 60 * i,30);
    arrayOfBalls.push(ball)
}
//the ball at the bottom
bottomBitch = new balls(50,300,540);
//main function
setInterval(function draw(){
    if (arrayOfSmallBalls.length>0) {
        //console.log(balls.distance(arrayOfSmallBalls[0],arrayOfBalls[4]))
    }
    ctx.clearRect(0, 0, 800, 800);
    DrawTopBalls();
    drawBottombitch();
    checkifkeyispressed();
    drawsmallguys();
    update();
    collision();
    //todo this
    //draw the array of balls
},100);



function collision(){
    for(let i = 0; i < arrayOfSmallBalls.length; i++){
        for(let j = 0; j < arrayOfBalls.lenght; j++){
            if (balls.distance(arrayOfSmallBalls[i],arrayOfBalls[j]) <= 40) {
                phonenumber += i+1;
                arrayOfSmallBalls.splice(i, 1);
                console.log("that hit something");

            }
        }
    }
}
function drawsmallguys(){
    for(let i = 0; i < arrayOfSmallBalls.length;i++){
        ctx.beginPath();
        ctx.arc(arrayOfSmallBalls[i].x,arrayOfSmallBalls[i].y,arrayOfSmallBalls[i].radius,0,2*Math.PI);
        ctx.stroke();

    }
}
//check if spacebar is pressed, if so, 
//it will create a small ball that goes up 
//and hits a target;
function update(){
    for(let i = 0; i < arrayOfSmallBalls.length; i++){
        arrayOfSmallBalls[i].y-=5;
    }
}
function checkifkeyispressed(){
    document.body.onkeyup = function(e){
        if(e.keyCode == 32){
            let temp = new balls(15,bottomBitch.x,bottomBitch.y);
            arrayOfSmallBalls.push(temp);
        }
        if(e.keyCode == 65 || e.keyCode == 97){
            bottomBitch.x -= 10;
        }
        if(e.keyCode == 68 || e.keyCode == 100){
            bottomBitch.x += 10
        }
    }


}

function drawBottombitch(){
    ctx.beginPath();
    ctx.arc(bottomBitch.x,bottomBitch.y,bottomBitch.radius,0,2*Math.PI);
    ctx.stroke();

}

function DrawTopBalls(){
    for(let i = 0; i < arrayOfBalls.length; i++){
        ctx.beginPath();
        ctx.arc(arrayOfBalls[i].x,arrayOfBalls[i].y,arrayOfBalls[i].radius,0,2*Math.PI);
        ctx.stroke();

    }

}