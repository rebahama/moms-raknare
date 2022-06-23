
    
   window.addEventListener('DOMContentLoaded', (event) => {
    
    let btn=document.getElementById('calculatesix');
    btn.addEventListener('click', countSix);

function countSix(){
    let valuesix=document.getElementById('summasex');
    let result=document.getElementById('result');
    let testing=document.getElementById('test-result')
    valuemoms=parseFloat(valuesix.value);
    sumIt=valuemoms * 0.06;
    newvalue=valuemoms-sumIt
    testing.innerHTML= `${valuemoms} - ${sumIt}`
    result.value=Math.round(newvalue)
    console.log(newvalue,sumIt)
    testing.value=`${valuemoms} - ${sumIt} = ${newvalue}`
}
});
    








