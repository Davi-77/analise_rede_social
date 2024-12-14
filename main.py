import instaloader
from dotenv import load_dotenv
import os

load_dotenv()

usuario = os.getenv("INSTAGRAM_USERNAME")
senha = os.getenv("INSTAGRAM_PASSWORD")

#iniciar 0 instaloader
loader = instaloader.Instaloader()
 
try:
    loader.login(usuario, senha)
    print('login realizado com sucesso')
except Exception as e:
    print(f'falha ao logar {e}')



perfil = "neymarjs"
profile = instaloader.Profile.from_username(loader.context, perfil)

dados = []

for post in profile.get_posts():
    dados.append({ 
            "data": post.date,
            "likes": post.likes,
            "comentarios": post.comments,
            "hashtags": post.caption_hashtags,  
         }  )   
  
#salvado em formato CSV
import pandas as pd

df = pd.DataFrame(dados)
df.to_csv("dados_instagram.csv", index=False ) 

