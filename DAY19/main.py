import utils


class UsersPermissions:

    def __init__(self, permissions):
        self.__permissions = permissions

    @property
    def permissions(self):
        return self.__permissions

    def output(self):
        return f"{self.permissions}"

    def __repr__(self):
        return f"permission | {self.permissions}"


class Users(UsersPermissions):
    def __init__(self, user, permissions):
        super().__init__(permissions)
        self.__user = user

    @property
    def user(self):
        return self.__user

    def output(self):
        return f"{self.user} | {self.permissions}"



def generator():
    for user in utils.users.items():
        yield user


def menu():
    while True:
        print("Users:")
        for id, name in generator():
            print(f'{id} {utils.colors.get("BLUE")}{name}{utils.colors.get("RESET")}')
        def choice():
            permission_asc = int(input("Enter the user ID from the list: "))
            asc = input("Enable Administrator Privileges? ON | OFF: ").upper()
            if asc == 'ON':
                utils.users[permission_asc]['switch']|= 0b001
            elif asc == 'OFF':
                utils.users[permission_asc]['switch']|= 0b000
            return permission_asc, asc
        permission_asc, asc = choice()
        user_permissions = Users(utils.users[permission_asc], asc)
        print(user_permissions.output())
if __name__ == "__main__":

    menu()