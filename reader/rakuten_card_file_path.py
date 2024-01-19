from pathlib import Path


class RakutenCardFilePath:
    __path : Path
    def __init__(self, path: Path) -> None:
        self.__path = path

    def __str__(self) -> str:
        return self.__path.name

    def __repr__(self) -> str:
        return str(self)

    def to_path(self) -> Path:
        return self.__path