import os
import sys
import json
from dotenv import load_dotenv
from curl_cffi import requests

load_dotenv()

def get_instagram_profile(username: str, proxy: str = None) -> dict:
    """
    Busca informacoes publicas de um perfil do Instagram.
    
    Args:
        username: Nome de usuario (com ou sem @)
        proxy: Proxy opcional (ex: http://user:pass@host:port)
    
    Returns:
        dict: Informacoes do perfil
    """
    username = username.strip().lstrip("@")
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "0",
        "x-asbd-id": "359341",
        "Referer": "https://www.instagram.com/",
        "sec-ch-ua": '"Not:A-Brand";v="8", "Chromium";v="134"',
        "sec-ch-ua-full-version-list": '"Not:A-Brand";v="8.0.0.0", "Chromium";v="134.0.0.0"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "priority": "u=1, i",
    }

    proxies = {"https": proxy, "http": proxy} if proxy else None

    response = requests.get(url, headers=headers, impersonate="chrome124", proxies=proxies)
    response.raise_for_status()

    user = response.json()["data"]["user"]

    return {
        "nome": user["full_name"],
        "username": user["username"],
        "bio": user["biography"],
        "site": user.get("external_url") or None,
        "seguidores": user["edge_followed_by"]["count"],
        "seguindo": user["edge_follow"]["count"],
        "posts": user["edge_owner_to_timeline_media"]["count"],
        "privado": user["is_private"],
        "verificado": user["is_verified"],
        "foto_url": user["profile_pic_url_hd"],
    }


def main():
    """Funcao principal com interface via terminal"""
    print("\nInstagram Profile Scraper")
    print("-" * 40)
    
    username = input("Digite o nome do usuario: ").strip()
    
    if not username:
        print("Erro: Nome de usuario nao informado")
        sys.exit(1)
    
    proxy = os.getenv("PROXY")
    
    if not proxy:
        usar_proxy = input("Usar proxy? (s/n): ").strip().lower()
        if usar_proxy == "s":
            proxy = input("Digite o proxy (ex: http://user:pass@host:port): ").strip()
    
    print("\nBuscando informacoes...")
    
    try:
        result = get_instagram_profile(username, proxy)
        print("\n" + json.dumps(result, ensure_ascii=False, indent=2))
    except requests.HTTPError as e:
        if e.response.status_code == 401:
            print("\nErro 401: Acesso negado pelo Instagram")
            print("Seu IP pode estar bloqueado. Tente usar um proxy.")
            print("\nPara configurar um proxy:")
            print("1. Copie o arquivo .env.example para .env")
            print("2. Adicione sua configuração de proxy no .env")
            print("3. Ou execute novamente e escolha 's' para usar proxy")
        else:
            print(f"\nErro HTTP: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nErro: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
