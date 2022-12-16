// Create svg and initial bars
const w1 = 500;
const h1 = 500;
const margin1 = {top: 25, right: 0, bottom: 25,
    left: 70};
const innerWidth1 = w1 - margin1.left - margin1.right;
const innerHeight1 = h1 - margin1.top - margin1.bottom;

const duration1 = [[3.0,5.0,"7 dwarfs train"], [7.5,1.5,"pirates of caribbean"], [1.5,13.5,"astro orbiter"],
[2,5.0,"regal carrousel"], [7,2.5,"big thunder7mtn"], [18,3.5,"splash mountain"], 
[10,3.0,"space mountain"], [8,3.5,"jungle cruise"], [1.5,7.5,"mad tea party"], 
[1.5,10.0,"dumbo"], [1.5,16.0,"magic carpets"], [10,1.5,"peoplemover"], 
[7,3.0,"under the sea"], [2,7.0,"barnstormer"], [4,4.0,"winnie the pooh"], 
[14.5,0,"enchanted tiki rm"], [10,2.5,"haunted mansion"], [4.5,3.0,"buzz lightyear"]];
const pop71 = ["7 dwarfs train", "pirates of caribbean", "haunted mansion",
              "splash mountain", "big thunder7mtn", "space mountain", "jungle cruise"];

const xScale1 = d3.scaleLinear()
    .domain([0,20])
    .range([0, innerWidth1]);

const yScale1 = d3.scaleLinear()
    .domain([0, 25])
    .range([innerHeight1,0]);

const xAxis1 = d3.axisBottom()
    .scale(xScale1);

const yAxis1 = d3.axisLeft()
    .scale(yScale1);

// add svg

const svg1 = d3.select("div#D3_2")
  .append("svg")
    .attr("width", 700)
    .attr("height", 700);

// add background rectangle

svg1.append("rect")
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", w+100)
    .attr("height", h+50)
    .attr("fill", "aliceblue");

// add circles as a group

const circles1 = svg1.append("g")
    .attr("id", "plot2")
    .attr("transform", `translate (${margin1.left}, ${margin1.top})`)
  .selectAll("circle")
    .data(duration1);
var curtarget = "dummyvar";
var curcolor = "dummyvar";
circles1.enter().append("circle")
    .attr("cx", d => xScale1(d[0]))
    .attr("cy", d => yScale1(d[1]))
    .attr("r", 7)
    .attr("fill", "#ffbf00")
    .on("mouseover", function(event,d) {
      curtarget = event.currentTarget;
      var xcoord = +d3.select(event.currentTarget).attr("cx") + 8;
      var ycoord = +d3.select(event.currentTarget).attr("cy") - 8;
      curcolor = d3.select(event.currentTarget).attr("fill");
      d3.select(event.currentTarget).transition().duration(250).attr("fill", "#00b384").attr("r", "9");
      svg1.select("g#plot2")
        .append("text")
        .attr("id", "tooltip2")
        .attr("x", xcoord)
        .attr("y", ycoord)
        .text("Duration: "+d3.format(".2")(d[0])+" min, \nAWT_100: "+d3.format(".2f")(d[1])+" min")
      svg1.select("g#plot2")
        .append("text")
        .attr("id", "tooltip22")
        .attr("x", xcoord)
        .attr("y", ycoord-15)
        .text("Attraction: "+d[2]);
   })
   .on("mouseout", function() {
       d3.select(curtarget).transition().duration(250).attr("fill", curcolor).attr("r", "7");
       d3.select("#tooltip2").remove();
       d3.select("#tooltip22").remove();
   });

// add axes

svg1.append("g")
    .attr("class", "xAxis")
    .attr("transform", `translate (${margin.left}, ${h - margin.bottom})`)
    .call(xAxis1);

svg1.append("text")
  .attr("class", "x label")
  .attr("text-anchor", "end")
  .attr("x", 0.7*w)
  .attr("y", h+10)
  .text("Attraction Duration (min)");

svg1.append("g")
    .attr("class", "yAxis")
    .attr("transform", `translate (${margin.left}, ${margin.top})`)
    .call(yAxis1);

svg1.append("text")
  .attr("class", "y label")
  .attr("text-anchor", "end")
  .attr("x", -0.3*h)
  .attr("y", 20)
  // .attr("dy", ".75em")
  .attr("transform", "rotate(-90)")
  .text("AWT_100 (min)");


// Button
d3.selectAll("input#dd2")
.on("click", function(event) { 
  // console.log("input");
    var pop = event.currentTarget.value; 
    console.log(pop);
    var temp = d3.select("g#plot2").selectAll("circle");
    for (let i = 0; i < 18; i++){
      var target = temp._groups[0][i];
      var name = target.__data__[2];
      if (pop71.includes(name)){
        if (pop == "pop") {
            d3.select(target).attr("fill", "red");
        }else{
          d3.select(target).attr("fill", "#ffbf00");
        }
      }
    };
    }) // end .// end .on