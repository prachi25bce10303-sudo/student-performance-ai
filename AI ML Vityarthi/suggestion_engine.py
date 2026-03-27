def give_suggestions(data, predicted_score):
    suggestions = []

    if data["attendance"] < 70:
        suggestions.append("Improve attendance")

    if data["study_hours"] < 2:
        suggestions.append("Increase study hours")

    if data["sleep"] < 6:
        suggestions.append("Get more sleep")

    if data["screen_time"] > 5:
        suggestions.append("Reduce screen time")

    if data["stress"] > 7:
        suggestions.append("Manage stress better")

    if predicted_score >= 80:
        suggestions.append("Try advanced topics and challenges")

    return suggestions


def generate_study_plan(predicted_score):
    if predicted_score < 60:
        return [
            "Day 1-2: Revise basics",
            "Day 3-4: Practice questions",
            "Day 5-6: Mock tests",
            "Day 7: Review mistakes"
        ]
    elif predicted_score < 80:
        return [
            "Day 1-2: Strengthen concepts",
            "Day 3-5: Practice problems",
            "Day 6: Mock test",
            "Day 7: Analyze performance"
        ]
    else:
        return [
            "Day 1-3: Advanced topics",
            "Day 4-6: Projects/practice",
            "Day 7: Revision"
        ]
def get_grade(score):
     if score >= 85:
        return "A"
     elif score >= 70:
        return "B"
     elif score >= 50:
         return "C"
     else:
        return "F"


def get_result(score):
    if score >= 40:
        return "Pass"
    else:
        return "Fail"