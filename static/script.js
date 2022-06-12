

let btn=document.getElementById('calculatesix');
btn.addEventListener('click', countSix)



function countSix(){
    let valuesix=document.getElementById('summasex');
    let result=document.getElementById('result');
    valuemoms=parseFloat(valuesix.value);
    sumIt=valuemoms * 0.06;
    
    result.value=sumIt
    console.log(sumIt)
}

