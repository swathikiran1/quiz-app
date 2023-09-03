# Python GK Quiz App

print("Hello, welcome to the GK quiz. Answer the questions as they are presented.")


class Question:
    def __init__(self, questionText, answer, multipleChoiceOptions=None):
        self.questionText = questionText
        self.answer = answer
        self.multipleChoiceOptions = multipleChoiceOptions

    def __repr__(self):
        return '{' + self.questionText + ', ' + self.answer + ', ' + str(self.multipleChoiceOptions) + '}'


quizQuestions = [
    Question("Question 1. Which planet in the solar system is the hottest", "B", [
             "A. Mercury", "B. Venus", "C. Earth", "D. Mars"]),
    Question("Question 2. What city is the capital of Japan", "A", [
             "A. Tokyo", "B. New Delhi", "C. Canberra", "D. London"]),
    Question("Question 3. Which is the largest country in the world",
             "D", ["A. India", "B. Australia", "C. China", "D. Russia"]),
    Question("Question 4. Which country takes the most land mass", "B", [
             "A. United States", "B. Russia", "C. Australia", "D. Antarctica"]),
    Question("Question 5. Which is the coldest continent in the world", "D", [
             "A. United States", "B. Russia", "C. Australia", "D. Antarctica"]),
    Question("Question 6. Which country produces maximum aluminium in the world", "C", [
             "A. India", "B. Australia", "C. Jamaica", "D. Russia"]),
    Question("Question 7. How many countries are present in Africa",
             "B", ["A. 53", "B. 54", "C. 55", "D. 56"]),
    Question("Question 8. How many bones are in the human body",
             "A", ["A. 206", "B. 207", "C. 208", "D. 209"]),
    Question("Question 9. What is the most abundant gas in Earth's atmosphere", "A", [
             "A. Nitrogen", "B. Hydrogen", "C. Carbon-Dioxide", "D. Oxygen"]),
    Question("Question 10. Which planet is nearest to the Earth", "D",
             ["A. Mars", "B. Mercury", "C. Jupiter", "D. Venus"]),
    Question("Question 11. Which is the hottest continent on Earth", "A", [
             "A. Africa", "B. Asia", "C. Europe", "D. South America"]),
    Question("Question 12. Which is the highest mountain in the world", "A", [
             "A. Mount Everest", "B. Mount Kilimanjaro", "C. Aconcagua", "D. Denali"]),
    Question("Question 13. What is the capital of Uttar Pradesh", "D", [
             "A. Hyderabad", "B. Mumbai", "C. Kolkata", "D. Lucknow"]),
    Question("Question 14. Which country has the largest population in the world", "C", [
             "A. United States", "B. Russia", "C. India", "D. China"]),
    Question("Question 15. What is the capital of India", "D", [
             "A. Mumbai", "B. Hyderabad", "C. Kolkata", "D. New Delhi"]),
    Question("Question 16. How many number of Union Territories there in India", "C", [
             "A. 6", "B. 7", "C. 8", "D. 9"]),
    Question("Question 17. Which is the brightest planet in the Solar system.", "B", [
             "A. Mercury", "B. Venus", "C. Earth", "D. Jupiter"]),
    Question("Question 18. Where is Gir National Park located", "C", [
             "A. Andhra Pradesh", "B. Bihar", "C. Gujarat", "D. Tamilanadu"]),
    Question("Question 19. Which is the largest beach in India", "B", [
             "A. Rk Beach", "B. Marina Beach", "C. Puri Beach", "D. Mahabalipuram Beach"]),
    Question("Question 20. Which is the largest planet in Solar system",
             "D", ["A. Mercury", "B. Venus", "C. Earth", "D. Jupiter"])
]

score = 0

for question in quizQuestions:
    print("-" * 60)
    if (question.multipleChoiceOptions != None):
        print("{}?".format(question.questionText))
        for option in question.multipleChoiceOptions:
            print(option)
        userInput = input("Enter (A, B, C, D): ")
    else:
        print("{}?".format(question.questionText))
        userInput = input("Enter (A, B, C, D): ")

    if (userInput.lower() == question.answer.lower()):
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print("{} is the correct answer".format(question.answer))

print("-" * 60)

print("                         RESULTS                       ")

print("-" * 60)

print("Your score is {}%".format(int(score / len(quizQuestions))*100))
