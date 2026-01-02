import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        try:
            min_durata = int(self._view.txt_durata.value)
        except ValueError:
            self._view.show_alert("Numero non valido!")
            return

        self._model.load_albums(min_durata)
        self._model.load_playlists()
        self._model.build_graph()

        self._view.dd_album.options = [ft.dropdown.Option(a.title) for a in self._model.album]

        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Grafo creato: {len(self._model.G.nodes)} album, {len(self._model.G.edges)} archi")
        )

        self._view.update()

    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        title = e.control.value
        self._selected_album = next((a for a in self._model.album if a.title == title), None)


    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        if not self._selected_album:
            self._view.show_alert("Selezionare un album")
            return

        componente = self._model.analisi_componente(self._selected_album)
        durata_tot = sum(a.durata for a in componente)

        self._view.lista_visualizzazione_2.controls.clear()
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f"Dimensione componente: {len(componente)}")
        )
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f"Durata totale: {durata_tot:.22f} minuti")
        )

        self._view.update()

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO