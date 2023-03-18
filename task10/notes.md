

Bayes' Theorem is a way of finding a probability when we know certain other probabilities.

The formula is:

P(A|B) = _P(A) P(B|A)_**P(B)**

|Which tells us:| | |
| --- | --- | --- |
| | how often A happens *given that B happens*, written **P(A\|B)**, | |
| When we know:| | |
| | how often B happens *given that A happens*, written **P(B\|A)** | 
| | and how likely A is on its own, written **P(A)** | 
| | and how likely B is on its own, written **P(B)** | 

Let us say P(Fire) means how often there is fire, and P(Smoke) means how often we see smoke, then:

P(Fire|Smoke) means how often there is fire when we can see smoke  
P(Smoke|Fire) means how often we can see smoke when there is fire

So the formula kind of tells us "forwards" P(Fire|Smoke) when we know "backwards" P(Smoke|Fire)

### Example:

- dangerous fires are rare (1%)
- but smoke is fairly common (10%) due to barbecues,
- and 90% of dangerous fires make smoke

We can then discover the **probability of dangerous Fire when there is Smoke**:

P(Fire|Smoke) =_P(Fire) P(Smoke|Fire)_**P(Smoke)**

\=_1% x 90%_**10%**

\=9%

So it is still worth checking out any smoke to be sure.

![picnic](https://www.mathsisfun.com/data/images/picnic.jpg)

### Example: Picnic Day

You are planning a picnic today, but the morning is cloudy

- Oh no! 50% of all rainy days start off cloudy!
- But cloudy mornings are common (about 40% of days start cloudy)
- And this is usually a dry month (only 3 of 30 days tend to be rainy, or 10%)

**What is the chance of rain during the day?**

We will use Rain to mean rain during the day, and Cloud to mean cloudy morning.

The chance of Rain given Cloud is written P(Rain|Cloud)

So let's put that in the formula:

P(Rain|Cloud) = _P(Rain) P(Cloud|Rain)_**P(Cloud)**

- P(Rain) is Probability of Rain = 10%
- P(Cloud|Rain) is Probability of Cloud, given that Rain happens = 50%
- P(Cloud) is Probability of Cloud = 40%

P(Rain|Cloud) = _0.1 x 0.5_**0.4**  = .125

Or a 12.5% chance of rain. Not too bad, let's have a picnic!

## Just 4 Numbers

Imagine 100 people at a party, and you tally how many wear pink or not, and if a man or not, and get these numbers:

![bayes table](https://www.mathsisfun.com/data/images/bayes-table-pink-man.svg)

Bayes' Theorem is based off just those 4 numbers!

Let us do some totals:

![bayes table totals](https://www.mathsisfun.com/data/images/bayes-table-pink-man-tot.svg)

And calculate some probabilities:

-   the probability of being a man is P(Man) = _40_**100** = 0.4
-   the probability of wearing pink is P(Pink) = _25_**100** = 0.25
-   the probability that a man wears pink is P(Pink|Man) = _5_**40** = 0.125
-   the probability that a person wearing pink is a man **P(Man|Pink) = ...**

![puppy rips](https://www.mathsisfun.com/data/images/arrow-pup-rip.jpg)

And then the puppy arrives! Such a cute puppy.

But all your data is **ripped up**! Only 3 values survive:

-   **P(Man) = 0.4,**
-   **P(Pink) = 0.25 and**
-   **P(Pink|Man) = 0.125**

Can you discover **P(Man|Pink)** ?

Imagine a pink-wearing guest leaves money behind ... was it a man? We can answer this question using Bayes' Theorem:

P(Man|Pink) = _P(Man) P(Pink|Man)_**P(Pink)**

P(Man|Pink) = _0.4 × 0.125_**0.25** = 0.2

_Note: if we still had the raw data we could calculate directly _5_**25** = 0.2_

## Being General

Why does it work?

Let us replace the numbers with letters:

![bayes table](https://www.mathsisfun.com/data/images/bayes-table.svg)

Now let us look at **probabilities**. So we take some ratios:

-   the overall probability of "A" is P(A) = _s+t_**s+t+u+v**
-   the probability of "B given A" is P(B|A) = _s_**s+t**

And then multiply them together like this:

![bayes table math P(A)](https://www.mathsisfun.com/data/images/bayes-table-math-a.svg)

Now let us do that again but use **P(B)** and **P(A|B)**:

![bayes table math P(B)](https://www.mathsisfun.com/data/images/bayes-table-math-b.svg)

Both ways get the **same result** of _s_**s+t+u+v**

So we can see that:

P(B) P(A|B) = P(A) P(B|A)

_Nice and symmetrical _


Pasted image 20230318181242.png
