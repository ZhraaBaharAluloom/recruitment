def get_skills():
    # Add at least 3 random skills for the user to select from
    return ["JavaScript", "ReactJS", "TypeScript", "Python", "HTML"]


def show_skills(skills):
    # Pretty print skills to the user

    # Write your code here
    for index, item in enumerate(skills, 1):
        print(f'{index}: {item}')


def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    show_skills(skills)
    skill1 = int(input("Pick a skill from the above skills: "))
    skill2 = int(input("Pick a skill from the above skills: "))
    skills = [skills[skill1 - 1], skills[skill2 - 1]]
    return skills


def get_user_cv(skills):
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    years = int(input("Enter your years of experience : "))
    cv = {"name": name, "age": age, "experience": years,
          "skills": get_user_skills(skills)}

    return cv


def check_acceptance(cv, desire_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    print(desire_skill)
    if 25 < cv["age"] < 40 and cv["experience"] > 3 and desire_skill in cv["skills"]:
        return True


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    skills = get_skills()
    cvv = get_user_cv(skills)

    if check_acceptance(cvv, skills[2]):
        print("alf alf mabrook")
    else:
        print("ya 3ami 6eeer")
    ...


if __name__ == "__main__":
    main()
