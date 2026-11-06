import time
import requests

# --- I TUOI DATI TELEGRAM CONFERMATI ---
TOKEN_TELEGRAM = "9092558730:AAG_JNLi-i-Kz3GBFoOuLMG7apP_xU1cpDs"
ID_CHAT_TELEGRAM = "8692534224"

def genera_report(novita, rimossi):
    orario = time.strftime("%Y-%m-%d %H:%M:%S")
    messaggio = f"🔔 <b>AGGIORNAMENTO PUC ({orario})</b>\n\n"
    scritto = False
    
    if novita:
        scritto = True
        messaggio += "➕ <b>NUOVI TORNEI:</b>\n"
        for n in novita:
            messaggio += f"• {n}\n"
            
    if rimossi:
        scritto = True
        messaggio += "\n➖ <b>TORNEI RIMOSSI:</b>\n"
        for r in rimossi:
            messaggio += f"• {r}\n"
            
    if scritto:
        try:
            url_tg = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
            payload = {
                "chat_id": ID_CHAT_TELEGRAM,
                "text": messaggio,
                "parse_mode": "HTML"
            }
            requests.post(url_tg, json=payload, timeout=15)
        except Exception:
            pass

# Ciclo automatico per il cloud
if __name__ == "__main__":
    while True:
        try:
            print("Controllo tornei FIT avviato sul cloud...")
            # Qui si attiverà il controllo reale dei tornei del portale
        except Exception:
            pass
            
        # Aspetta 1 ora (3600 secondi) prima di fare il prossimo controllo
        time.sleep(3600)
