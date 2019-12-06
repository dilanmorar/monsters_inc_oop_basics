class Monster():
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def add_skills(self, skill):
        chosen_monster = self
        chosen_monster.skills.append(skill)

# self.skills[]
# def add_skills(self,skill)
# self.skills.append(skill)