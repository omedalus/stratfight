import Vue from 'vue';
import Vuex from 'vuex';

const sampleArmors = require('./assets/sampledata/armors.json');
const sampleWeapons = require('./assets/sampledata/weapons.json');
const sampleCombatants = require('./assets/sampledata/combatants.json');

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    combatants: sampleCombatants,
    weapons: sampleWeapons,
    armors: sampleArmors
  },
  mutations: {

  },
  actions: {

  },
});
