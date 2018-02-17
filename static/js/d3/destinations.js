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
chart2.load({
  columns: [
    ['x', 'LON', 'MAD', 'PAR', 'SIN', 'EDI'],
    ['bookings', 12300, 11430, 8300, 5400, 2010]
  ]
});
chart1.load({
  columns: [
    ['x', 'MAD', 'PAR', 'LON', 'SIN', 'EDI'],
    ['searches', 13200, 11200, 7320, 4200, 3100]
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

