import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()

        self.album = {} #mappa_id

    def build_graph(self, d : int):

        self.G.clear()
        self.album = {}

        album = DAO.getSommaAlbum()
        for somma, album_id in album:
            minuti = somma // 60000
            self.album[album_id] = minuti

        for album_id, minuti in self.album.items():
            if minuti > d:
                self.G.add_node(album_id)

        for a1, a2 in DAO.getCoppieAlbum():
            if a1 in self.G and a2 in self.G:
                self.G.add_edge(a1, a2)

    def get_nodes(self):
        return self.G.number_of_nodes()

    def get_edges(self):
        return self.G.number_of_edges()



