import json
from produto import Produto


def salvar(produtos, arquivo="dados.json"):
    dados = [p.to_dict() for p in produtos]

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar(arquivo="dados.json"):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        return [Produto.from_dict(item) for item in dados]

    except FileNotFoundError:
        return []