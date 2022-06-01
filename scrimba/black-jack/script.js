// variable declarations

let cards = []
let sum = 0

let hasBlackJack = false
let isAlive = true
let message = ""

let messageEle = document.getElementById("message_el")
let cardEle = document.getElementById("card_el")
let sumEle = document.getElementById("sum_el")

function getRandomCard() {
    let randomNumber = Math.floor( Math.random()*13 ) + 1
    if (randomNumber > 10) {
        return 10
    } 
    else if (randomNumber === 1) {
        return 11
    } 
    else {
        return randomNumber
    }
}
function startGame(){
    isAlive = true
    let firstCard = getRandomCard()
    let secondCard = getRandomCard()
    cards = [firstCard, secondCard]
    sum = firstCard + secondCard
    renderGame()
}

function renderGame(){
    cardEle.textContent = "Cards: "
    for(let i = 0; i < cards.length; i++){
        cardEle.textContent += cards[i] + ","
    }
    sumEle.textContent = "Sum: " + sum 
    if (sum <= 20) {
        message = "Do you want to draw a new card?"
    } else if (sum === 21) {
        message = "You've got Blackjack!"
        hasBlackJack = true
    } else {
        message = "You're out of the game!"
        isAlive = false
    }
    messageEle.textContent = message
}

function newCard(){
    if (isAlive === true && hasBlackJack === false){
        let new_card = getRandomCard()
        sum += new_card
        cards.push(new_card)
        renderGame()
    }
}
