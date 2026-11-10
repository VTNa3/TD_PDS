def letter_grade(score):
    """Return the letter grade of a score from 0 to 100."""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:          # A+ must be tested BEFORE A
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print()
for s in [99, 90, 85.5, 72, 60, 59.9, -5, 101]:
    print(f"{s:>5} -> {letter_grade(s)}")