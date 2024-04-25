// Jay Phillips
// 4/24/2024


let stabilityScore = 0;

// Make the 
document.getElementById("calcBttn").addEventListener("click", function() {
    console.log("Here I am");
});


$.ajax({
    type: "POST",
    url: "python/calculator.py",
    data: { param: text}
  }).done(function( o ) {
     // do something
  });