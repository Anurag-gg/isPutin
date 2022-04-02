FROM jhonatans01/python-dlib-opencv
COPY . .
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]