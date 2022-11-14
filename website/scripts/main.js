function makeBoard(){
    //Creates a board div, places SVG inside and adds to main container, binds event listeners
    var mainContainer = document.getElementById("mainContainer");
    var board = document.createElement("img");
    board.src = "img/boardVector.svg";
    board.id = "board";
    board.className = "board";
    board.addEventListener("click", placeRing);
    board.addEventListener("mousemove", hoverRing);
    board.addEventListener("mouseleave", removetempRing);
    mainContainer.appendChild(board);
}

function placeRing(){
    //Places a ring on the board by taking the x and y coordinates of the click event

    //To do: Implemet ring snapping onto nearest node
    var board = document.getElementById("board");
    var offsetX = board.offsetLeft;
    var offsetY = board.offsetTop;
    var x = event.pageX - offsetX;
    var y = event.pageY - offsetY;
    console.log(x + " " + y);
    var ring = document.createElement("div");
    ring.id = "permanent"
    ring.addEventListener('mousemove', hoverRing);
    //Need this to stop animation breaking when mouse moves over already placed ring
    ring.className = "ring";
    ring.style.position = "absolute";
    var closestX = closestVertical(x);
    var closestY = closestHorizontal(y);
    console.log(closestX + " " + closestY);
    ring.style.left = (closestX + offsetX - 34)+ "px";
    ring.style.top = (closestY + offsetY - 34) + "px";
    mainContainer.appendChild(ring);
}

function hoverRing(){
    //Places a temporary ring on the board by taking the current x and y coordinates of the mouse while it is moving inside the board div
    removetempRing();
    var board = document.getElementById("board");
    var offsetX = board.offsetLeft;
    var offsetY = board.offsetTop;
    var x = event.pageX - offsetX;
    var y = event.pageY - offsetY;
    var ring = document.createElement("div");
    ring.id = "temporary"
    ring.className = "ring";
    ring.addEventListener("click", placeRing);
    //Must bind placeRing listener to the temporary ring so you can still place a ring when hovering over the temporary one.
    ring.style.position = "absolute";
    var closestX = closestVertical(x);
    var closestY = closestHorizontal(y);
    ring.style.left = (closestX + offsetX - 34)+ "px";
    ring.style.top = (closestY + offsetY - 34) + "px";
    mainContainer.appendChild(ring);
}

function removetempRing(){
    //Removes the temporary ring when the mouse leaves the board div and also runs at the start of the hoverRing function
    var oldRing = document.getElementById("temporary");
    if(oldRing != null){
        oldRing.remove();
    }
}

function closestVertical(x){
    //Returns the closest vertical node to the x coordinate of the mouse
    var nodes = [46, 104, 162, 220, 278, 336, 395, 453, 510, 569, 627];
    var closest = nodes.reduce(function(prev, curr) {
        return (Math.abs(curr - x) < Math.abs(prev - x) ? curr : prev);
    });
    return closest;
}

function closestHorizontal(y){
    //Returns the closest horizontal node to the y coordinate of the mouse
    var nodes = [36, 68, 101, 135, 168, 202, 236, 269, 303, 337, 370, 403, 437, 470, 504, 538, 572, 605, 639];
    var closest = nodes.reduce(function(prev, curr) {
        return (Math.abs(curr - y) < Math.abs(prev - y) ? curr : prev);
    });
    return closest;
}

window.onload = makeBoard;

