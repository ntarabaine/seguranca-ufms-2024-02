import os
import hmac
import hashlib

def gerar_ramdom_bytes(length):
  return os.urandom(length)

def hmac_auth(key, msg):
  return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).hexdigest()

def verify_hmac(key, msg, hmac_value):
    genereted_hmac = hmac_auth(key, msg)
    return hmac.compare_digest(genereted_hmac, hmac_value)

key = gerar_ramdom_bytes(16)
msg = "Testando Hmac"
hmac_value = hmac_auth(key, msg)
verificar = verify_hmac(key, msg, hmac_value)

print("HMAC: ", hmac_value)
print("verificando: ", verificar)