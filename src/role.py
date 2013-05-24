class RoleComponent():
    def __init__(self, role, description):
        self.role = role
        self.description = description

        self.name = 'role'

    def __str__(self):
        return self.role
