    let btn2=document.getElementById('calculatetjugofem')
    btn2.addEventListener('click', testing)

function testing(){
    let sumTwentyfive=document.getElementById('summatjugofem')
    newSum=parseInt(sumTwentyfive.value);
    newSumTwo=newSum * 0.25
    let result2=document.getElementById('resulttjugofem')
    result2.value=newSumTwo
    console.log(newSumTwo)

    
}