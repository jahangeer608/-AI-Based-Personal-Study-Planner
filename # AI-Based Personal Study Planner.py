# AI-Based Personal Study Planner
# Programming for AI Lab Project

class StudyPlanner:
    def __init__(self):
        self.subjects = []

    def add_subject(self):
        n = int(input("Enter number of subjects: "))

        for i in range(n):
            print(f"\nSubject {i+1}")
            name = input("Subject Name: ")
            difficulty = int(input("Difficulty (1-10): "))
            exam_days = int(input("Days Left Until Exam: "))

            self.subjects.append({
                "name": name,
                "difficulty": difficulty,
                "exam_days": exam_days
            })

    def generate_plan(self):
        total_hours = int(input("\nAvailable Study Hours Per Day: "))

        # AI-inspired priority formula
        for subject in self.subjects:
            subject["priority"] = (
                subject["difficulty"] * 10
            ) / subject["exam_days"]

        self.subjects.sort(
            key=lambda x: x["priority"],
            reverse=True
        )

        total_priority = sum(
            s["priority"] for s in self.subjects
        )

        print("\n" + "="*50)
        print("      AI PERSONAL STUDY PLAN")
        print("="*50)

        for subject in self.subjects:
            allocated_hours = (
                subject["priority"] / total_priority
            ) * total_hours

            print(f"\nSubject: {subject['name']}")
            print(f"Priority Score: {subject['priority']:.2f}")
            print(f"Recommended Study Time: {allocated_hours:.1f} Hours")

        print("\nHighest Priority Subject:")
        print(self.subjects[0]["name"])

        print("\nKeep studying consistently. Good Luck!")
        print("="*50)


# Main Program
planner = StudyPlanner()

print("===================================")
print("   AI-Based Personal Study Planner ")
print("===================================")

planner.add_subject()
planner.generate_plan()
