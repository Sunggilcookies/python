
//디지털 시계
window.onload = function(){
     setInterval(myWatch, 1000);



     function myWatch(){
        const date = new Date();
        let now = date.toLocaleTimeString();
        document.getElementById('demo').innerHTML = now;
    }
    //배역 이미지 슬라이딩
    //경로 주의 - static 폴더에서 시작함
    let picture = [
    '../static/images/header1.jpg',
    '../static/images/header2.jpg',
    '../static/images/header3.jpg'
    ]
    let imgIdx = 0;

    showPicture(); //show Picture 함수 호출

    function showPicture(){
        let img = document.getElementById('pic');
        img.src = picture[imgIdx]   // 첫 이미지 저장
        imgIdx++;
        if(imgIdx == picture.length){ //imgIdx == picture.length
            imgIdx=0;
        }
    setTimeout(showPicture, 1000);
    }
    //1초 간격으로 show Picture() 호출



}
