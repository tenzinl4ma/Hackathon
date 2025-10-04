// Convention: positive = cost/consumption, negative = benefit/production
// Units: cost = million USD, energy = kW (avg), air = tons CO2e/yr, water = m³/yr
// keys: id, name, icon, cost, water, air, energy, pop, height, dimension, color
const buildings = [

  // ——— Residential / Urban Form ———
  {
    id: 'residential-high-complex',
    name: 'High-Rise Complex',
    icon: '🏙️',
    cost: 600,                 // ~large multi-tower complex
    water: 72000,             // 100 m³/person/yr × 1,800 ppl
    air: 4500,                 // ~2.5 t CO₂e/person/yr × 1,800 ppl (ops only)
    energy: 1500,              // ~0.8 kW/person avg × 1,800
    pop: 1800,
    height: 12,
    dimension: 200,
    color: '#3b82f6'
  },
  {
    id: 'residential-suburb',
    name: 'Suburb',
    icon: '🏘️',
    cost: 200,                 // subdivision + local infra
    water: 72000,              // 120 m³/person/yr × 600 ppl
    air: 6000,                 // ~4 t CO₂e/household-leaning per person × 600 ppl (incl. ops bias)
    energy: 720,               // ~1.2 kW/person × 600
    pop: 600,
    height: 1,
    dimension: 750,
    color: '#3b82f6'
  },

  // ——— Civic / Green ———
  {
    id: 'service-school',
    name: 'School',
    icon: '🏫',
    cost: 50,
    water: 10000,
    air: 400,                  // building ops
    energy: 300,               // mid-size school avg demand
    pop: 0,
    height: 1.2,
    dimension: 200,
    color: '#a855f7'
  },
  {
    id: 'green-park',
    name: 'Parks',
    icon: '🌳',
    cost: 40,
    water: 50000,              // irrigation (depends on climate/area)
    air: -200,                 // sequestration / air-quality benefit
    energy: 20,                // lighting, pumps, facilities
    pop: 0,
    height: 1,
    dimension: 350,
    color: '#10b981'
  },

  // ——— Water & Land ———
  {
    id: 'infrastructure-canal',
    name: 'Great reservoir',
    icon: '💦',
    cost: 1200,
    water: -20000000,          // net available supply/retention
    air: -100,                 // minor regional cooling/air benefit
    energy: 0,
    pop: 0,
    height: 0.5,
    dimension: 850,
    color: '#60a5fa'
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
    dimension: 250,
    color: '#60a5fa'
  },
  {
    id: 'agri-farm',
    name: 'Farm',
    icon: '🌾🍚',
    cost: 80,
    water: 1000000,            // irrigation for sizeable area
    air: -500,                 // soil/crop sequestration (very rough)
    energy: 200,               // pumps, processing, on-site loads
    pop: 0,
    height: 0.5,
    dimension: 1000,
    color: '#84cc16'
  },

  // ——— Energy ———
  {
    id: 'energy-wind-farm',
    name: 'Wind Farm',
    icon: '⚡',
    cost: 60,                  // ~50 MW onshore @ ~$1.2M/MW
    water: 0,                  // negligible
    air: -60000,               // ~50 MW × 35% CF × 8760 h × 0.35–0.5 t/MWh
    energy: -50000,            // -50,000 kW (generation)
    pop: 0,
    height: 12,
    dimension: 450,
    color: '#efefef'
  },
  {
    id: 'energy-hydro-dam',
    name: 'Hydroelectric Dam',
    icon: '⚡',
    cost: 300,                // ~300 MW class
    water: -5000000,          // managed storage/availability (net)
    air: 0,              // displaced fossil generation
    energy: -2000000,           // -300,000 kW (generation)
    pop: 0,
    height: 2,
    dimension: 500,
    color: '#99c0e3'
  },
  {
    id: 'energy-solar',
    name: 'Solar Energy',
    icon: '⚡',
    cost: 300,                   // ~5 MW @ ~$1M/MW utility-scale
    water: 1000,               // panel cleaning
    air: 0,                // ~5 MW × 18% CF × 8760 h × 0.35 t/MWh
    energy: -5000,             // -5,000 kW (generation)
    pop: 0,
    height: 2,
    dimension: 100,
    color: '#fde047'
  },
  {
    id: 'energy-coal-plant',
    name: 'Coal Power Plant',
    icon: '🏭',
    cost: 150,                // ~600 MW new-build order of magnitude
    water: 30000000,           // cooling water withdrawals/consumption
    air: 1000000,              // ~1–4 MtCO₂e/yr depending on CF & intensity
    energy: -300000,           // -300,000 kW (generation)
    pop: 0,
    height: 2,
    dimension: 300,
    color: '#ef4444'
  }
];
