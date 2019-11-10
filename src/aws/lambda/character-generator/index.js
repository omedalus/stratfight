const SCORE_SCALE = 30;

const generateCharacter = () => {
  const retval = {
    id: "",
    client_id: "",
    game_id: "",

    attributes: {
      prowess: Math.floor(Math.random() * SCORE_SCALE) + 1,
      toughness: Math.floor(Math.random() * SCORE_SCALE / 5) + 1,
      speed: Math.floor(Math.random() * SCORE_SCALE / 5) + 1,
    },
    bonuses: [],
    condition: {
      damage: 0,
      injury: 0
    },
    allocations: {
      threaten: 0,
      guard: 0,
      attack: 0,
      defend: 0,
      pull: 0,
      dash: 0
    }
  };
  return retval;
};

const generateBonuses = () => {

};

const bonuspool = [
  {
    name: "Bruiser",
    description: "When an attack connects, it inflicts possible additional points of Damage.",
    attributes: ["skill"],
    stats: {
      damage: 5
    }
  }, {
    name: "Sparmaster",
    description: "You get 5 free points of Pull.",
    attributes: ["skill"],
    stats: {
      pull: 5
    }
  }, {
    name: "Greased",
    description: "You get 5 free points of Dash. Note that this does not help you in Pursuit.",
    attributes: ["status"],
    stats: {
      dash: 5
    }
  }, {
    name: "Gun",
    description: "You have a handgun, which gives you large bonuses to Damage and to Pursuit (because the opponent has to outrun your aim).",
    attributes: ["item", "weapon", "hand", "ranged"],
    stats: {
      damage: 20,
      pursue: 20
    }
  }, {
    name: "Sword",
    description: "You have a sword, which gives you large bonuses to Damage. It also gives you a Defense bonus if the opponent is also armed with a melee weapon.",
    attributes: ["item", "weapon", "hand", "melee"],
    stats: {
      damage: 20,
      pursue: 20
    }
  }
];



const handler = async (event) => {
  const ch = generateCharacter();

  const response = {
    statusCode: 200,
    body: JSON.stringify(ch),
  };
  return response;
};

module.exports = { 
  handler 
};
