const buildings = [
  // ——— Residential ———
  {
    id: 'residential-high-complex',
    type: 'residential',
    name: 'High-Rise Complex',
    icon: '🏙️',
    cost: 900,
    money: 10,                 // generates small income per sec
    water: -72000,             // uses water
    air: -4500,                // emits pollution
    energy: -250000,           // consumes energy
    pop: 1800,
    height: 12,
    dimension: 300,
    color: '#3b82f6'
  },
  {
    id: 'residential-suburb',
    type: 'residential',
    name: 'Suburb',
    icon: '🏘️',
    cost: 180,
    money: 8,
    water: -72000,
    air: -6000,
    energy: -720000,
    pop: 800,
    height: 3,
    dimension: 750,
    color: '#3b82f6'
  },

  // ——— Civic / Green ———
  {
    id: 'service-school',
    type: 'civic',
    name: 'School',
    icon: '🏫',
    cost: 120,
    money: -2,
    water: -10000,
    air: -400,
    energy: -300,
    pop: 0,
    height: 4,
    dimension: 400,
    color: '#a855f7'
  },
  {
    id: 'green-park',
    type: 'green',
    name: 'Park',
    icon: '🌳',
    cost: 60,
    money: -1,
    water: -50000,             // irrigation use
    air: 200,                  // cleans air
    energy: -20,
    pop: 0,
    height: 1,
    dimension: 600,
    color: '#10b981'
  },

  // ——— Water & Land ———
  {
    id: 'infrastructure-great-reservoir',
    type: 'water',
    name: 'Great Reservoir',
    icon: '💦',
    cost: 1400,
    money: -3,
    water: 20000000,           // supplies water
    air: 100,
    energy: 0,
    pop: 0,
    height: 0.5,
    dimension: 850,
    color: '#60a5fa'
  },
  {
    id: 'infrastructure-small-reservoir',
    type: 'water',
    name: 'Small Reservoir',
    icon: '💧',
    cost: 320,
    money: -1,
    water: 5000000,
    air: 30,
    energy: 0,
    pop: 0,
    height: 0.5,
    dimension: 350,
    color: '#60a5fa'
  },
  {
    id: 'agri-farm',
    type: 'landuse',
    name: 'Farm',
    icon: '🌾🍚',
    cost: 100,
    money: 6,
    water: -1000000,
    air: 500,                  // slight sequestration
    energy: -200,
    pop: 0,
    height: 1,
    dimension: 1000,
    color: '#84cc16'
  },

  // ——— Energy ———
  {
    id: 'energy-wind-farm',
    type: 'energy',
    name: 'Wind Farm',
    icon: '⚡',
    cost: 420,
    money: -2,
    water: 0,
    air: 60000,                // cleans air (avoided pollution)
    energy: 120000,            // produces clean energy
    pop: 0,
    height: 2,
    dimension: 450,
    color: '#efefef'
  },
  {
    id: 'energy-hydro-dam',
    type: 'energy',
    name: 'Hydroelectric Dam',
    icon: '⚡',
    cost: 1300,
    money: -8,
    water: 5000000,            // adds secure supply
    air: 0,
    energy: 2000000,           // large generation
    pop: 0,
    height: 2,
    dimension: 600,
    color: '#99c0e3'
  },
  {
    id: 'energy-solar',
    type: 'energy',
    name: 'Solar Energy',
    icon: '⚡',
    cost: 300,
    money: -1,
    water: -1000,
    air: 0,
    energy: 20000,
    pop: 0,
    height: 4,
    dimension: 100,
    color: '#fde047'
  },
  {
    id: 'energy-coal-plant',
    type: 'energy',
    name: 'Coal Power Plant',
    icon: '⚡',
    cost: 160,
    money: 40,
    water: -3000000,
    air: -1000000,
    energy: 500000,
    pop: 0,
    height: 2,
    dimension: 300,
    color: '#ef4444'
  },

  // ——— Industry ———
  {
    id: 'factory-standard',
    type: 'industrial',
    name: 'Standard Factory',
    icon: '🏭',
    cost: 140,
    money: 35,
    water: -300000,
    air: -400000,
    energy: -150000,
    pop: 0,
    height: 3,
    dimension: 500,
    color: '#9ca3af'
  },
  {
    id: 'factory-sustainable',
    type: 'industrial',
    name: 'Sustainable Factory',
    icon: '🌲🏭',
    cost: 260,
    money: 20,
    water: -120000,
    air: -50000,
    energy: -50000,
    pop: 0,
    height: 3,
    dimension: 500,
    color: '#16a34a'
  },

  // ——— Commercial ———
  {
    id: 'commercial-district',
    type: 'commercial',
    name: 'Commercial District',
    icon: '💰',
    cost: 350,
    money: 25,
    water: -100000,
    air: -3000,
    energy: -60000,
    pop: 0,
    height: 6,
    dimension: 400,
    color: '#f59e0b'
  }
];
