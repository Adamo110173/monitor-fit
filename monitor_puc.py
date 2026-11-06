import time
import requests

# Dati Telegram confermati
TOKEN_TELEGRAM = "9092558730:AAG_JNLi-i-Kz3GBFoOuLMG7apP_xU1cpDs"
ID_CHAT_TELEGRAM = "8692534224"

# PROVA DI INVIO FORZATA ALL'AVVIO
try:
    url_test = f"https://telegram.org{TOKEN_TELEGRAM}/sendMessage"
    payload_test = {"chat_id": ID_CHAT_TELEGRAM, "text": "🚀 SERVER CLOUD RENDER ATTIVO E FUNZIONANTE!"}
    requests.post(url_test, json=payload_test, timeout=15)
except Exception:
    pass

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
            url_tg = f"https://telegram.org{TOKEN_TELEGRAM}/sendMessage"
            payload = {
                "chat_id": ID_CHAT_TELEGRAM,
                "text": messaggio,
                "parse_mode": "HTML"
            }
            requests.post(url_tg, json=payload, timeout=15)
        except Exception:
            pass

if __name__ == "__main__":
    while True:
        try:
            print("Controllo tornei FIT avviato sul cloud...")
            # Qui andrà inserito il comando per il controllo reale dei tornei
        except Exception:
            pass
            
        # Aspetta 1 ora (3600 secondi) prima di fare il prossimo controllo
        time.sleep(3600)
