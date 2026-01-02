import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()

        self.album = []
        self.mappa_id = {}
        self.connessioni = {}

    def load_albums(self, min_duration):
        self.album = DAO.getDurataAlbum(min_duration)
        for a in self.album:
            self.mappa_id[a.id] = a

    def load_playlists(self):
        self.connessioni = DAO.getCoppieAlbum()

    def build_graph(self):

        self.G.clear()
        self.G.add_nodes_from(self.album)

        for a1, a2 in self.connessioni:
            if a1 in self.G.nodes() and a2 in self.G.nodes():
                self.G.add_edge(a1, a2)


    def analisi_componente(self, album):

        if album not in self.G:
            return []
        return list(nx.node_connected_component(self.G, album))






