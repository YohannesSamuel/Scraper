var count1 = 0;
var count2 = 0;
var count3 = 0;
var count4 = 0;
var count5 = 0;
var count6 = 0;

document.getElementById("googlelab").addEventListener("click", function(){
    if(count1 == 0){
        document.getElementById("google").style.display = 'block';
        count1 = count1 + 1;
    }else{
        document.getElementById("google").style.display = 'none';
        count1 = count1 - 1;
    }
});

document.getElementById("tiktoklab").addEventListener("click", function(){
    if(count2 == 0){
        document.getElementById("tiktok").style.display = 'block';
        count2 = count2 + 1;
    }else{
        document.getElementById("tiktok").style.display = 'none';
        count2 = count2 - 1;
    }
});

document.getElementById("twitterlab").addEventListener("click", function(){
    if(count3 == 0){
        document.getElementById("twitter").style.display = 'block';
        count3 = count3 + 1;
    }else{
        document.getElementById("twitter").style.display = 'none';
        count3 = count3 - 1;
    }
});
document.getElementById("instagramlab").addEventListener("click", function(){
    if(count4 == 0){
        document.getElementById("instagram").style.display = 'block';
        count4 = count4 + 1;
    }else{
        document.getElementById("instagram").style.display = 'none';
        count4 = count4 - 1;
    }
});
document.getElementById("youtubelab").addEventListener("click", function(){
    if(count6 == 0){
        document.getElementById("youtube").style.display = 'block';
        count6 = count6 + 1;
    }else{
        document.getElementById("youtube").style.display = 'none';
        count6 = count6 - 1;
    }
});
document.getElementById("linkedinlab").addEventListener("click", function(){
    if(count5 == 0){
        document.getElementById("linkedin").style.display = 'block';
        count5 = count5 + 1;
    }else{
        document.getElementById("linkedin").style.display = 'none';
        count5 = count5 - 1;
    }
});