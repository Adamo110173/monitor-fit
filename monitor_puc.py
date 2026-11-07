import os
import sys
import time
import requests
from dotenv import load_dotenv

load_dotenv("C:/Users/ADAMO/Desktop/monitor-fit/.env")
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def genera_report(novita, rimossi):
    orario = time.strftime("%Y-%m-%d %H:%M:%S")
    ID_CHAT_TELEGRAM = "8692534224"
    
    messaggio = f"🔔 <b>AGGIORNAMENTO PUC DEL {orario}</b>\n\n"
    scritto = False 
    
    if novita:
        messaggio += "+ <b>NUOVI TORNEI:</b>\n"
        for n in novita:
            messaggio += f"• {n}\n"
            
    if rimossi:
        messaggio += "\n- <b>TORNEI RIMOSSI:</b>\n"
        for r in rimossi:
            messaggio += f"• {r}\n"

    try:
        with open("C:/Users/ADAMO/Desktop/monitor-fit/report_tornei.txt", "a", encoding="utf-8") as f:
            f.write(f"\n=== AGGIORNAMENTO PUC DEL {orario} ===\n")
            if novita:
                f.write(f"NUOVI:\n{str(novita)}\n")
            if rimossi:
                f.write(f"RIMOSSI:\n{str(rimossi)}\n")
    except Exception:
        pass

    if scritto:
        try:
            url_tg = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            payload = {
                "chat_id": ID_CHAT_TELEGRAM,
                "text": messaggio,
                "parse_mode": "HTML"
            }
            risposta = requests.post(url_tg, json=payload, timeout=10)
            
            if risposta.status_code != 200:
                print(f"Telegram ha rifiutato il messaggio. Errore: {risposta.text}")
            else:
                print("Messaggio inviato a Telegram con successo!")
        except Exception as e:
            print(f"Errore invio Telegram: {e}")

genera_report([], [])
sys.exit(0)
