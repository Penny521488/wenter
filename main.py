def determine_grade(score):
    if 0 <= score <= 49:
        return "незадовільно"
    elif 50 <= score <= 69:
        return "задовільно"
    elif 70 <= score <= 89:
        return "добре"
    elif 90 <= score <= 100:
        return "відмінно"
    else:
        return "Invalid score"

score = int(input("Введіть кількість балів: "))
grade = determine_grade(score)
print(f"Ваша оцінка: {grade}")
