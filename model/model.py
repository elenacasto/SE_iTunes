import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()

        self.albums = []
        self.mappa_id = {}
        self.connessioni = {}

        self.set_migliore = []

    def load_albums(self, min_duration):
        self.albums = DAO.getDurataAlbum(min_duration)
        for a in self.albums:
            self.mappa_id[a.id] = a

    def load_playlists(self):
        self.connessioni = DAO.getCoppieAlbum(self.albums)

    def build_graph(self):

        self.G.clear()
        self.G.add_nodes_from(self.albums)

        for i, a1 in enumerate(self.albums):
            for a2 in self.albums[i+1:]:
                if self.connessioni[a1] & self.connessioni[a2]:
                    self.G.add_edge(a1, a2)

    def analisi_componente(self, album):

        if album not in self.G:
            return []
        return list(nx.node_connected_component(self.G, album))

    def get_set_album(self, start_album, durata_max):
        componente = self.analisi_componente(start_album)
        self.set_migliore = []
        self._ricorsione(componente, [start_album], start_album.durata, durata_max)
        return self.set_migliore


    def _ricorsione(self, albums, current_set, current_durata, durata_max):
        if len(current_set) > len(self.set_migliore):
            self.set_migliore = current_set[:]

            for album in albums:
                if album in current_set:
                    continue
                nuova_durata = current_durata + album.durata
                if nuova_durata <= durata_max:
                    current_set.append(album)
                    self._ricorsione(albums, current_set, nuova_durata, durata_max)
                    current_set.pop()