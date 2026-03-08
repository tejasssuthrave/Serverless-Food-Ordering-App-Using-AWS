const API_URL = "https://ta2kg0he2i.execute-api.us-west-1.amazonaws.com/test";

async function loadMenu(){

try{

const response = await fetch(API_URL + "/Get-menu");
const data = await response.json();

const menuDiv = document.getElementById("menu");
menuDiv.innerHTML="";

data.forEach(item => {

menuDiv.innerHTML += `
<div class="card">
<img src="${item.image_url}">
<h3>${item.food_name}</h3>
<p>₹${item.price}</p>
</div>
`;

});

}catch(error){
console.log(error);
document.getElementById("menu").innerHTML="Failed to load menu";
}

}

async function placeOrder(){

const user = document.getElementById("user").value;
const food = document.getElementById("food").value;
const quantity = document.getElementById("quantity").value;

if(!user || !food || !quantity){
document.getElementById("result").innerText="Please fill all fields";
return;
}

const response = await fetch(API_URL + "/place-order",{

method:"PUT",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
user:user,
food:food,
quantity:quantity
})

});

const result = await response.text();

document.getElementById("result").innerText=result;

}

loadMenu();