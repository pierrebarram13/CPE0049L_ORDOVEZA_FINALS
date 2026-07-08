from auth_service import AuthService
from library_service import LibraryService

class ServiceFactory:

    @staticmethod
    def get_service(name):

        if name == "auth":
            return AuthService()

        if name == "library":
            return LibraryService()

        raise ValueError("Unknown service")