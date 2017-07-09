// introduction https://d3js.org/#introduction

// source
<script src="https://d3js.org/d3.v4.js"></script>
<script src="https://d3js.org/d3-selection.v1.min.js"></script>


//////////////////// SELECTION ////////////////////
  // select will grab the first selection it encounters
  // selectAll will grab all selection
d3.select(".main-title") //select class
d3.select("#header") // select id
d3.select("h1") // select tag
d3.select("img").attr("src") // select an attribute eg., <img src="./assets/udacity.svg">

  // nested selection
d3.select("#header img") // select parent id=header, and then followed by the child tag <img>. Need not be direct child



//////////////////// SWAP ////////////////////
  // change text
d3.select(".main-title").text("I changed the title");


//////////////////// TRANSITIONS ////////////////////

// fade transition
d3.select("body").transition()
    .style("background-color", "black");