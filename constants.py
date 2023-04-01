from enum import unique, IntEnum, Enum


@unique
class TaskUrl(Enum):
    """
    example url
    """
    slove_right = 'https://www.12306.cn/index/'
    missing_block = 'https://www.processon.com/'


@unique
class TestType(IntEnum):
    slove_right = 1
    missing_block = 2
