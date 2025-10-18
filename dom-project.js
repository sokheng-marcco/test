let score = JSON.parse(localStorage.getItem('score')) || {
            wins : 0,
            losses : 0,
            ties : 0
        };
        
    saveScore();
    displayScore();

function displayScore () {
    document.querySelector('.js-score').innerHTML = 
        `Win : ${score.wins}, Lose : ${score.losses}, Tie : ${score.ties}`;
}

function saveScore () {
    localStorage.setItem('score' , JSON.stringify(score));
}

function pickComputerMove () {
    let randomNum = Math.random();
    let computerMove = '';

    if (randomNum <= 1/3) {
        computerMove = 'rock';
    } else if (randomNum > 1/3 && randomNum <= 1/2) {
        computerMove = 'paper';
    } else {
        computerMove = 'scissors';
    }
    return computerMove;
}

function playGame (playerPick) {
    let result = '';
    computerMove = pickComputerMove();

    if (playerPick === 'rock') {
        if (computerMove === 'rock') {
            result = 'Tie!';
        } else if (computerMove === 'paper') {
            result = 'You Lose!';
        } else if (computerMove === 'scissors') {
            result = 'You Win!';
        }
    } else if (playerPick === 'paper') {
        if (computerMove === 'rock') {
            result = 'You Win!';
        } else if (computerMove === 'paper') {
            result = 'Tie!';
        } else if (computerMove === 'scissors') {
            result = 'You Lose!';
        }
    } else if (playerPick === 'scissors') {
        if (computerMove === 'rock') {
            result = 'You Lose!';
        } else if (computerMove === 'paper') {
            result = 'You Win!';
        } else if (computerMove === 'scissors') {
            result = 'Tie!';
        }
    }

    document.querySelector('.js-result').innerHTML = result;
        
    document.querySelector('.js-move').innerHTML =
        `You <img src="rock-paper-scissors-images/${playerPick}-emoji.png" class="move-icon"/> <img src="rock-paper-scissors-images/${computerMove}-emoji.png" class="move-icon"/> Computer`;
        


    if (result === 'You Win!') {
        score.wins += 1;
    } else if (result === 'You Lose!') {
        score.losses += 1;
    } else if (result === 'Tie!') {
        score.ties += 1;
    }

    saveScore();
    displayScore();
    return result;
}
