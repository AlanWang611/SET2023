FROM dustynv/jetson-inference:r32.7.1

COPY . .

CMD ["python3", "main.py"]
