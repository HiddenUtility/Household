from pathlib import Path
from config.data_direcotry_path import DataDirectoryPath
from config.finace_names import FainanceNames
from config.bank_names import BankNames
from config.card_names import CardNames

class MakingDirecotry:
    def __init__(self) -> None:
        pass
        
    def __mkdir(self, path: Path):
        if not path.exists():
            path.mkdir()

    def run(self):
        dirnames = [d.name for d in BankNames]
        dirnames += [d.name for d in CardNames]
        dirnames += [d.name for d in FainanceNames]
        dst:Path = DataDirectoryPath.DATA_PAH
        self.__mkdir(dst)
        [self.__mkdir(dst.joinpath(name)) for name in dirnames]
