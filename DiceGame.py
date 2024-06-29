import random

def toss_coin():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"

def main():
    print("Tossing a coin...")
    heads_count = 0
    tails_count = 0
    
    for round in range(1, 4):
        result = toss_coin()
        print(f"Round {round}: {result}")
        
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    
    print(f"Heads: {heads_count}, Tails: {tails_count}")

if __name__ == "__main__":
    main()
