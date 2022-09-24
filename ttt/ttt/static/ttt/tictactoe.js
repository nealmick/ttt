


console.log('tictactoe')


let x = 3;
let y = 3;

let winner = '_'
let board = [];

let state = 1

board =createBoard(board,x,y)


console.log(board)




    

printBoard()


function restart(){
  location.reload();

}




function getMove(board){
    let fasdf = prepareSend(board)
    state=2
    $.ajax(
      {
          type:"GET",
          url: "/tictactoe/ttt/move/",
          
          dataType: 'json',
          data:{
            asdf: String(fasdf),
          },
          success: function(asdf) {
            let res = asdf.asdf
            rw = String(asdf.winner)
  
            
            //console.log('response:',res)
            updateBoard(board,res)
            printBoard()
            updateView(board)
            if(rw=='x' || rw =='o'){
                document.getElementById("winner").innerText = 'winner is: '+rw
                winner = rw
            }
            if(rw=='t'){
                document.getElementById("winner").innerText = 'Tie Game!'
                winner = rw
            }

            state = 1

            //board.move(fasdf[0]+fasdf[1].toUpperCase()+'-'+ fasdf[2]+fasdf[3].toUpperCase() )
            
  
        }
      })

      return winner
  
  }



function updateView(board){
    count=1;
    for(foo=0;foo<x;foo++){
        for(oof=0;oof<y;oof++){
            if(board[foo][oof]!='_'){
                document.getElementById("box"+String(count)).innerText = board[foo][oof]
            }
            count++

        }
    }


}

function updateBoard(board,fasdf){

    let counter = 0;
    for(foo=0;foo<x;foo++){
        for(oof=0;oof<y;oof++){

            if(fasdf[counter]!='_'){
                board[foo][oof]=fasdf[counter]
            }
            counter++
            
        }
    }

    return board
}

function prepareSend(board){
    let sendString = '';

    for(foo=0;foo<x;foo++){
       
        for(oof=0;oof<y;oof++){
            sendString+=board[foo][oof]
        }

    }
    return sendString   


}






function printBoard(){
    let pString = "";
    let bigString ="";
    for(foo=0;foo<x;foo++){
       
        for(oof=0;oof<y;oof++){
            pString+=board[foo][oof]
        }
        bigString+=pString+'\n'
        pString = "";
    }
    //console.log(bigString)
}

function createBoard(board,x,y){
    
    for(foo=0;foo<x;foo++){
        board.push([]);
        for(oof=0;oof<y;oof++){
            board[foo].push('_')
        }
    }
    return board
}


function box1(){
    if (board[0][0]=='_'&& winner=='_'&& state==1){
        document.getElementById("box1").innerText = 'x'
        board[0][0]='x'
        printBoard()
        getMove(board)
    }
}

function box2(){
    if (board[0][1]=='_'&& winner=='_'&& state==1){
      document.getElementById("box2").innerText = 'x'
        board[0][1]='x'
        printBoard()
        getMove(board)
    }
}
function box3(){
    if (board[0][2]=='_'&& winner=='_'&& state==1){
        document.getElementById("box3").innerText = 'x'
        board[0][2]='x'
        printBoard()
        getMove(board)
    }
}
function box4(){
    if (board[1][0]=='_'&& winner=='_'&& state==1){
        document.getElementById("box4").innerText = 'x'
        board[1][0]='x'
        printBoard()
        getMove(board)
    }
}
function box5(){
    if (board[1][1]=='_'&& winner=='_'&& state==1){
        document.getElementById("box5").innerText = 'x'
        board[1][1]='x'
        printBoard()
        getMove(board)
    }
}
function box6(){
    if (board[1][2]=='_'&& winner=='_'&& state==1){

        document.getElementById("box6").innerText = 'x'
        board[1][2]='x'
        printBoard()
        getMove(board)
    }
}
function box7(){
    if (board[2][0]=='_'&& winner=='_'&& state==1){

        document.getElementById("box7").innerText = 'x'
        board[2][0]='x'
        printBoard()
        getMove(board)
    }
}
function box8(){
    if (board[2][1]=='_'&& winner=='_'&& state==1){

        document.getElementById("box8").innerText = 'x'
        board[2][1]='x'
        printBoard()
        getMove(board)
    }
}
function box9(){
    if (board[2][2]=='_'&& winner=='_'&& state==1){
        document.getElementById("box9").innerText = 'x'
        board[2][2]='x'
        printBoard()
        getMove(board)
    }
}

