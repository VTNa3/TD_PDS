def digit_sum(n):
    """Add up the digits of a whole number."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10        # last digit
        n //= 10               # drop the last digit
    return total


def reverse_number(n):
    """Return the digits of n in reverse order, e.g. 1234 -> 4321."""
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result


def is_palindrome(n):
    """True when n reads the same in both directions."""
    return n == reverse_number(n)


print()
for n in [2026, 12321, 9875]:
    print(f"{n}: digit sum = {digit_sum(n)}, reversed = {reverse_number(n)}, "
        f"palindrome = {is_palindrome(n)}")

count = 0
for n in range(10, 1000):
    if is_palindrome(n):
        count += 1
print("Palindromes from 10 to 999:", count)