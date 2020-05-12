# Strategic Fighting
A combat system whose primary focus is strategy and cost/benefit analysis, not twitch reflexes.

## Raison d'etre
Fighting systems in roleplaying games tend to be very unsatisfying. In a game driven by plot and character, the fighting experience should be focused on the stakes of the fight, the implications of engaging in the fight, the different *ways* to engage in the fight, and other high-level decisions. The actual minutia of the fighting should be left to the *character*, not the *player*. The player should focus on the character development and story, and a combat system for a roleplaying game should emphasize the *drama* and *tension* of the combat rather than the mechanics therein.

Put bluntly, just because *I* have bad reflexes or *I* can't aim worth a damn, doesn't mean that my *character* should lose the fight. Conversely, if I can just save-scum my way through various combats, then it seems like my weakling novice character somehow never loses a battle.

### Hit-point systems are boring.

"I attack. I attack again." Hitpoint systems leave the player with very few choices in combat. They also exhibit a rather silly "critical existence failure", in which a character can sustain some fixed number of injuries that will result in them losing consciousness or flat-out dying. It manages to be both boring and over-specific at the same time.

## Design

Ideally, the fighting system should be playable as a card game. This will permit friendly social beta-testing. More importantly, if the rules are straightforward enough for a card game, then they'll be easily comprehensible to players of a video game.

This system is primarily designed for combat between two characters. It'll need to be further adapted for n-ary combay.

### d2 System

Almost all "rolls" will be done by flipping some number of d2s (pennies). This will give each "roll" a nice binomial distribution -- centered enough to be fairly predictable, variant enough to still never be quite certain of what will happen. The value of the roll is the number of Heads that come up in a flip.

#### Contested Rolls

Most rolls are contested, meaning that two characters are competing for some mutually exclusive outcome (this outcome is typically, "I want to hurt that guy," versus, "I want that guy to not hurt me.") Both players flip their respective numbers of d2s, and whoever has the most Heads wins. In the event of a tie, the winner is automatically the underdog -- i.e. whichever character was flipping fewer d2s for that roll. If both characters were flipping the same number of d2s and tied, then a simple coin fip resolves the winner.

#### Notation

We'll use the notation ```D2ROLL(Value)``` to indicate to flip a number of coins indicated by the attribute or variable indicated by Value. The result of the roll is the number of Heads.

### Character Skills and Attributes

Each character knows how to perform certain offensive and defensive moves with certain weapons. ("Unarmed" is a weapon.) The character's martial training and skills with that weapon can reveal more moves. At any given moment in combat, the character can't necessarily perform all moves they know; their skill determines, in part, how many openings they see at any given time.

### Turns and Initiative

Like D&D, combat takes place in turns. Unlike D&D, these turns are not symmetrical; it is not the case that Alice attacks Bob, and then Bob attacks Alice, and so on. Combat does not occur in a fair predictable trade of blow for blow.

Instead, each turn is a contested initiative check. The character's martial skill and personal attributes improve their initiative; their armor and the weight of their weapons worsen it.
