from random import randint

def generate_numbers(n):
    answer = [randint(1,45) for _ in range(n)]
    return answer 
    
def draw_winning_numbers():
    answer = sorted(generate_numbers(6))
    answer.append(randint(1,45))
    return answer

def count_matching_numbers(numbers, winning_numbers):
    cnt = 0
    for i in numbers:
        if i in winning_numbers:
            cnt += 1
    return cnt

def check(numbers, winning_numbers):
    cnt = count_matching_numbers(numbers,winning_numbers[:6])
    prize = 0
    if cnt >= 6:
        prize = 1000000000
    elif cnt >= 5:
        if winning_numbers[6] in numbers:
            prize = 50000000
        prize = 1000000
    elif cnt >= 4:
        prize = 50000
    elif cnt >= 3:
        prize = 5000
    return prize
