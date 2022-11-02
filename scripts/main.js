function makeBoard(){
    var mainContainer = document.getElementById("mainContainer");
    var board = document.createElement("img");
    board.src = "img/boardVector.svg";
    board.id = "board";
    board.className = "board";
    board.addEventListener("click", mousePosition);
    mainContainer.appendChild(board);
}

function mousePosition(){
    var board = document.getElementById("board");
    var offsetX = board.offsetLeft;
    var offsetY = board.offsetTop;
    var x = event.pageX - offsetX;
    var y = event.pageY - offsetY;; 
    console.log(x + " " + y);
    var marker = document.createElement("div");
    marker.style.position = "absolute";
    marker.style.left = (x + offsetX)+ "px";
    marker.style.top = (y + offsetY) + "px";
    marker.style.width = "10px";
    marker.style.height = "10px";
    marker.style.backgroundColor = "red";
    mainContainer.appendChild(marker);
}



window.onload = makeBoard;

