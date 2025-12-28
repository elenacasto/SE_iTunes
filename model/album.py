from dataclasses import dataclass


@dataclass
class Album:
    id : int
    title : str
    artist_id : int


