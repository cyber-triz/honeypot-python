import socket
import threading
import datetime

# -------------------------------
# Módulo: Registrador
# -------------------------------
def registrar(evento):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    linha = f"[{timestamp}] {evento}"
    print(linha)
    with open("honeypot_log.txt", "a") as arquivo:
        arquivo.write(linha + "\n")


# -------------------------------
# Módulo: Emulador de serviço
# -------------------------------
def emulador_servico(client_socket, endereco, porta):
    registrar(f"Conexão de {endereco[0]}:{endereco[1]} na porta {porta}")
    
    try:
        banner = f"Serviço fictício na porta {porta}. A interação será registrada.\n"
        client_socket.send(banner.encode())

        while True:
            dados = client_socket.recv(1024)
            if not dados:
                break
            mensagem = dados.decode(errors="ignore").strip()
            registrar(f"Recebido de {endereco[0]}:{endereco[1]} >> {mensagem}")
            resposta = f"[porta {porta}] Comando '{mensagem}' registrado.\n"
            client_socket.send(resposta.encode())

    except Exception as e:
        registrar(f"Erro com {endereco[0]}:{endereco[1]} >> {e}")
    finally:
        registrar(f"Conexão encerrada com {endereco[0]}:{endereco[1]} na porta {porta}")
        client_socket.close()


# -------------------------------
# Módulo: Ouvinte de rede
# -------------------------------
def iniciar_ouvinte(host, portas):
    servidores = []

    for porta in portas:
        try:
            servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            servidor.bind((host, porta))
            servidor.listen(5)
            servidores.append(servidor)
            registrar(f"[OUVINTE] Escutando na porta {porta}")
        except Exception as e:
            registrar(f"[ERRO] Porta {porta} falhou: {e}")

    try:
        while True:
            for servidor in servidores:
                servidor.settimeout(1.0)
                try:
                    client_socket, endereco = servidor.accept()
                    porta = servidor.getsockname()[1]
                    thread = threading.Thread(target=emulador_servico, args=(client_socket, endereco, porta))
                    thread.daemon = True
                    thread.start()
                except socket.timeout:
                    continue
    except KeyboardInterrupt:
        registrar("Honeypot encerrado manualmente.")
    finally:
        for servidor in servidores:
            servidor.close()
        registrar("Todos os ouvintes foram encerrados.")


# -------------------------------
# Execução principal
# -------------------------------
if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORTAS = [21, 22, 80]  # FTP, SSH, HTTP (falsos)
    iniciar_ouvinte(HOST, PORTAS)
