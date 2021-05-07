from pypresence import Presence
import time
start_time = int(time.time())
client_id = '{APPLICATION ID}'
RPC = Presence(client_id)
RPC.connect()
while True:
  RPC.update(state='{descrição}',
           details="{detalhes}",
           large_image="{opcional}",
           large_text="{texto da imagem grande}",
           small_image="{opcional, pequena}",
           small_text="{texto da imagem pequena}",
           start=start_time,
           buttons=[{"label": "Perfil", "url": "https://github.com/{perfil}"}]
           )