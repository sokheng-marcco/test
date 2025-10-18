let scores = {
        wins : 0,
        losses : 0,
        ties : 0
    };

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

    if (result === 'You Win!') {
        scores.wins += 1;
    } else if (result === 'You Lose!') {
        scores.losses += 1;
    } else if (result === 'Tie!') {
        scores.ties += 1;
    }

    alert(`You picked ${playerPick}, computer picked ${computerMove}, ${result}
Win : ${scores.wins}, Lose : ${scores.losses}, Tie : ${scores.ties}`);
}