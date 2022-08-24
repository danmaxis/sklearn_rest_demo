

// Set a random number between -5 and 5 as mu
var mu = Math.random() * 10 - 5;

var randoms = Float64Array.from({length: 2000}, d3.randomNormal(mu, 2));
// Insert the histogram into the DOM
//var histogram = d3.histogram(randoms, {width:200, height: 200, color: "steelblue", domain: [-10, 10]});
//d3.select("#graph_area").


var chart = c3.generate({
    bindto: '#graph_area',
    data: {
      columns: [
        randoms,
      ]
    }
});