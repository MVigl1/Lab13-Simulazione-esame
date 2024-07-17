import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._stati = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._stati)
        self._idMap = {}
        for v in self._stati:
            self._idMap[v.id] = v


    def getYears(self):
        return DAO.getYears()

    def setShape(self, anno):
        return DAO.setShape(anno)

    def creaGrafo(self, anno, forma):
        result = []
        self.addEdges(anno, forma)
        print(self._grafo)
        sum=0
        for stato in self._stati:
            sum = self.getPesiAdiacenti(stato)
            print(f'Nodo {stato}: {sum}')
            result.append((stato,sum))

    def addEdges(self, anno, forma):
        for stato in self._stati:
            if (stato.Neighbors is not None):
                listConfini = stato.Neighbors.split()
                for confine in listConfini:
                    weight = self.calcolaPeso(stato, confine, anno, forma)
                    self._grafo.add_edge(stato, self._idMap[confine], weight=weight)

    def calcolaPeso(self, stato1, stato2, anno, forma):
        return DAO.getPeso(stato1, stato2, anno, forma)

    def getPesiAdiacenti(self, stato):
        sum = 0
        for stato1 in self._stati:
            if(self._grafo.has_edge(stato, stato1)):
                sum += int(self._grafo[stato][stato1]['weight'])
        return sum
