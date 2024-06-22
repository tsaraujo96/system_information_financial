from datetime import datetime

import pandas as pd
import requests


class OptionRepository:
    def get_all_opcoes(self, ativo_objeto) -> pd.DataFrame:
        url = f"https://opcoes.net.br/listaopcoes/completa?&idAcao={ativo_objeto}&listarVencimentos=true&cotacoes=true"
        r = requests.get(url).json()
        vencimentos = [i["value"] for i in r["data"]["vencimentos"]]

        if vencimentos:
            df_completo = pd.concat([self._build_table(ativo_objeto, vencimento) for vencimento in vencimentos])
            self._treating_dataframe(df_completo)

        else:
            df_completo = pd.DataFrame()
        return df_completo

    def _build_table(self, ativo_objeto, vencimento) -> pd.DataFrame:
        url = (
            f"https://opcoes.net.br/listaopcoes/completa?idLista="
            f"ML&idAcao={ativo_objeto}&listarVencimentos=false&cotacoes=true&vencimentos={vencimento}"
        )

        r = requests.get(url).json()
        preco_acao = self._get_header(ativo_objeto)
        tabela = [
            [
                ativo_objeto,
                vencimento,
                i[0].split("_")[0],
                i[2],
                i[3],
                i[5],
                preco_acao,
                i[8],
                i[9],
                i[10],
                i[11],
                datetime.strptime(vencimento, "%Y-%m-%d").date() - datetime.now().date(),
            ]
            for i in r["data"]["cotacoesOpcoes"]
        ]
        return pd.DataFrame(
            tabela,
            columns=[
                "ativo_objeto",
                "vencimento",
                "opcao",
                "tipo",
                "modelo",
                "strike",
                "preço_acao",
                "preco_opcao",
                "vol. qt",
                "vol. fin",
                "data_de_fechamento",
                "dias_faltantes",
            ],
        )

    @staticmethod
    def _get_header(ativo_objeto) -> float:
        url = f"https://opcoes.net.br/cotacoes?ativos={ativo_objeto}"
        r = requests.get(url).json()
        preco_acao = r["data"][ativo_objeto]["ULT"]
        return preco_acao

    @staticmethod
    def _treating_dataframe(df: pd.DataFrame):
        df.dropna(how="any", axis=0, inplace=True)
        df.reset_index(drop=True, inplace=True)
