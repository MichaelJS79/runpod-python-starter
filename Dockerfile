FROM runpod/base:0.4.0-cuda12.1.105-cudnn8-ubuntu20.04
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY handler.py /handler.py
CMD ["python", "-u", "handler.py"]
