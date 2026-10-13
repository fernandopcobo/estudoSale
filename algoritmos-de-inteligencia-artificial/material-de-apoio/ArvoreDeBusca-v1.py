import code
def main():
    InputData = LoadInputData()
    OutputData = ArvoreDeBusca(InputData)
    ReturnOutputData(OutputData)
#    code.interact(local=locals())

def SelecionadorTipoBusca():
    flag = False
    OpcoesValidas = [1, 2]
    while flag == False:
        TipoBusca = int(input(" \n Selecione 1 caso queira utilizar Árvore de Busca Geral ou 2 para Busca em Largura: "))
        if TipoBusca in OpcoesValidas:
            flag = True
    return TipoBusca

def LoadInputData():
    InputData = DataStorageClass('Input Data')
    InputData.TipoBusca = SelecionadorTipoBusca()
    InputData.Grafo = {'A': ['B', 'C', 'D', 'E'],
                       'B': ['A', 'C'],
                       'C': ['A', 'B', 'E'],
                       'D': ['A', 'E', 'F'],
                       'E': ['A', 'C', 'D', 'F'],
                       'F': ['D', 'E']
                       }
    InputData.NoRaiz = input("\n Digite o estado inicial: ").upper()
    InputData.NoObjetivo = input("\n Digite o estado objetivo: ").upper()
    return InputData

def ArvoreDeBusca(InputData):
    OutputData = DataStorageClass('Output Data')
    Arvore = []
    Fronteira = []
    Fronteira.append([InputData.NoRaiz])
    Explorado = []

    while Fronteira:
        CaminhoAtual = Fronteira.pop(0)
        NoAtual = CaminhoAtual[-1]
        Arvore.append(CaminhoAtual)

        if NoAtual == InputData.NoObjetivo:
            OutputData.Caminho = CaminhoAtual
            OutputData.Arvore = Arvore
            return OutputData

        if NoAtual not in Explorado:
            Explorado.append(NoAtual)
            for vizinhos in InputData.Grafo[NoAtual]:
                if InputData.TipoBusca == 1:
                    (CaminhoAtual, Fronteira, NovoCaminho) = BuscaGeral(vizinhos, CaminhoAtual, Fronteira)
                    OutputData.TipoDeBusca = "Árvore Geral"
                elif InputData.TipoBusca == 2:
                    (CaminhoAtual, Fronteira, NovoCaminho, Explorado) = BuscaEmLargura(vizinhos, CaminhoAtual, Fronteira, Explorado)
                    OutputData.TipoDeBusca = "Busca em Largura"
                            
    OutputData.Caminho = None
    OutputData.Arvore = Arvore
    return OutputData

def BuscaGeral(vizinhos, CaminhoAtual, Fronteira):
    NovoCaminho = []
    if vizinhos not in CaminhoAtual:
        NovoCaminho = CaminhoAtual + [vizinhos]
        Fronteira.append(NovoCaminho)
    return [CaminhoAtual, Fronteira, NovoCaminho]

def BuscaEmLargura(vizinhos, CaminhoAtual, Fronteira, Explorado):
    NovoCaminho = []
    if vizinhos not in Explorado:
        NovoCaminho = CaminhoAtual + [vizinhos]
        Fronteira.append(NovoCaminho)
    return [CaminhoAtual, Fronteira, NovoCaminho, Explorado]

def ReturnOutputData(OutputData):
    print("\n Cominho Encontrado: ")
    print(OutputData.Caminho)
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