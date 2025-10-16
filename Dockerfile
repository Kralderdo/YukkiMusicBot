# Yeni Python sürümüyle uyumlu taban imaj (Python 3.11 + NodeJS)
FROM nikolaik/python-nodejs:python3.11-nodejs20

# Gerekli paketleri yükle
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini ayarla
WORKDIR /app

# Tüm dosyaları kopyala
COPY . /app/

# Pip güncelle ve bağımlılıkları kur
RUN pip3 install --no-cache-dir -U pip setuptools wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Başlatma komutu
CMD ["bash", "start"]
