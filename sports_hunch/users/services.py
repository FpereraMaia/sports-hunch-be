from users.models import User


class UserService:
    @staticmethod
    def create(email, name):
        user = UserService.assemble(email, name)
        user.save()
        return user

    @staticmethod
    def assemble(email, name):
        try:
            user = User.objects.get(email__icontains=email)
        except User.DoesNotExist:
            user = User()
            user.email = email

        user.name = name
        return user
