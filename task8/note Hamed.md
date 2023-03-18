# Binomial Distribution

The binomial distribution is a probability distribution that describes the number of successes in a fixed number of independent trials with a given probability of success.

## Formula:

The formula for the binomial distribution is:

P(X = k) = (n choose k) * p^k * (1 - p)^(n - k)

where:
- P(X = k) is the probability of k successes in n trials
- n is the number of trials
- k is the number of successes
- p is the probability of success in a single trial

## Properties:

Some important properties of the binomial distribution are:

- The mean of the binomial distribution is np
- The variance of the binomial distribution is np(1 - p)
- The shape of the distribution approaches a normal distribution as n increases, if p is not too close to 0 or 1.

## Example:


1. A baseball player has a 0.3 batting average. In a game with 5 at-bats, what is the probability he gets exactly 2 hits?
   - Solution: P(X=2) = (5 choose 2) * (0.3)^2 * (0.7)^3 = 0.3087

2. A factory produces computer chips with a 5% defect rate. If a sample of 100 chips is randomly selected, what is the probability that 8 of them are defective?
   - Solution: P(X=8) = (100 choose 8) * (0.05)^8 * (0.95)^92 = 0.088

3. In a survey, 70% of respondents said they prefer brand A over brand B. If a sample of 10 people is randomly selected, what is the probability that exactly 8 of them prefer brand A?
   - Solution: P(X=8) = (10 choose 8) * (0.7)^8 * (0.3)^2 = 0.1209

4. A restaurant has a 25% chance of getting a good review. If they ask 20 customers to leave a review, what is the probability that at least 5 of them leave a good review?
   - Solution: P(X>=5) = 1 - P(X<5) = 1 - P(X=0) - P(X=1) - P(X=2) - P(X=3) - P(X=4)
                 = 1 - (20 choose 0) * (0.25)^0 * (0.75)^20 - (20 choose 1) * (0.25)^1 * (0.75)^19 - (20 choose 2) * (0.25)^2 * (0.75)^18 - (20 choose 3) * (0.25)^3 * (0.75)^17 - (20 choose 4) * (0.25)^4 * (0.75)^16
                 = 0.8176

5. A basketball player has a 70% free-throw percentage. If she takes 10 free throws, what is the probability that she makes at least 7 of them?
   - Solution: P(X>=7) = 1 - P(X<7) = 1 - P(X=0) - P(X=1) - P(X=2) - P(X=3) - P(X=4) - P(X=5) - P(X=6)
                 = 1 - (10 choose 0) * (0.7)^0 * (0.3)^10 - (10 choose 1) * (0.7)^1 * (0.3)^9 - (10 choose 2) * (0.7)^2 * (0.3)^8 - (10 choose 3) * (0.7)^3 * (0.3)^7 - (10 choose 4) * (0.7)^4 * (0.3)^6 - (10 choose 5) * (0.7)^5 * (0.3)^5 - (10 choose 6) * (0.7)^6 * (0.3)^4
                 = 0.3732



6.100 people You know from previous data that approximately 60% of people prefer chocolate.  calculate the probability of getting different numbers of chocolate ice cream preferences. 
		the probability of exactly 50 people preferring chocolate    ice cream would be:
			P(X=50) = (100 choose 50) * (0.6)^50 * (0.4)^50 ≈ 0.079 Another example is rolling a fair die 10 times and counting the number of times the number 5 comes up. This is a binomial distribution with n = 10 and p = 1/6 (since there is a 1/6 chance of rolling a 5 on any given roll). The probability of rolling exactly 2 fives would be: P(X=2) = (10 choose 2) * (1/6)^2 * (5/6)^8 ≈ 0.224



![[Pasted image 20230318120552.png]]
![[Pasted image 20230318120618.png]]
![[Pasted image 20230318120650.png]]
![[Pasted image 20230318120711.png]]
![[Pasted image 20230318120728.png]]
![[Pasted image 20230318180615.png]]
![[Pasted image 20230318181242.png]]
