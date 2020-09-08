class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    # create the method
    def __add__(self, other):
        """Addition of tasks."""
        desc = '\n'.join([self.description, other.description])
        teams = ', '.join([self.team, other.team])
        return Task(desc, teams)