from typing import Dict

from entidades.posicao import Posicao


class ValidadorJson:
    def __init__(self, json_resposta: Dict):
        self.json_resposta = json_resposta

    def validar_json_parada(self):
        endereco_localizacao = self.json_resposta['ed'] if self.json_resposta.get('ed') is not None else None
        codigo_parada = self.json_resposta['cp'] if self.json_resposta.get('cp') is not None else None
        nome_parada = self.json_resposta['np'] if self.json_resposta.get('np') is not None else None
        posicao = Posicao(self.json_resposta['py'], self.json_resposta['px'])
        return endereco_localizacao, codigo_parada, nome_parada, posicao

    def validar_json_onibus(self):
        acessibiliade = self.json_resposta['a']
        prefixo = self.json_resposta['p']
        posicao = Posicao(self.json_resposta['py'], self.json_resposta['px'])
        return acessibiliade, prefixo, posicao

    def validar_json_linha(self):
        codigo_identificador = self.json_resposta['cl'] if self.json_resposta.get('cl') is not None else None
        modo_circular = self.json_resposta['lc'] if self.json_resposta.get('lc') is not None else None
        letreiro_numerico = self.json_resposta['lt'] if self.json_resposta.get('lt') is not None else None
        letreiro_numerico_segunda_parte = self.json_resposta['tl'] if self.json_resposta.get('tl') is not None else None
        sentido_linha = self.json_resposta['sl'] if self.json_resposta.get('sl') is not None else None
        terminal_principal = self.json_resposta['tp'] if self.json_resposta.get('tp') is not None else None
        terminal_secundario = self.json_resposta['ts'] if self.json_resposta.get('ts') is not None else None
        return codigo_identificador, modo_circular, letreiro_numerico, letreiro_numerico_segunda_parte, sentido_linha, \
            terminal_principal, terminal_secundario
