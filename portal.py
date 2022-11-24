import random


def login_page():

    print("\n        ===Login Page===         ")
    print("---------------------------------------")
    print("| 1.  Register        | 2. Login      |")
    print("---------------------------------------")
    print("|               3.Exit                |")
    print("---------------------------------------")


def portal_menu(name):
    print("\n   === At Home Workout Portal ===       ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Bodyweight    | 2.    Cardio     |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Plyometric    | 4.    Exit       |")
    print("------------------------------------------")


def bodyweight():
    bw_exercises = ["Push Ups", "Squats", "Planks", "Seated Dips"]
    bw_exercise_pick = random.choice(bw_exercises)
    print(f"\nIt lands on {bw_exercise_pick}!!")

    reps = random.randint(5, 25)
    print(f"\nYou have {bw_exercise_pick} for {reps} reps.")


def cardio():
    car_exercises = ["Jumping Jacks", "Burpees",
                     " Mountain Climbers", "High Knees"]
    car_exercise_pick = random.choice(car_exercises)
    print(f"\nIt lands on {car_exercise_pick}!!")

    reps = random.randint(15, 30)
    print(f"\nYou have {car_exercise_pick} for {reps} second.\n")


def plyometrics():
    ply_exercises = ["Squat Jumps", "Jump Tucks",
                     " Explosion Push Up", "Lunge Jumps"]
    ply_exercise_pick = random.choice(ply_exercises)
    print(f"\nIt lands on {ply_exercise_pick}!!")

    reps = random.randint(5, 10)
    print(f"\nYou have {ply_exercise_pick} for {reps} reps.")


def exit(name):
    print(f"\nGoodbye {name}!")
