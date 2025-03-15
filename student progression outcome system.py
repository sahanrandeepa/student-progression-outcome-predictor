from graphics import *

def get_credits_input(credit_type):
    values = [0, 20, 40, 60, 80, 100, 120]
    while True:
        try:
            credit_input = input(f"Please enter your credits at {credit_type}: ")
            if credit_input.isnumeric():
                credit_value = int(credit_input)
                if credit_value not in values:
                    print('Out of range.')
                    continue
                return credit_value
            else:
                print('Integer required')
        except ValueError:
            print('Integer required.')

def predict_progression(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits

    progress = []
    progress_module_trailer = []
    module_retriever = []
    exclude = []

    if total_credits != 120:
        return 'Total incorrect.'

    elif fail_credits >= 80:
        exclude.append([pass_credits, defer_credits, fail_credits])
        return 'Exclude'

    elif pass_credits <= 80:
        module_retriever.append([pass_credits, defer_credits, fail_credits])
        return 'Do not Progress – module retriever'

    elif pass_credits == 100:
        progress_module_trailer.append([pass_credits, defer_credits, fail_credits])
        return 'Progress (module trailer)'

    else:
        progress.append([pass_credits, defer_credits, fail_credits])
        return 'Progress'

def create_histogram(progress_count, trailing_count, module_retriever_count, exclude_count, total_students):
    win = GraphWin("My rectangle", 800, 800)
    win.setBackground("#EDF2EC")

    Title = Text(Point(200, 50), "Histogram Results")
    Title.setTextColor("black")
    Title.setSize(30)
    Title.setStyle("bold")
    Title.draw(win)

    p1 = Text(Point(200, 600), "Progress")
    p1.setTextColor("black")
    p1.setSize(12)
    p1.setStyle("bold")
    p1.draw(win)

    p2 = Text(Point(305, 600), "Trailer")
    p2.setTextColor("black")
    p2.setSize(12)
    p2.setStyle("bold")
    p2.draw(win)

    p3 = Text(Point(418, 600), "Retriever")
    p3.setTextColor("black")
    p3.setSize(12)
    p3.setStyle("bold")
    p3.draw(win)

    p4 = Text(Point(528, 600), "Excluded")
    p4.setTextColor("black")
    p4.setSize(12)
    p4.setStyle("bold")
    p4.draw(win)

    rect1 = Rectangle(Point(150, 590), Point(250, (590 - 25 * progress_count)))
    rect1.setFill("orange")
    rect1.draw(win)

    rect2 = Rectangle(Point(260, 590), Point(360, (590 - 25 * trailing_count)))
    rect2.setFill("dark blue")
    rect2.draw(win)

    rect3 = Rectangle(Point(370, 590), Point(470, (590 - 25 * module_retriever_count)))
    rect3.setFill("dark green")
    rect3.draw(win)

    rect4 = Rectangle(Point(480, 590), Point(580, (590 - 25 * exclude_count)))
    rect4.setFill("dark red")
    rect4.draw(win)

    number1 = Text(Point(200, (580 - 25 * progress_count)), progress_count)
    number1.setTextColor("black")
    number1.setSize(12)
    number1.setStyle("bold")
    number1.draw(win)

    number2 = Text(Point(305, (580 - 25 * trailing_count)), trailing_count)
    number2.setTextColor("black")
    number2.setSize(12)
    number2.setStyle("bold")
    number2.draw(win)

    number3 = Text(Point(418, (580 - 25 * module_retriever_count)), module_retriever_count)
    number3.setTextColor("black")
    number3.setSize(12)
    number3.setStyle("bold")
    number3.draw(win)

    number4 = Text(Point(528, (580 - 25 * exclude_count)), exclude_count)
    number4.setTextColor("black")
    number4.setSize(12)
    number4.setStyle("bold")
    number4.draw(win)

    total_students_text = Text(Point(110, 710), total_students)
    total_students_text.setTextColor("black")
    total_students_text.setSize(15)
    total_students_text.setStyle("bold")
    total_students_text.draw(win)

    view = Text(Point(210, 710), "Total Student")
    view.setTextColor("black")
    view.setSize(15)
    view.setStyle("bold")
    view.draw(win)

    return win

def save_to_file(data, filename):
    with open(filename, 'a') as file:
        for entry in data:
            file.write(f"{entry[0]} - {entry[1]}, {entry[2]}, {entry[3]}\n")

def load_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(' - ')
            outcome = parts[0]
            credits = [int(x) for x in parts[1].split(', ')]
            data.append([outcome] + credits)
    return data

def main():
    progression_data = []
    total_students = 0

    while True:
        pass_credits = get_credits_input('pass')
        defer_credits = get_credits_input('defer')
        fail_credits = get_credits_input('fail')

        outcome = predict_progression(pass_credits, defer_credits, fail_credits)
        total_students += 1

        print()
        print(outcome)
        print()

        progression_data.append([outcome, pass_credits, defer_credits, fail_credits])

        user_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit: ")

        if user_input.lower() == 'q':
            save_to_file(progression_data, 'progression_data.txt')
            break
        elif user_input.lower() != 'y':
            print("Invalid input. Exiting.")
            break
        print()

    progress_count = trailing_count = module_retriever_count = exclude_count = 0

    for entry in progression_data:
        if entry[0] == 'Progress':
            progress_count += 1
        elif entry[0] == 'Progress (module trailer)':
            trailing_count += 1
        elif entry[0] == 'Do not Progress – module retriever':
            module_retriever_count += 1
        elif entry[0] == 'Exclude':
            exclude_count += 1

    histogram_win = create_histogram(progress_count, trailing_count, module_retriever_count, exclude_count, total_students)
    histogram_win.getMouse()  

   
    loaded_data = load_from_file('progression_data.txt')
    print("\nPart 2:")
    for data in loaded_data:
        print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")

if __name__ == '__main__':
    main()
