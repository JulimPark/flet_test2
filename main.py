import flet as ft

import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def main(page: ft.Page):
    aa = ft.Text('안녕하세요')
    page.add(aa)
    pass

ft.app(target=main)
