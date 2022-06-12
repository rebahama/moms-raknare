let btn3=document.getElementById('calculatetrettio')
btn3.addEventListener('click', testing3)

function testing3(){
let sumTwentyfive3=document.getElementById('summatrettio')
newSum3=parseInt(sumTwentyfive3.value);
newSumTwo3=newSum3 * 0.40
let result2=document.getElementById('resulttrettio')
result2.value=Math.round(newSumTwo3)
console.log(newSumTwo)
}