import code
import heapq
def main():
    InputData = LoadInputData()
    OutputData = ArvoreDeBusca(InputData)
    ReturnOutputData(OutputData)
    code.interact(local=locals())

def SelecionadorTipoBusca():
    flag = False
    OpcoesValidas = [1, 2, 3, 4]
    while flag == False:
        TipoBusca = int(input(" \n Selecione 1 caso queira utilizar Árvore de Busca Geral \n" \
        "2 para Busca em Largura \n" \
        "3 para Busca Uniforme \n" \
        "4 para Busca em Profundidade \n"))
        if TipoBusca in OpcoesValidas:
            flag = True
    return TipoBusca

def LoadInputData():
    InputData = DataStorageClass('Input Data')
    InputData.TipoBusca = SelecionadorTipoBusca()
    if (InputData.TipoBusca == 1) or (InputData.TipoBusca == 2) or (InputData.TipoBusca == 4):
        InputData.Grafo = {'A': ['B', 'C', 'D', 'E'],
                        'B': ['A', 'C'],
                        'C': ['A', 'B', 'E'],
                        'D': ['A', 'E', 'F'],
                        'E': ['A', 'C', 'D', 'F'],
                        'F': ['D', 'E']
                        }
    elif (InputData.TipoBusca == 3):
        InputData.Grafo = {     'A': {'B': 2, 'C': 5, 'D': 3, 'E': 6},
                                'B': {'A': 2, 'C': 4},
                                'C': {'A': 5, 'B': 4, 'E': 2},
                                'D': {'A': 3, 'E': 1, 'F': 5},
                                'E': {'A': 6, 'C': 2, 'D': 1,'F': 3},
                                'F': {'D': 5, 'E': 3}
                                }
    InputData.NoRaiz = input("\n Digite o estado inicial: ").upper()
    InputData.NoObjetivo = input("\n Digite o estado objetivo: ").upper()
    return InputData

def ArvoreDeBusca(InputData):
    OutputData = DataStorageClass('Output Data')
    OutputData.TipoBusca = InputData.TipoBusca
    LocalData = DataStorageClass('Local Data')
    LocalData.Arvore = []
    LocalData.Fronteira = []
    LocalData.Explorado = []

    if (InputData.TipoBusca == 1) or (InputData.TipoBusca == 2) or (InputData.TipoBusca == 4):
        LocalData.Fronteira.append([InputData.NoRaiz])
    elif (InputData.TipoBusca == 3):
        heapq.heappush(LocalData.Fronteira, (0, [InputData.NoRaiz]))

    while LocalData.Fronteira:
        if (InputData.TipoBusca == 1) or (InputData.TipoBusca == 2) or (InputData.TipoBusca == 4):
            LocalData.CaminhoAtual = LocalData.Fronteira.pop(0)
        elif (InputData.TipoBusca == 3):
            LocalData.CustoAtual, LocalData.CaminhoAtual = heapq.heappop(LocalData.Fronteira)

        LocalData.NoAtual = LocalData.CaminhoAtual[-1]
        LocalData.Arvore.append(LocalData.CaminhoAtual)

        if LocalData.NoAtual == InputData.NoObjetivo:
            OutputData.Nome = LocalData.nome
            OutputData.Caminho = LocalData.CaminhoAtual
            OutputData.Arvore = LocalData.Arvore
            OutputData.Explorado = LocalData.Explorado
            if (InputData.TipoBusca == 3):
                OutputData.Custo = LocalData.CustoAtual

            return OutputData

        if LocalData.NoAtual not in LocalData.Explorado:
            LocalData.Explorado.append(LocalData.NoAtual)
            if InputData.TipoBusca == 1:
                LocalData.nome = "Árvore Geral"
                LocalData = BuscaGeral(InputData, LocalData)
            elif (InputData.TipoBusca == 2) or (InputData.TipoBusca == 4):
                LocalData = BuscaEmLarguraOuProfundidade(InputData, LocalData)
            elif (InputData.TipoBusca == 3):
                LocalData = BuscaUniforme(InputData, LocalData)
                    
    OutputData.Nome = LocalData.nome
    OutputData.Caminho = None
    if (InputData.TipoBusca == 3):
        OutputData.Custo = None
    OutputData.Explorado = LocalData.Explorado
    OutputData.Arvore = LocalData.Arvore
    return OutputData

def BuscaGeral(InputData, LocalData):
    LocalData.NovoCaminho = []
    LocalData.nome = "Árvore Geral"
    for vizinhos in InputData.Grafo[LocalData.NoAtual]:
        if vizinhos not in LocalData.CaminhoAtual:
            LocalData.NovoCaminho = LocalData.CaminhoAtual + [vizinhos]
            LocalData.Fronteira.append(LocalData.NovoCaminho)
    return LocalData

def BuscaEmLarguraOuProfundidade(InputData, LocalData):
    LocalData.NovoCaminho = []
    if (InputData.TipoBusca == 2):
        LocalData.nome = "Busca em Largura"
        for vizinhos in InputData.Grafo[LocalData.NoAtual]:
            if vizinhos not in LocalData.Explorado:
                LocalData.NovoCaminho = LocalData.CaminhoAtual + [vizinhos]
                LocalData.Fronteira.append(LocalData.NovoCaminho)
    elif (InputData.TipoBusca == 4):
        LocalData.nome = "Busca em Profundidade"
        for vizinhos in reversed(InputData.Grafo[LocalData.NoAtual]):
            if vizinhos not in LocalData.Explorado:
                LocalData.NovoCaminho = LocalData.CaminhoAtual + [vizinhos]
                LocalData.Fronteira.append(LocalData.NovoCaminho)
    return LocalData

def BuscaUniforme(InputData, LocalData):
    LocalData.nome = "Busca em Uniforme"
    for vizinhos, Custo in InputData.Grafo[LocalData.NoAtual].items():
        if vizinhos not in LocalData.Explorado:
            LocalData.NovoCaminho = LocalData.CaminhoAtual + [vizinhos]
            LocalData.NovoCusto = LocalData.CustoAtual + Custo
            heapq.heappush(LocalData.Fronteira, (LocalData.NovoCusto, LocalData.NovoCaminho))
    return LocalData

def ReturnOutputData(OutputData):
    print("\n Cominho Encontrado: ")
    print(OutputData.Caminho)
    if OutputData.TipoBusca == 3:
        print("\nCusto total:")
        print(OutputData.Custo)

    print("\n Árvore Gerada: ")
    for ramos in OutputData.Arvore:
        print(ramos)

    return OutputData

class DataStorageClass:
    def __init__(self, Name):
        self.Name = Name
    def __repr__(self):
        return f"{self.__dict__}"
    def as_list(self):
        return list(self.__dict__.values())
    def __str__(self):
        return str(self.__dict__)

main()