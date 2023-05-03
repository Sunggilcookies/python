
//디지털 시계
window.onload = function(){
    setInterval(myWatch, 1000);

     function myWatch(){
        const date = new Date();
        let now = date.toLocaleTimeString();
        document.getElementById('demo').innerHTML = now;


    }



}
