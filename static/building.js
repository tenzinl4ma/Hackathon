
const buildings = [
  {
    id: 'residential-high-complex',
    name: 'High-Rise Complex',
    icon: '🏙️',
    cost: 600,
    water: 72000,
    air: 4500,
    energy: -150000,
    pop: 1800,
    height: 12,
    dimension: 300,
    color: '#3b82f6',
    carbon: 4500          // same as operational CO2e
  },
  {
    id: 'residential-suburb',
    name: 'Suburb',
    icon: '🏘️',
    cost: 200,
    water: 72000,
    air: 6000,
    energy: -720000,
    pop: 800,
    height: 3,
    dimension: 750,
    color: '#3b82f6',
    carbon: 6000
  },

  // ——— Civic / Green ———
  {
    id: 'service-school',
    name: 'School',
    icon: '🏫',
    cost: 50,
    water: 10000,
    air: 400,
    energy: 300,
    pop: 0,
    height: 4,
    dimension: 400,
    color: '#a855f7',
    carbon: 400
  },
  {
    id: 'green-park',
    name: 'Parks',
    icon: '🌳',
    cost: 40,
    water: 50000,
    air: -200,
    energy: 20,
    pop: 0,
    height: 1,
    dimension: 600,
    color: '#10b981',
    carbon: -200         // carbon sequestration
  },

  // ——— Water & Land ———
  {
    id: 'infrastructure-canal',
    name: 'Great reservoir',
    icon: '💦',
    cost: 1200,
    water: -20000000,
    air: -100,
    energy: 0,
    pop: 0,
    height: 0.5,
    dimension: 850,
    color: '#60a5fa',
    carbon: -100
  },
  {
    id: 'canal',
    name: 'Small reservoir',
    icon: '💧',
    cost: 300,
    water: -5000000,
    air: -30,
    energy: 0,
    pop: 0,
    height: 0.5,
    dimension: 350,
    color: '#60a5fa',
    carbon: -30
  },
  {
    id: 'agri-farm',
    name: 'Farm',
    icon: '🌾🍚',
    cost: 80,
    water: 1000000,
    air: -500,
    energy: 200,
    pop: 0,
    height: 1,
    dimension: 1000,
    color: '#84cc16',      // rough sequestration
  },

  // ——— Energy ———
  {
    id: 'energy-wind-farm',
    name: 'Wind Farm',
    icon: '⚡',
    cost: 60,
    water: 0,
    air: -60000,
    energy: -50000,
    pop: 0,
    height: 2,
    dimension: 450,
    color: '#efefef',      // avoids fossil emissions
  },
  {
    id: 'energy-hydro-dam',
    name: 'Hydroelectric Dam',
    icon: '⚡',
    cost: 300,
    water: -5000000,
    air: 0,
    energy: -2000000,
    pop: 0,
    height: 2,
    dimension: 600,
    color: '#99c0e3',       // net neutral (rough estimate)
  },
  {
    id: 'energy-solar',
    name: 'Solar Energy',
    icon: '⚡',
    cost: 300,
    water: 10000,
    air: 0,
    energy: -9000,
    pop: 0,
    height: 4,
    dimension: 100,
    color: '#fde047',     // avoided emissions from grid
  },
  {
    id: 'energy-coal-plant',
    name: 'Coal Power Plant',
    icon: '⚡',
    cost: 150,
    water: 3000000,
    air: 1000000,
    energy: +300000,
    pop: 0,
    height: 2,
    dimension: 300,
    color: '#ef4444',      // roughly equal to air emissions
  },
  {
    id: 'factory',
    icon: '🏭',
    cost: 150,
    water: 100000,
    energy: -20000,
    money: 1000,
    air: 1000000
  }
];
