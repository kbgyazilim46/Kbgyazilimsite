from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Kimse Baş Göz hakkında</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }}
        nav a {{ margin: 10px; text-decoration: none; color: #333; font-weight: bold; }}
        .container {{ max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #444; }}
    </style>
</head>
<body>
    <nav>
        <a href="/">Hakkında</a>
        <a href="/iletisim">İletişim</a>
    </nav>
    <div class="container">
        %%CONTENT%%
    </div>
</body>
</html>
"""

@app.route('/')
def hakkinda():
    content = """
    <h1>Hakkında</h1>
    <p>Selamünaleyküm, ben nam-ı değer <strong>Kimsebaşgöz</strong>. İsmim <strong>Ahmet Utku Can</strong>'dır.</p>
    <p>Aşağıdaki bilgiler iletişim bilgilerimdir. Her türlü sanal işlem için bana ulaşabilirsiniz güvenilirlik için aşağıdaki Instagram hesabıma yazabilirsiniz.</p>

    <img src="https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/profil.png" alt="Kimsebaşgöz" width="300">
    <h2>Güvence Fotoğrafları</h2>
<div style="display: flex; gap: 15px; flex-wrap: wrap;">
  <img src="https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/guvence1.png" alt="Güvence 1" width="200">
  <img src="https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/guvence2.png" alt="Güvence 2" width="200">
  <img src="https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/guvence3.jpg" alt="Güvence 3" width="200">
</div>

<audio autoplay loop>
  <source src="https://raw.githubusercontent.com/kbgyazilim46/kbgyazilimsite/main/arkamuzik.mp3" type="audio/mp3">
</audio>

    <h2>İletişim</h2>
    <p><strong>Telefon:</strong> <a href='tel:wa.me/+639092363984'>wa.me/+639092363984</a></p>
    <p><strong>Instagram:</strong> <a href='https://instagram.com/_kimsebasgoz_' target='_blank'>@_kimsebasgoz_</a></p>
    <p><strong>E-posta:</strong> <a href='mailto:kimsebasgozedemez@gmail.com'>kimsebasgozedemez@gmail.com</a></p>
    """
    return HTML_TEMPLATE.replace("%%CONTENT%%", content)

@app.route('/iletisim')
def iletisim():
    content = """
    <h1>İletişim</h1>
    <p><strong>Telefon:</strong> <a href='tel:wa.me/+639092363984'>wa.me/+639092363984</a></p>
    <p><strong>Instagram:</strong> <a href='https://instagram.com/_kimsebasgoz_' target='_blank'>@_kimsebasgoz_</a></p>
    <p><strong>E-posta:</strong> <a href='mailto:kimsebasgozedemez@gmail.com'>kimsebasgozedemez@gmail.com</a></p>
    """
    return HTML_TEMPLATE.replace("%%CONTENT%%", content)

if __name__ == '__main__':
    app.run(debug=True)
