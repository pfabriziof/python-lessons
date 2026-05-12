class InformalParserInterface:
    """This is an interface for other implementations"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Extract text from the current loaded file"""
        pass


class PdfParser(InformalParserInterface):
    """This is a concrete class to extract from PDF

    Here you'll implement your methods to extract text from PDF files.
    Right now is just an example, that's why is not implemented.
    """

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides the interface's method"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides the interface's method"""
        pass


class EmlParser(InformalParserInterface):
    """This is another concrete class to extract from Email"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides the interface's method"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides the interface's method"""
        pass


"""Metaclasses"""


class ParserMeta(type):
    """A Parser metaclass used to create the parser class"""
    def __instacecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, 'load_data_source') and
            callable(subclass.load_data_source) and
            hasattr
        )


class UpdateInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
