const SCORE_SCALE = 25;

const generateCharacter = () => {
  const retval = {
    attributes: {
      prowess: Math.floor(Math.random() * SCORE_SCALE) + 1,
      toughness: Math.floor(Math.random() * SCORE_SCALE / 5) + 1,
      speed: Math.floor(Math.random() * SCORE_SCALE / 5) + 1,
    },
    items_skills_and_effects: {

    },
    motivations: {

    },
    condition: {
      damage: 0,
      injury: 0
    },
    allocations: {

    }
  };
  return retval;
};


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
