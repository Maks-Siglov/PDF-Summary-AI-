class ApplicationException(Exception):
    """
    Base class for application exceptions
    * all application exceptions must be derived from this class
    """


# File exc


class WrongFileFormatException(ApplicationException):
    pass


class TooLargeFileException(ApplicationException):
    pass


class EmptyFileException(ApplicationException):
    pass
