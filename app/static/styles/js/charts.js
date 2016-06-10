// var queue = d3_queue.queue();
console.log('Charts fired')
console.log('v proj2.13')

d3_queue.queue()
  .defer(d3.json, "/static/styles/datum/precincts.json")
  .await(makeGraphs);

// add network
function makeGraphs(error, precincts) {
  console.log('makeGraphs fired')
  makeMap(error, precincts);
  // add other charts etc.
};

function makeMap(error, precincts) {
  console.log('makeMap fired')
  // var precincts = precincts;

  var mapWidth = 700;
  var mapHeight = 708;

  precinctsFeatures = topojson.feature(precincts, precincts.objects.precincts).features;


  var projection = d3.geo.mercator()
    .center([-73.94, 40.70])
    .scale(60000)
    .translate([50 +(mapWidth) / 2, (mapHeight) / 2]);

  var path = d3.geo.path()
      .projection(projection);

  var mapSvg = d3.select("#mapBlock")
    .append("svg")
    .attr("width", mapWidth)
    .attr("height", mapHeight);

  mapSvg
    .attr("id", "map")
    .selectAll(".zip")
    .data(topojson.feature(precincts, precincts.objects.precincts).features)
    .enter().append("path")
    .attr("class", "zip")
    .attr("id", function(d) {
      return "zip " + d.zip;
    })
    .attr("d", path)





}
