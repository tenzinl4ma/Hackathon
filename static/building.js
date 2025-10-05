const buildings = [
  // ——— Residential (ADD population) ———
  {
    id: 'residential-high-complex',
    type: 'housing',
    name: 'High-Rise Complex',
    icon: '🏙️',
    cost: 900,
    money: 0,
    water: -7200,
    air: -30,
    energy: -25000,
    pop: 7000,
    labor: 7000,  // ADDS workers
    height: 12,
    dimension: 300,
    color: '#3b82f6'
  },
  {
    id: 'residential-suburb',
    type: 'housing',
    name: 'Suburb',
    icon: '🏘️',
    cost: 180,
    money: 0,
    water: -7200,
    air: -40,
    energy: -72000,
    pop: 5000,
    labor: 5000,  // ADDS workers
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
    water: -1000,
    air: -2,
    energy: -30,
    pop: 0,
    labor: -500,  // NEEDS workers (teachers)
    height: 4,
    dimension: 400,
    color: '#a855f7'
  },
  {
    id: 'service-hospital',
    type: 'civic',
    name: 'Hospital',
    icon: '🏥',
    cost: 200,
    money: -3,
    water: -2000,
    air: -5,
    energy: -50,
    pop: 0,
    labor: -800,  // NEEDS workers (doctors/nurses)
    height: 5,
    dimension: 400,
    color: '#ef4444'
  },
  {
    id: 'green-park',
    type: 'green',
    name: 'Park',
    icon: '🌳',
    cost: 60,
    money: -1,
    water: -5000,
    air: 20,
    energy: -2,
    pop: 0,
    labor: -50,  // NEEDS workers (maintenance)
    height: 1,
    dimension: 600,
    color: '#10b981'
  },
  {
    id: 'green-parkc',
    name: 'Bike Lane Network',
    icon: '🚴‍♂️',
    type: 'green',
    cost: 500,
    energy: 0,
    water: 0,
    air: -250,
    pop: 0,
    money: 0,
    labor: -100,  // NEEDS workers (maintenance)
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
    cost: 600,
    money: -3,
    water: 20000,
    air: 10,
    energy: 0,
    pop: 0,
    labor: -200,  // NEEDS workers (operators)
    height: 0.5,
    dimension: 850,
    color: '#60a5fa'
  },
  {
    id: 'infrastructure-small-reservoir',
    type: 'water',
    name: 'Small Reservoir',
    icon: '💧',
    cost: 200,
    money: -1,
    water: 5000,
    air: 3,
    energy: 0,
    pop: 0,
    labor: -50,  // NEEDS workers
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
    water: -10000,
    air: 10,
    energy: -20,
    pop: 0,
    labor: -500,  // NEEDS workers (farmers)
    height: 1,
    dimension: 1000,
    color: '#84cc16'
  },

  // ——— Energy ———
  {
    id: 'energy-coal-plant',
    type: 'energy',
    name: 'Coal Power Plant',
    icon: '⚡',
    cost: 160,
    money: 0,
    water: -2500,
    air: -20,
    energy: 100000,
    pop: 0,
    labor: -300,  // NEEDS workers (operators)
    height: 2,
    dimension: 300,
    color: '#ef4444'
  },
  {
    id: 'energy-wind-farm',
    type: 'energy',
    name: 'Wind Farm',
    icon: '⚡',
    cost: 420,
    money: -2,
    water: 0,
    air: 0,
    energy: 12000,
    pop: 0,
    labor: -150,  // NEEDS workers
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
    water: 5000,
    air: 0,
    energy: 200000,
    pop: 0,
    labor: -400,  // NEEDS workers
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
    water: -100,
    air: 0,
    energy: 20000,
    pop: 0,
    labor: -100,  // NEEDS workers
    height: 4,
    dimension: 100,
    color: '#fde047'
  },

  // ——— Industry ———
  {
    id: 'factory-standard',
    type: 'industrial',
    name: 'Standard Factory',
    icon: '🏭',
    cost: 140,
    money: 10,
    water: -2000,
    air: -30,
    energy: -25000,
    labor: -2000,  // NEEDS workers
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
    money: 5,
    water: -1200,
    air: -15,
    energy: -25000,
    labor: -2000,  // NEEDS workers
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
    money: 5,
    water: -1000,
    air: -10,
    energy: -40000,
    labor: -10000,  // NEEDS workers
    pop: 0,
    height: 6,
    dimension: 400,
    color: '#f59e0b'
  }
];