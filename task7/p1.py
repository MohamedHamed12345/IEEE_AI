import math

def probability_of_k(n, k, p):
        q = 1 - p
        return math.comb(n, k) * pow(p , k) * (pow(q , n - k))

def solve():

    n = int(input('Enter the number of  flips: '))
    coin_side = input("Head or Tail: ")
    k = int(input(f"the number of  {coin_side}  appearnce: "))
    p = float(input(f"Enter the probability of  {coin_side}(1<): "))
    probability = probability_of_k(n, n - k, p)

    print("The answer is:", round(probability,2))
        

if __name__ == "__main__":
        solve()

