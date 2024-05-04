def cal_macros(user):
    print(user)
    bmr = 0
    tdee: int = 0
    activity_level = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extra Active": 1.9
    }
    goals = {
        "weight loss": [-250, {"carbohydrates": 0.4, "protein": 0.3, "fat": 0.3}],
        "extreme weight loss": [-500, {"carbohydrates": 0.3, "protein": 0.4, "fat": 0.3}],
        "maintenance": [0, {"carbohydrates": 0.5, "protein": 0.25, "fat": 0.25}],
        "muscle gain": [250, {"carbohydrates": 0.55, "protein": 0.2, "fat": 0.25}],
        "extreme muscle gain": [500, {"carbohydrates": 0.55, "protein": 0.2, "fat": 0.25}]
    }
    if user["gender"] == "male":
        bmr = int(88.362 + (13.397 * user["weight"]) + (4.799 * user["height"]) - (5.677 * user["age"]))
    else:
        bmr = int(447.593 + (9.247 * user["weight"]) + (3.098 * user["height"]) - (4.330 * user["age"]))

    for actv in activity_level:
        if user["activity"] == actv:
            tdee = int(bmr * activity_level[actv])
            break

    calories = tdee + goals[user["goal"]][0]
    protein = int((calories * goals[user["goal"]][1]["protein"]) / 4)
    carbohydrates = int((calories * goals[user["goal"]][1]["carbohydrates"]) / 4)
    fat = int((calories * goals[user["goal"]][1]["fat"]) / 9)
    return calories, protein, carbohydrates, fat
