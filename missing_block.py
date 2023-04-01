from abc import ABC

from robot import Robot


class MissingBlock(Robot, ABC):
    def __init__(self, default_config):
        super().__init__(default_config)

    def test_missing_block(self):
        ...
