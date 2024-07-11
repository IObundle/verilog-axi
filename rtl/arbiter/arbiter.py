import os

# Find python modules
if __name__ == "__main__":
    import sys

    sys.path.append("./scripts")

from iob_module import iob_module


if __name__ == "__main__":
    iob_module.find_modules()


class arbiter(iob_module):
    @classmethod
    def _init_attributes(cls):
        """Init module attributes"""
        cls.name = "arbiter"
        cls.version = "V0.10"
        cls.setup_dir = os.path.dirname(__file__)
