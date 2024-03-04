FROM python:3.13.0a4-alpine3.19
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=5 \
CMD curl --fail http://localhost:5000/health  || exit 1
ENTRYPOINT ["python", "./src/app.py"]