_How to handle **Dependent Events**_

` from mathfun`
## Independent Events

meaning each event is **not affected** by any other events.

![head tails coin](https://www.mathsisfun.com/data/images/head-tails-dollar.jpg)

### Example: Tossing a coin.

Each toss of a coin is a perfect isolated thing.

What it did in the past will not affect the current toss.

So each toss is an **Independent Event**.

## Dependent Events

But events can also be "dependent" ... which means they **can be affected by previous events** ...

![probability marbles](https://www.mathsisfun.com/data/images/probability-marbles1.svg)

### Example: Marbles in a Bag

2 blue and 3 red marbles are in a bag.

What are the chances of getting a blue marble?

The chance is **2 in 5**

**But after taking one out** the chances change!

So the next time:

![probability marbles](https://www.mathsisfun.com/data/images/probability-marbles2.svg)  
if we got a **red** marble before, then the chance of a blue marble next is **2 in 4**

![probability marbles](https://www.mathsisfun.com/data/images/probability-marbles3.svg)  




So the next event **depends on** what happened in the previous event, and is called **dependent**.

Replacement


-   **With** Replacement: the events are **Independent** (the chances don't change)
-   **Without** Replacement: the events are **Dependent** (the chances change)

**Dependent** events are what we look at here.

## Tree Diagram

A Tree Diagram is a wonderful way to picture what is going on, so let's build one for our marbles example.

There is a 2/5 chance of pulling out a Blue marble, and a 3/5 chance for Red:

![probability marbles tree 1](https://www.mathsisfun.com/data/images/probability-marbles-tree1.svg)

We can go one step further and see what happens when we pick a second marble:

![probability marbles tree 2](https://www.mathsisfun.com/data/images/probability-marbles-tree2.svg)

I
## Notation

It means we can then use the power of algebra to play around with the ideas. So here is the notation for probability:

P(A) means "Probability Of Event A"


**P(A) = 2/5**


-   If we got a **Blue Marble first** the chance is now **1/4**
-   If we got a **Red Marble first** the chance is now **2/4**

So we have to say **which one we want**, and use the symbol "|" to mean "given":

P(B|A) means "Event B **given** Event A"

In other words, event A has already happened, now what is the chance of event B?

P(B|A) is also called the "Conditional Probability" of B given A.

And in our case:

**P(B|A) = 1/4**





### Example: Drawing 2 Kings from a Deck

**Event A** is drawing a King first, and **Event B** is drawing a King second.


P(A) = 4/52

But after removing a King from the deck the probability of the 2nd card drawn is **less** likely to be a King (only 3 of the 51 cards left are Kings):

P(B|A) = 3/51

And so:

**P(A and B) = P(A) x P(B|A)** = (4/52) x (3/51) = 12/2652 = **1/221**

So the chance of getting 2 Kings is 1 in 221, or about 0.5%

## Finding Hidden Data

Using Algebra we can also "change the subject" of the formula, like this:

<table><tbody><tr><td>Start with:</td><td>&nbsp;</td><td>P(A and B) = P(A) x P(B|A)</td></tr><tr><td>Swap sides:</td><td>&nbsp;</td><td>P(A) x P(B|A) = P(A and B)</td></tr><tr><td>Divide by P(A):</td><td>&nbsp;</td><td>P(B|A) = P(A and B) / P(A)</td></tr></tbody></table>

And we have another useful formula:

![P(B given A) = P( A and B ) / P(A) ](https://www.mathsisfun.com/data/images/probability-independent-formula2.gif)

_"The probability of **event B given event A** equals  
the probability of **event A and event B** divided by the probability of **event A**_

### Example: Ice Cream

70% of your friends like Chocolate, and 35% like Chocolate AND like Strawberry.

What percent of those who like Chocolate also like Strawberry?

P(Strawberry|Chocolate) = P(Chocolate and Strawberry) / P(Chocolate)

0.35 / 0.7 = 50%

50% of your friends who like Chocolate also like Strawberry

![soccer teams](https://www.mathsisfun.com/images/soccer-teams.jpg)

## Big Example: Soccer Game

You are off to soccer, and want to be the Goalkeeper, but that depends who is the Coach today:

-   with Coach Sam the probability of being Goalkeeper is **0.5**
-   with Coach Alex the probability of being Goalkeeper is **0.3**

Sam is Coach more often ... about 6 out of every 10 games (a probability of **0.6**).

So, what is the probability you will be a Goalkeeper today?

Let's build a [tree diagram](https://www.mathsisfun.com/data/probability-tree-diagrams.html). First we show the two possible coaches: Sam or Alex:

![tree diagram 1](https://www.mathsisfun.com/data/images/tree-diagram-ex1-1.svg)

The probability of getting Sam is 0.6, so the probability of Alex must be 0.4 (together the probability is 1)

Now, if you get Sam, there is 0.5 probability of being Goalie (and 0.5 of not being Goalie):

![tree diagram 2](https://www.mathsisfun.com/data/images/tree-diagram-ex1-2.svg)

If you get Alex, there is 0.3 probability of being Goalie (and 0.7 not):

![tree diagram 3](https://www.mathsisfun.com/data/images/tree-diagram-ex1-3.svg)

The tree diagram is complete, now let's calculate the overall probabilities. Remember that:

P(A and B) = P(A) x P(B|A)

Here is how to do it for the "Sam, Yes" branch:

![tree diagram 4](https://www.mathsisfun.com/data/images/tree-diagram-ex1-4.svg)

(When we take the 0.6 chance of Sam being coach times the 0.5 chance that Sam will let you be Goalkeeper we end up with an 0.3 chance.)

But we are not done yet! We haven't included Alex as Coach:

![tree diagram 5](https://www.mathsisfun.com/data/images/tree-diagram-ex1-5.svg)

An 0.4 chance of Alex as Coach, followed by an 0.3 chance gives 0.12

**And the two "Yes" branches of the tree together make:**

0.3 + 0.12 = **0.42 probability** of being a Goalkeeper today

(That is a 42% chance)

### Check

One final step: complete the calculations and make sure they add to 1:

![tree diagram 6](https://www.mathsisfun.com/data/images/tree-diagram-ex1-6.svg)

0.3 + 0.3 + 0.12 + 0.28 = 1

Yes, they add to **1**, so that looks right.

## Friends and Random Numbers

Here is another quite different example of Conditional Probability.

**4 friends** (Alex, Blake, Chris and Dusty) each choose a random number between 1 and 5. What is the chance that any of them chose the same number?

Let's add our friends one at a time ...

### First, what is the chance that Alex and Blake have the same number?

Blake compares his number to Alex's number. There is a 1 in 5 chance of a match.

As a [tree diagram](https://www.mathsisfun.com/data/probability-tree-diagrams.html):

![events dependent 1](https://www.mathsisfun.com/data/images/events-dependent-ex-1.svg)

Note: "Yes" and "No" together  makes 1  
(1/5 + 4/5 = 5/5 = 1)

### Now, let's include Chris ...

But there are now two cases to consider:

-   If Alex and Blake **did** match, then Chris has only **one number** to compare to.
-   But if Alex and Blake **did not** match then Chris has **two numbers** to compare to.

And we get this:

![events dependent 2](https://www.mathsisfun.com/data/images/events-dependent-ex-2.svg)

For the top line (Alex and Blake **did** match) we already have a match (a chance of 1/5).

But for the "Alex and Blake **did not** match" there is now a **2/5** chance of Chris matching (because Chris gets to match his number against both Alex and Blake).

And we can work out the combined chance by **multiplying the chances** it took to get there:

Following the "No, Yes" path ... there is a 4/5 chance of No, followed by a 2/5 chance of Yes:

(4/5) × (2/5) = 8/25

Following the "No, No" path ... there is a 4/5 chance of No, followed by a 3/5 chance of No:

(4/5) × (3/5) = 12/25

Also notice that when we add all chances together we still get 1 (a good check that we haven't made a mistake):

(5/25) + (8/25) + (12/25) = 25/25 = 1

### Now what happens when we include Dusty?

It is the same idea, just more of it:

![events dependent 3](https://www.mathsisfun.com/data/images/events-dependent-ex-3.svg)

OK, that is all 4 friends, and the "Yes" chances together make 101/125:

Answer: **101/125**

But here is something interesting ... if we follow the "No" path we can **skip all the other calculations** and make our life easier:

![events dependent 4](https://www.mathsisfun.com/data/images/events-dependent-ex-4.svg)

The chances of **not matching** are:

(4/5) × (3/5) × (2/5) = **24/125**

So the chances of **matching** are:

1 - (24/125) = **101/125**

(And we didn't really need a tree diagram for that!)

And that is a popular trick in probability:

It is often easier to work out the "No" case  
(and subtract from 1 for the "Yes" case)

