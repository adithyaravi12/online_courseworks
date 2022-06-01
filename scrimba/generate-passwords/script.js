let characters = ["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+~\\`|}{[]:;?><,./-=0123456789"]

let pf1 = document.getElementById("pass-field1")
let pf2 = document.getElementById("pass-field2")
let pf3 = document.getElementById("pass-field3")
let pf4 = document.getElementById("pass-field4")

function pass(){
    var password = ''
    str = characters[0]

    for(let count = 0; count<=15; count++){
        var char = Math.floor(Math.random() * str.length + 1)
        password += str.charAt(char)
    }
    return pass
}

function genPass(){
    pf1.textContent = pass()
    pf2.textContent = pass()
    pf3.textContent = pass()
    pf4.textContent = pass()
}