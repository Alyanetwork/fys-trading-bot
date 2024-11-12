Projeniz için ilişkisel veritabanı yönetim sistemi (RDBMS) taslağını aşağıda sunuyorum. Bu veritabanı yapısı, kullanıcıların hesap bilgilerini, API anahtarlarını, işlem geçmişini ve cüzdan bakiyelerini saklayarak yatırım botunun sağlıklı bir şekilde çalışmas

RDBMS Taslağı: Tablo
1. users - Kullanıcı
sql
Kodu kopyala
CREATE TABLE users (
    user_id SERIAL 
    user_id SERI

    user_id S

    user_i

    use

   
PRIMARY KEY,
    username 
    username VAR

    username 

    userna
VARCHAR(50) UNIQUE NOT NULL,
    email 
  
VARCHAR(100) UNIQUE NOT NULL,
    password_hash 
    password_hash VAR

    password_hash 

    password_ha

    password
VARCHAR(255) NOT NULL,
    created_at 
    created_at

    created

    crea
TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

);
`
user_id: He
username: K
email:
password_hash:
created_at: Hes
2. api_keys - Kullan
sql
Kodu kopyala
CREATE TABLE api_keys (
    api_key_id SERIAL 
    api_key_id 

    api_key_i

    api
PRIMARY KEY,
    user_id 
    user_id 
INT REFERENCES users(user_id) ON DELETE CASCADE,
    exchange_name 
    exchange_name VA

    exchange_name 

    exchange_na
VARCHAR(50) NOT NULL,
    api_key 
 
VARCHAR(255) NOT NULL,
    api_secret 
    api_secret VAR

    api_secret V

    api_secre

    api_se

    api
VARCHAR(255) NOT NULL,
    created_at 
    created_at

    created

    crea

    c
TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

);
``

);
api_key_id:
user_id: Kusers tab
exchange_name:
api_key: Kullanıcıya özgü API anahtarı.
api_secret: Kullanıcıya özg
3. transactions - Gerçekleştirilen
sql
Kodu kopyala
CREATE TABLE transactions (
    transaction_id SERIAL 
    transaction_id SERIAL PRIMAR

    transaction_id SERIAL PR

    transaction_id

    transactio

    transa

    t
PRIMARY KEY,
    user_id 
   
INT REFERENCES users(user_id) ON DELETE CASCADE,
    symbol 
    symbol VARC

    symbol 
VARCHAR(20) NOT NULL,
    order_type 
    order_type 

    order_ty

    o

 
VARCHAR(10) NOT NULL,
    side 
    side VAR

    sid
VARCHAR(10) NOT NULL,
    amount 
    amount 

    amou

    a

 
DECIMAL(18, 8) NOT NULL,
    price 
    price DECIMA

    price DE

    pric

    
DECIMAL(18, 8),
    status 
    status VARC

    status 

    sta

   
VARCHAR(20) DEFAULT 'pending',
    created_at 
    created_at TIMES

    created_at 

  
TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
transaction_id: İ
user_id: Kullanıcı kimliği,users tablosuna refer
symbol:
order_type: İşlem tür
side: İşlem yönü
amount: İşlem miktarı.
price: İşlem
status: İşlemin durumu ("
4. wallets - Kullanıcı cüzdan
sql
Kodu kopyala
CREATE TABLE wallets (
    wallet_id SERIAL 
    wallet_id SERIAL PRIMAR

    wallet_id SERIAL 

    wallet

    wa

  
PRIMARY KEY,
    user_id 
   
INT REFERENCES users(user_id) ON DELETE CASCADE,
    symbol 
    symbol VARCH

    sy

  
VARCHAR(20) NOT NULL,
    balance 
    balance D

    balanc

    ba
DECIMAL(18, 8) DEFAULT 0.0,
    updated_at 
    updated_at TIMESTA

    updated_at TI

    updated_
TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
wallet_id:
user_id: Kullanusers tablosuna referans.
symbol: Kripto para birimi (örneğin, "BTC", "ETH").
balance: Kullanıcının sahip olduğu miktar.
updated_at: Cüzdanın en son güncellenme zamanı.
5. bot_settings - Kullanıcı bot ayarlarını saklar
sql
Kodu kopyala
CREATE TABLE bot_settings (
    setting_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    bot_type VARCHAR(20) NOT NULL, -- örn. 'DCA', 'Grid'
    symbol VARCHAR(20) NOT NULL,
    investment_amount DECIMAL(18, 8),
    interval_hours INT,
    grid_levels INT,
    grid_size DECIMAL(18, 8),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
setting_id: Bot ayarları kimliği.
user_id: Kullanıcı kimliği, users tablosuna referans.
bot_type: Bot türü (örneğin, "DCA", "Grid"
symbol: İşlem ya
investment_amount: Bo
interval_hours:
grid_levels:
grid_size: Gr
Ö
Kul

sql
Kodu kopyala
INSERT INTO users (username, email, password_hash) 

VAL
VALUES ('user1', 'user1@example.com', 'hashed_password');
C

sql
Kodu kopyala
INSERT INTO wallets (user_id, symbol, balance) 
VALUES (1, 'BTC', 0.5);
Notlar
Tüm tablolar user_id s
ON DELETE CASCADE kullusers tablosundaki
B
