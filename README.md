## ⚠️ Aviso Legal

Este projeto é **apenas para fins educacionais e de pesquisa**. O uso inadequado pode violar os termos de serviço do Instagram. Respeite os limites de taxa (rate limits) e utilize proxies quando necessário. O autor não se responsabiliza por mau uso da ferramenta.

## Funcionalidades

- Extrai dados públicos de qualquer perfil do Instagram
- Não requer login ou autenticação
- Suporte a proxy para contornar bloqueios de IP
- Retorna dados em formato JSON

## Dados Extraídos

| Campo | Descrição |
|-------|-----------|
| nome | Nome completo do perfil |
| username | Nome de usuário |
| bio | Biografia do perfil |
| site | Site externo (se houver) |
| seguidores | Número de seguidores |
| seguindo | Número de contas seguidas |
| posts | Número de publicações |
| privado | Status do perfil (true/false) |
| verificado | Status de verificação (true/false) |
| foto_url | URL da foto de perfil |

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/mathias-ctrl/instagram-profile-scraper.git
cd instagram-profile-scraper
```

2. Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o proxy (opcional):
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações de proxy
```

## Como Usar

### Uso Básico

Execute o script e digite o nome do usuário quando solicitado:

```bash
python scraper.py
```

### Exemplo de Execução

```
Instagram Profile Scraper
----------------------------------------
Digite o nome do usuario: deliciasdathaioficial
Usar proxy? (s/n): n

Buscando informacoes...

{
  "nome": "Delicias da Thai - Pudim Gourmet",
  "username": "deliciasdathaioficial",
  "bio": "Pudim artesanal feito com muito carinho",
  "site": null,
  "seguidores": 537,
  "seguindo": 153,
  "posts": 19,
  "privado": false,
  "verificado": false,
  "foto_url": "https://..."
}
```

### Usando Proxy

O script oferece duas formas de configurar proxy:

**Opção 1: Arquivo .env**
```bash
# Edite o arquivo .env
PROXY=http://usuario:senha@host:porta
```
Então execute o script normalmente:
```bash
python scraper.py
```

**Opção 2: Durante a execução**
```bash
python scraper.py
# Quando perguntado, digite 's' e informe o proxy
```

## Erro 401 - Acesso Negado

Se você receber o erro `HTTP Error 401`, significa que seu IP foi temporariamente bloqueado pelo Instagram. Isso ocorre quando muitas requisições são feitas em pouco tempo.

### Serviços de Proxy Gratuitos

- [Webshare.io](https://www.webshare.io/) - Oferece 10 proxies gratuitos

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
