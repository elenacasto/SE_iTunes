from dataclasses import dataclass

@dataclass
class Track:
        id: int
        name: str
        album_id: int
        media_type_id: int
        genre_id: int
        composer : str
        milliseconds : int
        bytes : int
        unit_price : float


