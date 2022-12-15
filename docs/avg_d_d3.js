// Create svg and initial bars

const w = 500;
const h = 500;
const margin = {top: 25, right: 0, bottom: 25,
    left: 70};
const innerWidth = w - margin.left - margin.right;
const innerHeight = h - margin.top - margin.bottom;

const duration = [[3.0,79.22,"7 dwarfs train"], [7.5,29.26,"pirates of caribbean"], [1.5,27.77,"astro orbiter"],
[2,9.42,"regal carrousel"], [7,38.38,"big thunder7mtn"], [18,45.13,"splash mountain"], 
[10,58.37,"space mountain"], [8,44.22,"jungle cruise"], [1.5,12.73,"mad tea party"], 
[1.5,21.9,"dumbo"], [1.5,18.91,"magic carpets"], [10,16.98,"peoplemover"], 
[7,20.24,"under the sea"], [2,20.23,"barnstormer"], [4,29.55,"winnie the pooh"], 
[14.5,5.07,"enchanted tiki rm"], [10,32.56,"haunted mansion"], [4.5,33.07,"buzz lightyear"]];

const xScale = d3.scaleLinear()
    .domain([0,30])
    .range([0, innerWidth]);

const yScale = d3.scaleLinear()
    .domain([0, 100])
    .range([innerHeight,0]);

const xAxis = d3.axisBottom()
    .scale(xScale);

const yAxis = d3.axisLeft()
    .scale(yScale);

// add svg

const svg = d3.select("div#D3")
  .append("svg")
    .attr("width", 700)
    .attr("height", 700);

// add background rectangle

svg.append("rect")
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", w+100)
    .attr("height", h+50)
    .attr("fill", "aliceblue");

// add circles as a group

const circles = svg.append("g")
    .attr("id", "plot")
    .attr("transform", `translate (${margin.left}, ${margin.top})`)
  .selectAll("circle")
    .data(duration);
var curtarget = "dummyvar";
circles.enter().append("circle")
    .attr("cx", d => xScale(d[0]))
    .attr("cy", d => yScale(d[1]))
    .attr("r", 7)
    .attr("fill", "#ffbf00")
    .on("mouseover", function(event,d) {
      curtarget = event.currentTarget;
      var xcoord = +d3.select(event.currentTarget).attr("cx") + 8
      var ycoord = +d3.select(event.currentTarget).attr("cy") - 8
      d3.select(event.currentTarget).transition().duration(250).attr("fill", "#00b384").attr("r", "9");
      svg.select("g#plot")
        .append("text")
        .attr("id", "tooltip")
        .attr("x", xcoord)
        .attr("y", ycoord)
        .text("Duration: "+d3.format(".2")(d[0])+" min, \nAWT: "+d3.format(".2f")(d[1])+" min")
      svg.select("g#plot")
        .append("text")
        .attr("id", "tooltip2")
        .attr("x", xcoord)
        .attr("y", ycoord-15)
        .text("Attraction: "+d[2]);
   })
   .on("mouseout", function() {
       d3.select(curtarget).transition().duration(250).attr("fill", "#ffbf00").attr("r", "7");
       d3.select("#tooltip").remove();
       d3.select("#tooltip2").remove();
   });

// add axes

svg.append("g")
    .attr("class", "xAxis")
    .attr("transform", `translate (${margin.left}, ${h - margin.bottom})`)
    .call(xAxis);

svg.append("text")
  .attr("class", "x label")
  .attr("text-anchor", "end")
  .attr("x", 0.7*w)
  .attr("y", h+10)
  .text("duration (min)");

svg.append("g")
    .attr("class", "yAxis")
    .attr("transform", `translate (${margin.left}, ${margin.top})`)
    .call(yAxis);

svg.append("text")
  .attr("class", "y label")
  .attr("text-anchor", "end")
  .attr("x", -0.3*h)
  .attr("y", 20)
  // .attr("dy", ".75em")
  .attr("transform", "rotate(-90)")
  .text("average waiting time (min)");