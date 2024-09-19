from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encriptar(msg, chave):
	iv = get_random_bytes(AES.block_size)
	cipher = AES.new(chave,AES.MODE_CBC, iv)
	msg_padded = pad(msg.encode('utf-8'), AES.block_size)
	
	msg_en = cipher.encrypt(msg_padded)
	return iv + msg_en	
	
def aes_decriptar(msg_en, chave):
	iv = msg_en[:AES.block_size]
	cipher = AES.new(chave, AES.MODE_CBC, iv)
	msg_padded = cipher.decrypt(msg_en[AES.block_size:])
	msg = unpad(msg_padded, AES.block_size)
	return msg.decode('utf-8')
	
	
msg = "benito eh o melhor!"
chave = get_random_bytes(16)

msg_en = aes_encriptar(msg, chave)
print("mensagem encriptada: ", msg_en)


msg_de = aes_decriptar(msg_en, chave)
print("mensagem decriptada: ", msg_de)