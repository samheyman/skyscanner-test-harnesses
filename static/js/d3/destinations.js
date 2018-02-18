// fare search history
// actual numbers
// type=fare-search
var chart1 = c3.generate({
    bindto: '#destinations_most_searched_chart',
    data: {
      x: 'x',
      columns: [
        ['x', 'PAR', 'LON', 'NYC', 'TUN', 'BCN'],
        ['searches', 17750, 5976, 5620, 4611, 4104],
      ],

      types: {
        searches: 'bar'
      },
      colors: {
        searches: '#005EB8',
      }
    },
    axis : {
        x : {
            type: 'category',
            categories: ['PAR', 'LON', 'NYC', 'TUN', 'BCN'] 
        }
    }
});

// Most travelled destinations - has to be anonymised 
// Top destinations - flight scores
// type = air-traffic
var chart2 = c3.generate({
  bindto: '#destinations_most_travelled_chart',
  data: {
    x: 'x',
    columns: [
      ['x', 'PAR', 'LON', 'NYC', 'TUN', 'BCN'],
      ['bookings', 17750, 5976, 5620, 4611, 4104],
    ],

    types: {
      bookings: 'bar'
    },
    colors: {
      bookings: '#9BCAEB',
    }
  },
  axis : {
      x : {
          type: 'category',
          categories: ['PAR', 'LON', 'NYC', 'TUN', 'BCN']
          
      }
  }

});


function load_charts() { 

  chart1.load({
    columns: [
      ['x', 'PAR', 'LON', 'NYC', 'TUN', 'BCN'],
      ['searches', 13200, 11200, 7320, 4200, 3100]
    ]
  });

  chart2.load({
    columns: [
      most_travelled_data_xs,
      most_travelled_data_values
    ]
  });
}

// setTimeout(function () {
//     chart.load({
//         columns: [
//             ['data3', 130, -150, 200, 300, -200, 100]
//         ]
//     });
// }, 1000);

