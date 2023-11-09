import os
import sys

if 'foxbaja_telemetria.db' in os.listdir():
    print("\nERRO: base de dados ja existe, apague manualmente para continuar\n")
    sys.exit()

with sqlite3.connect('foxbaja_telemetria.db') as conn:
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS telemetria (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            velocidade INTEGER NOT NULL,
            temperatura INTEGER NOT NULL,
            rotacao INTEGER NOT NULL,
            combustivel INTEGER NOT NULL,
            freio INTEGER NOT NULL,
            timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """)
    c.execute(f"""
            INSERT INTO telemetria 
            (rotacao, velocidade, freio, combustivel, temperatura)
            VALUES
            (0, 0, 0, 0, 0)
            """)

    conn.commit()
