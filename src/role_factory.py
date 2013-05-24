from role import *

class RoleFactory:
    def __init__(self):
        self.roles = []

        self.roles.append(RoleComponent('Space Knight', 'Excelling in hand to hand combat, the space knight gets up close and personal with its enemies'))
        self.roles.append(RoleComponent('Laser Jockey', 'The LJs love nothing more than loading up their favourite blaster and nailing enemies from a distance'))
        self.roles.append(RoleComponent('Psypath', 'A mystic warrior, employing the skills of the mind to manipulate its enemies and surroundings'))

    def get_role(self, name):
        found = [role for role in self.roles if role.role == name]
        if len(found) > 1:
            raise Exception('RaceFactory.get_race: Found duplicate races')
        if len(found) < 1:
            return None

        return found[0]

        
