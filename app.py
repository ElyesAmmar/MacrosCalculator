from calculator import cal_macros

activity_list = {
    "1": "Sedentary",
    "2": "Lightly Active",
    "3": "Moderately Active",
    "4": "Very Active",
    "5": "Extra Active"
}
goal_list = {
    "1": "weight loss",
    "2": "extreme weight loss",
    "3": "maintenance",
    "4": "muscle gain",
    "5": "extreme muscle gain"
}


def activity(lists):
    msg = ''
    # map(lambda item: msg_activity + item)
    for item in lists:
        msg = msg + "\n" + f"if {str(lists[item])} enter {item}"
    return msg + "\n"


msg_activity = activity(activity_list)
msg_goal = activity(goal_list)
user_name = input("Enter username:")
user_age = input("Enter your age:")
user_gender = input("Enter your gender male or female:")
user_weight = input("Enter weight kg:")
user_height = input("Enter height cm:")
user_goal = goal_list[input(f"Enter your goal \n {msg_goal}")]
user_activity = activity_list[input(f"Enter username \n {msg_activity}")]

user = {
    "name": user_name,
    "age": int(user_age),
    "gender": user_gender,
    "weight": int(user_weight),
    "height": int(user_height),
    "goal": user_goal,
    "activity": user_activity,
}

def result(data):
    print("calories " + str(data[0]))
    print("protein " + str(data[1]))
    print("carbohydrates " + str(data[2]))
    print("fat " + str(data[3]))


macros = cal_macros(user)
result(macros)
