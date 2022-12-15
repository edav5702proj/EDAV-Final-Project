// var state=true;
// d3.select("div#facet").selectAll("img")
//   .on("click", function(event) {
//     console.log("hello");
//       console.log(state);
//       var width = parseFloat(d3.select(event.currentTarget).attr("width"))/100;
//       console.log(width);
//   if(state==true){
// d3.select(event.currentTarget).transition().duration(100).attr("width", parseFloat(width*2*100).toFixed(2)+"%");
//       state=false;
//   }else{
// d3.select(event.currentTarget).transition().duration(100).attr("width", parseFloat(width*0.5*100).toFixed(0.5)+"%");
//       state=true;
//   }
// });
// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var allimg = document.getElementsByClassName("abnormal");
var modalImg = document.getElementById("img01");
// var captionText = document.getElementById("caption");
for (let i = 0; i < 50; i++){
  allimg[i].onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    // captionText.innerHTML = this.alt;
  }
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}