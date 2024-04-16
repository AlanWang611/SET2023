FROM dustynv/jetson-inference:r32.7.1

RUN ldconfig

COPY . .

CMD ["python3", "main.py"]
