
async function send(){

let msg = document.getElementById("msg").value

let res = await fetch("http://localhost:5000/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:msg})
})

let data = await res.json()

let chat = document.getElementById("chat")

chat.innerHTML += "<p><b>You:</b> "+msg+"</p>"
chat.innerHTML += "<p><b>AI:</b> "+data.reply+"</p>"
chat.innerHTML += "<p><i>Emotion:</i> "+data.emotion+"</p>"

document.getElementById("msg").value = ""

}
