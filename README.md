# Strategic Fighting
A combat system whose primary focus is strategy and cost/benefit analysis, not twitch reflexes.

## Raison d'etre
Fighting systems in roleplaying games tend to be very unsatisfying. In a game driven by plot and character, the fighting experience should be focused on the stakes of the fight, the implications of engaging in the fight, the different *ways* to engage in the fight, and other high-level decisions. The actual minutia of the fighting should be left to the *character*, not the *player*. The player should focus on the character development and story, and a combat system for a roleplaying game should emphasize the *drama* and *tension* of the combat rather than the mechanics therein.

Put bluntly, just because *I* have bad reflexes or *I* can't aim worth a damn, doesn't mean that my *character* should lose the fight. Conversely, if I can just save-scum my way through various combats, then it seems like my weakling novice character somehow never loses a battle. The objective of the design of this combat system is to be vulnerable to neither failure mode.

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

### Life points. 30 of them, to be exact.

The d2 system lends itself to something akin to hitpoints, if not quite the same thing.

It so happens that 2^30 seconds works out to about 34 years, which is a reasonable estimate for about half of an average human lifespan (albeit somewhat on the short side).

Imagine a character spends every second of their life -- every tick of the wall-clock -- flipping some number of coins. When they're born, that number is 30. Every time all of the coins flip Tails, they lose one coin, and continue the process. If they lose their last coin, they die. 

The mean life expectancy for a character whose survivorship follows this model comes out to a little over 68 years, which corresponds to approximately one average human lifespan. 

This model carries a heavy emphasis on the word "average". Some characters won't live past birth -- they'll unfortunately flip all Tails in one of the earliest seconds of life, and hit a streak of Tails shortly thereafter that divide their lifespan in half and then in half again, over and over again until they are down to one coin within days or hours of age (albeit the odds of that happening are one in billions). Some characters will live for over a hundred years -- billions of seconds will go by and they will manage to avoid the dreaded all-Tails result every single time. Indeed, there is no hard-set upper limit; a person can theoretically live forever under these conditions (though infirmity and old age could be modeled as a "hard-coded" reduction in coins past some number of years of life -- for example, you automatically lose one coin every year of life past 100, such that, for the extremely fortunate few who managed to get to age 100, they can still live for another 30 years, though survival gets increasingly unlikely every year). 

Lethal damage reduces this expectation exponentially. Thus, for example, a single point of untreated lethal damage dealt at birth would reduce a character's expected lifespan in half, to about 34 years. A character born with 2 points of lethal damage, left untreated, would likely survive for 17 years. 3 points would shorten their lifespan to 8.5 years, and so on.

It's worth noting that, unlike a hitpoint system, nothing about this timetable is guaranteed. The shorter it gets, the more confident the estimate gets; but a character who's expected to live for "about another year" could die tomorrow, or could survive for another 20 years. It's possible. It's just a matter of probability.

In the context of combat, this describes how a character's subsequent post-combat life will be affected by the damage they sustain in combat. For example, a character won't want to engage in a combat in which they could theoretically prevail, but which would shorten their lifespan by decades (if said damage is left untreated). 

In practice, serious consideration of damage in combat begins to kick in at roughly the point at which the character might not be able to make it to a medical facility before their wounds start to get exponentially worse, i.e. faster than the character can reach medical attention, and faster than medical attention can alleviate them (i.e. the break-even point at which X hours of surgery can restore X hours of lifespan -- or the point at which surgeons would even bother). This is roughly proportional to the damage sustained -- so, ironically, the smallest wounds which require the least amount of healing are also the ones which the character has the longest amount of time to seek healing for, and the most grievous wounds that require the most significant medical intervention are the ones that the character has the least amount of time to seek said intervention for. 

The point of concern starts, conveniently, at roughly the halfway mark of the character's 30 starting coins, i.e. at 15 coins. A character who is down to 15 coins (who starts out flipping 15 coins every second, who will lose a coin if all remaining coins come up Tails, and who will die upon reaching 0 coins) will be expected to live for just over 20 hours. That's a good estimate of a point at which a character needs to be asking, "Can I get to a hospital/healer/medic as soon as combat is over?" It's the point at which sudden unexpected death becomes a real possibility.

Note that this 20-hour remaining lifespan is irrespective of the exact *cause* of death. The exact cause of death is determined by roleplaying and storytelling. Maybe the character bled out, or succumbed to internal injuries, or sustained progressive deterioriation from an infection, and so on.

It's also worth noting that death isn't *immediate* and without warning, when/if it does occur within those 20 hours. At some second within those hours, the character's 15 coins flip all heads, and the character loses a coin and now has 14 coins. On average, this occurs roughly 10 hours into the character's 20-hour remaining lifespan -- though it can occur in the immediate second of combat, or it can occur after days or weeks. Once it happens, those 14 coins, flipped every second with all-Tails resulting in a loss of a coin, give the character an average of 10 more hours of life -- though, again, this *can* happen at any time from immediate to never, with 10 hours being the average. Once it happens, the character is down to 13 coins, which give them an expected 7 more hours, and so on. The point is, death can come quickly or it can come slowly, but there's always a progression to it.

The point of all of this is to say that, as long as a character has more than 15 Life Coins remaining, they can more or less ignore the effects of permanent injury *within the course of that fight*. They may still have to seek medical attention after the fight (after all, if you walk away from a fight having only 20 hours to live, you haven't *won* it, exactly). But if they have 16 or more Life Coins, then they can at least more or less assume that they aren't going to spontaneously die *during that fight*. Once they're down to 15 or fewer Life Coins, though, imminent death becomes an increasingly concrete possibility. As such, though a character is implicitly rolling their Life Coins every second of their lives, this slightly tedious task doesn't carry immediate significance until they're down to 15 Life Coins.

Once the character is down to 15 Life Coins or below, the player has to roll a Life check every round of combat (e.g. every second). In other words, this is the point in the degredation of the character's health and the possibility of the charactert's demise at which the *implicit, theoretical* idea that every character lives their lives tossing a Life check every second of existence becoems not quite so implicit and theoretical, and actually concrete and real. The abstract, conceptual logic becomes something that the player actually has to do: toss their remaining number of Life Coins, remove one if they all come up Tails; and if they lose their last Life Coin, the character dies.

On the upside, this means that the *minimum* duration that a character who is down to 15 Life Points will survive (assuming they take no further Lethal damage) is 15 seconds. On the downside, it means that the "eggshell skull" principle applies: even a small amount of Lethal damage could potentially kill. You just never know.

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

#### Incapacitation
A numerical level set by an Incapacitation highwater. Incapacitation inflicts a fixed Incapacition Penalty on both attack and defense rolls. Unlike Pain, the Incapacitation Penalty is not rolled; it is subtracted directly from the Ability score.


#### Crippling
A numerical level set by a Crippling highwater. Crippling inflicts a fixed Crippled Penalty on both attack and defense rolls. Unlike Pain, the Crippled Penalty is not rolled; it is subtracted directly from the Ability score.

Unlike Pain or Incapacitation, the effects of Crippling don't automatically resolve shortly after combat. In a fight sequence, the character will carry their Crippling damage with them into the next combat. A character that takes Crippling damage may need hours, days, weeks, or months to heal -- and even then, only with bed rest. Sometimes recovery is impossible without medical or magical attention. Sometimes, Crippling damage could be permanent even *with* such measures. 

Crippling damage is counted as Lethal damage. See the description of Lethal damage above. Crippling damage is removed from a character's Life Coins. If a character is left with no Life Coins, they die.


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
