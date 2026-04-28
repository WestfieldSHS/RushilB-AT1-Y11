from colours import*
from colorama import Fore, Style, Back

#Reading Time Estimator
def estimate_time(text, wpm):
    words = text.split()
    return len(words) / wpm

#ESTIMATE PAUSE TIME BASED ON PUNCTUATION
def estimate_pauses(text):
    pause_time = 0
    pause_time += text.count(",") * 0.5 #Pause for 0.5 seconds for each comma
    pause_time += text.count(".") * 1   #Pause for 1 second for each full stop
    pause_time += text.count("!") * 1.2 #Pause for 1.2 seconds for each exclamation mark
    pause_time += text.count("?") * 1.2 #Pause for 1.2 seconds for each question mark
    pause_time += text.count("\n") * 2 #Pause for 2 seconds for each new line
    return pause_time

#USER INPUT SECTION
print("Choose your user type:")
print("1. Student")
print("2. Teacher")
print("3. Professional/Presenter/Other")

user = input("Enter 1, 2, or 3: ")

while True:
    print("Reading Style:")
    print("1. Silent (in the head)")
    print("2. Aloud (out loud)")

    reading_style = input("Enter 1 or 2: ")

    text = input("Paste your text here: ")
    if user == "1":  #Student
        print("What year are you in?")
        print("Kindergarten") 
        print("1st grade")
        print("2nd grade")
        print("3rd-5th grade")
        print("6th-8th grade")
        print("9th-12th grade")

        grade = input("Enter your year level (K-12): ")

    	#GRADE BASED WPM SELECTION
        if grade == "K":
            wpm = 20
        elif grade == "1":
            wpm = 60 if reading_style == "1" else 80
        elif grade == "2":
            wpm = 70 if reading_style == "1" else 108
        elif grade == "3":
            wpm = 90 if reading_style == "1" else 130
        elif grade == "4":
            wpm = 120 if reading_style == "1" else 158
        elif grade == "5":
            wpm = 130 if reading_style == "1" else 173
        elif grade == "6":
            wpm = 150 if reading_style == "1" else 185
        elif grade == "7":
            wpm = 150 if reading_style == "1" else 204
        elif grade == "8":
            wpm = 150 if reading_style == "1" else 204
        elif grade in ["9", "10", "11", "12"]:
            wpm = 180 if reading_style == "1" else 250
        else:
            print("Invalid grade level.")
            continue

    #USER TYPE: TEACHER
    elif user == "2":  
        wpm = 183 if reading_style == "1" else 260
        
    #USER TYPE: PROFESSIONAL/PRESENTER/OTHER
    elif user == "3":  
        wpm = 238 if reading_style == "1" else 155
    else:
        print("Invalid choice. Please enter 1, 2, or 3 .")


    base_seconds = estimate_time(text, wpm) * 60
    pause_seconds = estimate_pauses(text)
    total_seconds = base_seconds + pause_seconds

    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)

    word_count = len(text.split())
    character_count = len(text)

    print(f"{Fore.YELLOW}\n--- Reading Summary ---{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Reader Type: {Style.RESET_ALL}{'Student' if user=='1' else 'Teacher' if user=='2' else 'Professional'}")
    if user == "1":
        print(f"{Fore.RED}Grade Level: {Style.RESET_ALL}{grade}")
    print(f"{Fore.GREEN}Reading Style: {Style.RESET_ALL}{'Silent' if reading_style=='1' else 'Aloud'}")
    print(f"{Fore.BLUE}Word Count: {Style.RESET_ALL}{word_count}")
    print(f"{Fore.MAGENTA}Character Count: {Style.RESET_ALL}{character_count}")
    print(f"{Fore.WHITE}Estimated Time: {Style.RESET_ALL}{minutes} minutes {seconds} seconds")
    print("___________________________________________")

    repeat = input("\nDo you want to run the program again? (yes/no)(If you click yes the user type will still be the same): ")
    if repeat != "yes":
        print("Please run the program again if you want to estimate another text. Goodbye!")
        break