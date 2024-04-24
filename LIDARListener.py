import socket
import matplotlib.pyplot as plt
import numpy as np

# HOST AND PORT
PORT = 65432

angles = np.linspace(0, 2*np.pi, 100)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_title("LiDAR Strength and Distance")
plt.show()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', PORT))
    s.listen(10)
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            received_data = data.decode().split(',')
            if len(received_data) == 2:
                strength, distance = map(float, received_data)
                ax.clear()
                ax.scatter(angles, np.full_like(angles, distance), c=np.full_like(angles, strength), cmap='viridis',
                           alpha=0.75)
                ax.set_title("LiDAR Strength and Distance")
                plt.draw()
                plt.pause(0.001)
                print("Strength:", strength, "Distance:", distance)


def main():
    print("test")

if __name__ == "__main__":
    main()