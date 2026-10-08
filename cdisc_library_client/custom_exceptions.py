
class ResourceNotFoundException(Exception):
    status_code = 404

class LibraryAccessError(Exception):
    status_code = 401