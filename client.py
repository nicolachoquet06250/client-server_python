import socket


# cette fonction n'est pas très performante puisqu'elle
# ouvre et ferme la socket pour chaque message,
# mais vous voyez le principe.
def envoyer_message(ip: str, port: int, message):
    # on ouvre une socket TCP / IP, en IP V4
    # la doc contient une liste de constantes avec
    # les protocoles de base supportés
    # (http://docs.python.org/2/library/socket.html)
    # on peut aussi ouvrir des sockets unix, des datagrames...
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        # on broadcast le message
        sock.sendall(message.encode())
        # et on lit la réponse cash pistache
        # Tout ça est synchrone, car si on veut
        # faire de l'asynchrone, l'exemple serait
        # vachement moins simple
        response = sock.recv(1024)
        print("Received: " + response.decode())
    except Exception as e:
        print("Impossible de se connecter au serveur: {}".format(e))
    finally:
        # toujours fermer sa socket, même si dans notre cas
        # on a pas besoin de la fermer pour chaque message
        # On pourrait aussi utiliser le context manager closing()
        # pour cette tâche
        sock.close()


# petit test qui envoit trois messages
if __name__ == "__main__":
    ip, port = "127.0.0.1", 7777

    envoyer_message(ip, port, "Hello World 1")
    envoyer_message(ip, port, "Hello World 2")
    envoyer_message(ip, port, "Hello World 3")
