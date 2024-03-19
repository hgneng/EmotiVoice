import socket
import sys
from TTS.api import TTS

# 创建一个TCP/IP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址和端口号
server_address = ('localhost', 20492)
sock.bind(server_address)
tts = TTS('tts_models/en/ljspeech/tacotron2-DDC_ph')

# 监听端口，最大连接数为1
sock.listen(1)

while True:
  print('等待连接...')
  connection, client_address = sock.accept()
  try:
    print('连接来自:', client_address)
    #while True:
    data = connection.recv(1024)
    if data:
      print('收到数据:', data.decode())
      filepath = "/tmp/coquiOutput.wav"
      text = data.decode().rstrip()

      # 确保文本以"."结尾
      if not text.endswith("."):
        text += "."

      tts.tts_to_file(text, file_path=filepath)
      connection.sendall(filepath.encode())  # 发送数据给客户端
  except:
    # 当出现任何异常时执行的代码  
    e = sys.exc_info()  # 获取当前异常信息  
    print("发生异常:", e)
  finally:
    # 清理连接
    connection.close()