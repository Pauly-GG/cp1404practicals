def main():
    """Enter a score to display its status"""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """Determines the status of the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent score"
    elif score >= 50:
        return "Passable score"
    else:
        return "Bad score"


main()
