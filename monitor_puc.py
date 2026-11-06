import time
import requests

def genera_report(novita, rimossi):
    orario = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # --- I TUOI DATI TELEGRAM ---
    TOKEN_TELEGRAM = "9092558730:AAG_JNLi-i-Kz3GBFoOuLMG7apP_xU1cpDs"
    ID_CHAT_TELEGRAM = "8692534224"
    
    # Prepariamo il testo del messaggio in formato HTML
    messaggio = f"🔔 <b>AGGIORNAMENTO PUC ({orario})</b>\n\n"
    scritto = False  # 
    
    if novita:
        messaggio += "➕ <b>NUOVI TORNEI:</b>\n"
        for n in novita:
            messaggio += f"• {n}\n"
            
    if rimossi:
        messaggio += "\n➖ <b>TORNEI RIMOSSI:</b>\n"
        for r in rimossi:
            messaggio += f"• {r}\n"
            
    # Salva comunque il file sul desktop per storico
    try:
        with open("report_tornei.txt", "a", encoding="utf-8") as f:
            f.write(f"\n=== AGGIORNAMENTO PUC DEL {orario} ===\n")
            if novita:
                f.write(f"NUOVI:\n{str(novita)}\n")
            if rimossi:
                f.write(f"RIMOSSI:\n{str(rimossi)}\n")
    except Exception:
        pass
            
    # Blocco invio Telegram
    if scritto:
        try:
            url_tg = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
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
            if __name__ == "__main__":
    while True:
        try:
            # Sostituisci la riga qui sotto con il comando esatto 
            # che usava il tuo vecchio script per controllare i tornei
            print("Controllo tornei FIT avviato sul cloud...")
        except Exception as e:
            print(f"Errore nel ciclo continuo: {e}")
            
        # Aspetta 1 ora (3600 secondi) prima di fare il prossimo controllo
        time.sleep(3600)
