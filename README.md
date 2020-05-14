# Strategic Fighting
A combat system whose primary focus is strategy and cost/benefit analysis, not twitch reflexes.

## Raison d'etre
Fighting systems in roleplaying games tend to be very unsatisfying. In a game driven by plot and character, the fighting experience should be focused on the stakes of the fight, the implications of engaging in the fight, the different *ways* to engage in the fight, and other high-level decisions. The actual minutia of the fighting should be left to the *character*, not the *player*. The player should focus on the character development and story, and a combat system for a roleplaying game should emphasize the *drama* and *tension* of the combat rather than the mechanics therein.

Put bluntly, just because *I* have bad reflexes or *I* can't aim worth a damn, doesn't mean that my *character* should lose the fight. Conversely, if I can just save-scum my way through various combats, then it seems like my weakling novice character somehow never loses a battle.

## Design

Ideally, the fighting system should be playable as a tabletop game using cards, dice, coins, etc. This will permit friendly social beta-testing. More importantly, if the rules are straightforward enough for a tabletop game, then they'll be easily comprehensible to players of a video game.

### d2 System

Almost all "rolls" will be done by flipping some number of d2s (pennies). This will give each "roll" a nice binomial distribution -- centered enough to be fairly predictable, variant enough to still never be quite certain of what will happen. The value of the roll is the number of Heads that come up in a flip.

#### Notation

We'll use the notation ```Result = D2ROLL(Value)``` to indicate to flip a number of coins indicated by the attribute or variable indicated by *Value*. The *Result* of the roll is the number of Heads.

#### Contested Rolls and Flip-Offs

Most rolls are contested, meaning that two characters are competing for some mutually exclusive outcome (this outcome is typically, "I want to hurt that guy," versus, "I want that guy to not hurt me.") Both players flip their respective numbers of d2s, and whoever has the most Heads wins.

In the event of a tie, the players who tied hold a **Flip-Off**.
1. Start with the players who tied the contested roll.
1. Each remaining player flips a d2.
1. If everyone flipped Tails, repeat from Step 2.
1. Everyone who flipped Tails is eliminated from the Flip-Off.
1. If only one player is left, that player is the winner of the Flip-Off.
1. Repeat from Step 2.

### Highwaters, Not Hit-Points

"I attack. I attack again." Hitpoint systems leave the player with very few choices in combat. They also exhibit a rather silly "critical existence failure", in which a character can sustain some fixed number of injuries that will result in them losing consciousness or flat-out dying. It manages to be both boring and over-specific at the same time.

What we will use instead are *highwater* systems. These represent levels of various forms of disability that get set during the course of combat. Only the damage of a particular type sustained during a single attack counts towards setting a character's highwater mark for that type of damage during that session of combat. In other words, damage is not cumulative -- instead, damage is set to the single worst instance sustained during a fight. 

**Example**: A character starts combat with a Pain level of 0. Their opponent lands a successful blow upon them, dealing 4 points of Pain. That character's Pain level is now 4. A subsequent attack deals 2 points of Pain, but 2<4, so the character's Pain level is still 4. Another attack deals 6 points of Pain, so that character's Pain level is now 6. All subsequent attacks during that fight happen to deal Pain damage below 6, so the character's Pain level stays 6 until the end of combat.


### Damage Types

This combat system does not use hitpoints. Instead, it uses specific status effects, which affect subsequent combat rolls.

#### Pain
A numerical level set by a Pain highwater. Pain inflicts a variable Pain Penalty on an attacker's Attack Ability, which causes an attacker to be unable to execute an attack quite as effectively. A value of ```Pain Penalty = ROLL(Attacker's current Pain level)``` is subtracted from the attacker's Attack Ability. 

Each character starts each combat with a Pain level of 0. If the Pain Penalty is greater than or equal to the Attack Ability (thus reducing the effective Attack Ability to 0 or below), then the attack automatically fails.

##### Example
An attacker has an Attack Ability of 10, and is about to issue an attack which would normally flip 10d2 to determine effectiveness. However, the attacker has a Pain level of 4. Just before the attack roll, but after the player has already selected to perform the attack, the attacker flips 4d2 to determine their Pain Penalty. They roll a Pain Penalty of 3, which they subtract from their Attack Ability. Thus, for that particular attack roll, their effective Ability is not 10 but rather 7. They don't flip 10d2, but rather 7d2.

##### Roleplaying
Pain is meaningful in combat insofar as it causes distraction and lack of control. Pain causes the character's body to refuse to obey the commands of the mind. If the player commands the character to execute an action during combat, then it's understood that the character is gritting their teeth and forcing themselves to fight through the pain; but this exertion of willpower takes its toll in the form of poor execution and inadequate concentration on technique.

#### Crippling
A numerical level set by a Crippling highwater. Crippling inflicts a fixed Crippled Penalty on both attack and defense rolls. Unlike Pain, the Crippled Penalty is not rolled; it is subtracted directly from the Ability score.

Unlike Pain, the effects of Crippling don't automatically resolve shortly after combat. In a fight sequence, the character will carry their Crippling damage with them into the next combat. A character that takes Crippling damage may need hours, days, weeks, or months to heal -- and even then, only with bed rest. Sometimes recovery is impossible without medical or magical attention. Sometimes, Crippling damage could be permanent even *with* such measures. 

##### Example
An attacker has an Attack Ability of 10, but they've sustained 4 points of Crippling. If they attempt to attack, they will do so at an effective Attack Ability of 6.

##### Roleplaying
Crippling represents a generic form of bodily damage that physically prevents a character from fighting effectively. This includes things like broken limbs, head trauma, injury to the sensory organs such as the eyes and ears, or the effects of toxins or narcotics. 

Crippling is separate from Pain. While Pain represents resistance to the mind's ability to force the body to perform, Crippling represents the degradation of the body's physical ability to obey the mind's commands. For example, a character might not even *feel* that their leg is broken, but a fractured femur simply won't bear their standing weight. A character who's drunk to the point of seeing double may very well *want* to fight, but their senses simply don't give them accurate information about where to aim their fists.

Because Crippling damage takes much more time to heal than Pain, the character's willingness to accumulate Crippling damage must be weighed against what's at stake in the fight. It's reasonable for a character to really not care at all about Pain, because it's temporary -- they know that, after the fight, they can just walk it off. But the long-lasting or potentially even permanent disabilities resulting from a Crippling injury are so serious that there'd better be something worth getting seriously hurt for, otherwise it's probably time to end the fight.



### Character Skills and Attributes

Each character knows how to perform certain offensive and defensive moves with certain weapons. ("Unarmed" is a weapon.) The character's martial training and skills with that weapon can reveal more moves. At any given moment in combat, the character can't necessarily perform all moves they know; their skill determines, in part, how many openings they see at any given time.

#### Attributes

* **Agility**: 

### Turns and Initiative

Like D&D, combat takes place in turns. Unlike D&D, these turns are not symmetrical; it is not the case that Alice attacks Bob, and then Bob attacks Alice, and so on. Combat does not occur in a fair predictable trade of blow for blow.

Instead, each turn is a contested initiative check. The character's martial skill and personal attributes improve their initiative; their armor and the weight of their weapons worsen it.
