import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or max > 1000 or quantity > (max - min + 1) or quantity < 1:
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
    
def main():
    print(get_numbers_ticket(1, 49, 6))

if __name__ == "__main__":
    main()
