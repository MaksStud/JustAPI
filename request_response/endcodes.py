from enum import StrEnum


class TextEncoding(StrEnum):
    """
    Common text encodings for files and HTTP headers
    """
    UTF_8 = 'utf-8'
    UTF_16 = 'utf-16'
    ASCII = 'ascii'
    LATIN_1 = 'latin-1'
    WINDOWS_1251 = 'windows-1251' 
    WINDOWS_1252 = 'windows-1252' 
    CP1251 = 'cp1251' 
