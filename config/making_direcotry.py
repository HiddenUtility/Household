from enum import Enum, auto
from pathlib import Path

class DataDirecotryNames(Enum):
    EPOS_CARD = auto()
    JA_CARD = auto()
    RAKUTEN_BANK = auto()
    RAKUTEN_CRAD = auto()
    RAKUTEN_FINANCE = auto()
    UFJ_BANK = auto()
    TOYOTA_CARD = auto()


class MakingDirecotry:
    def __init__(self) -> None:
        pass
        
    def __mkdir(self, path: Path):
        if not path.exists():
            path.mkdir()

    def run(self):
        dirnames = [d.name for d in DataDirecotryNames]
        dst = Path("./data")
        self.__mkdir(dst)
        [self.__mkdir(dst.joinpath(name)) for name in dirnames]
