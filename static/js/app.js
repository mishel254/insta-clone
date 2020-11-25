window.onload
{
    var like = document.querySelector('#like');
    like.addEventListener('click',addlike());
    function addlike(){
        like.toggleClass("main");
        console.log('hullo')
    }
    
    addlike()
}
var a=2;
console.log(a)
