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
    ring.style.left = (x + offsetX)+ "px";
    ring.style.top = (y + offsetY) + "px";
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
    ring.style.left = (x + offsetX)+ "px";
    ring.style.top = (y + offsetY) + "px";
    mainContainer.appendChild(ring);
}

function removetempRing(){
    //Removes the temporary ring when the mouse leaves the board div and also runs at the start of the hoverRing function
    var oldRing = document.getElementById("temporary");
    if(oldRing != null){
        oldRing.remove();
    }
}

window.onload = makeBoard;

