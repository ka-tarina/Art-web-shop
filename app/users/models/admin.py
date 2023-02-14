from user import User, UserRole


class Admin(User):
    """A class representig an admin in the system."""
    __tablename__ = "admins"

    def __init__(self, name, email, password, status):
        """Initiallizes a new Admin object."""
        super().__init__(name=name, email=email, password=password, role=UserRole.ADMIN, status=status)
