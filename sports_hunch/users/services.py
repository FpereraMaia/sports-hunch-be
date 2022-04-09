from users.models import User


class UserService:
    @staticmethod
    def create(name, email):
        user = UserService.assemble(name, email)
        user.save()
        return user

    @staticmethod
    def assemble(name, email):
        try:
            user = User.objects.get(email__icontains=email)
        except User.DoesNotExist:
            user = User()
            user.email = email

        user.name = name
        return user
