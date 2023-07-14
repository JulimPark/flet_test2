import flet as ft

import os
from supabase import create_client, Client


def main(page: ft.Page):
    
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    
    aa = ft.Text('안녕하세요')
    page.add(aa)
    pass

ft.app(target=main)
