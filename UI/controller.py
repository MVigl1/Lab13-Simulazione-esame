import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        anni = self._model.getYears()
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(anno))

    def fillDDshape(self):
        self._view.ddshape.options = []
        if self._view.ddyear is not None:
            anno = self._view.ddyear.value
            shapes = self._model.setShape(anno)
            for shape in shapes:
                if shape != "":
                    self._view.ddshape.options.append(ft.dropdown.Option(shape))
            self._view.update_page()

        else:
            pass


    def handle_graph(self, e):
        if self._view.ddyear is not None and self._view.ddshape is not None:
            anno = self._view.ddyear.value
            forma = self._view.ddshape.value
            self._model.creaGrafo(anno, forma)


    def handle_path(self, e):
        pass