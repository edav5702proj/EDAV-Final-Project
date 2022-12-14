var state=true;
d3.select("div#facet").selectAll("img")
  .on("click", function(event) {
    console.log("hello");
      console.log(state);
      var width = parseFloat(d3.select(event.currentTarget).attr("width"))/100;
      console.log(width);
  if(state==true){
d3.select(event.currentTarget).transition().duration(100).attr("width", parseFloat(width*2*100).toFixed(2)+"%");
      state=false;
  }else{
d3.select(event.currentTarget).transition().duration(100).attr("width", parseFloat(width*0.5*100).toFixed(0.5)+"%");
      state=true;
  }
});