# Dockerfile
FROM python:3.10
ENV VLLM_DEVICE=cpu
WORKDIR /app

# ติดตั้งไลบรารีจำเป็น
RUN pip install fastapi uvicorn streamlit requests vllm

# ใส่ model แบบ pre-load ได้ภายหลัง

COPY . .

CMD ["bash"]