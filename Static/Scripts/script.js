 function myFunction() {
  var copyText = document.getElementById("output");
  copyText.select();
  copyText.setSelectionRange(0, 99999);

  navigator.clipboard.writeText(copyText.value);

  myButton.textContent="Text Copied!"
  Audio=document.getElementById("audio")
    Audio.play();
}

const myButton = document.getElementById('Copy');
myButton.addEventListener("click", myFunction);

Button = document.getElementById("back_button")

Button.addEventListener("click", function(){
    Audio=document.getElementById("audio2");
    Audio.play();
    Audio.addEventListener("ended", function(){
    document.getElementById("Link").click()
    });
});
 document.addEventListener('keydown', function(){
    Audio=document.getElementById("audio3")
    Audio.play();
});




