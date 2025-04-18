# main.py
def sum_even(nums: list[int]) -> int:
    """Повертає суму всіх парних чисел зі списку."""
    return sum(x for x in nums if x % 2 == 0)

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5, 6]
    print(f"Сума парних елементів: {sum_even(sample)}")
