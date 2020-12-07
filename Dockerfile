FROM faucet/python3
COPY app/ /app/
RUN pip3 install pytest-flask
RUN pip3 install flask-httpauth
ENV TOKEN_PASS=Token 
CMD python3 /app/app.py
