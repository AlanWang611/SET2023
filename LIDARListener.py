import socket
import matplotlib.pyplot as plt
import numpy as np

# HOST AND PORT
PORT = 65432

angles = np.linspace(0, 2*np.pi, 100)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_title("LiDAR Strength and Distance")
ax.set_ylim(0, 100) # ADJUST LIMIT
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
                angle, distance = map(float, received_data)
                angle = np.deg2rad(angle)
                if 0 <= angle <= 2*np.pi and 0 <= distance <= 100:
                    ax.clear()
                    ax.scatter(angle, distance, c='b', alpha=0.75)
                    ax.set_title("LiDAR Strength and Distance")
                    ax.set_ylim(0, 100) # ADJUST LIMIT
                    plt.pause(0.01)


def main():
    print("test")

if __name__ == "__main__":
    main()