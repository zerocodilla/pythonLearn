import user_management as UM, advanced_user_management as AUM

user_0 = UM.User('John', 'Meyer', '88', 'Singapore')
user_1 = UM.User('Vera', 'Meyer', '18', 'Moscow')
user_2 = UM.User('Lilly', 'Smith', '28', 'NY')
user_3 = UM.User('Viola', 'Smart', '21', 'London')
users = [user_3, user_2, user_1, user_0]

for user in users:
    user.describe_user()
    user.greet_user()
user_4 = UM.User('Viola', 'Smart', '21', 'London', 0)
user_4.describe_user()
user_4.increment_login_attempts(3)
user_4.describe_user()
user_4.increment_login_attempts(4)
user_4.describe_user()
user_4.reset_login_attempts()
user_4.describe_user()


admin = AUM.Admin('John', 'Smith', '41', 'London', 9,)
admin.describe_user()
admin.privileges.show_privileges()


my_admin = AUM.Admin('Justin', 'Case', '33', 'London', 9)
my_admin.privileges
my_admin.privileges.show_privileges()