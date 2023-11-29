FROM python:3.10.13

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

COPY ./requirements.txt ./code/requirements.txt

RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9000

CMD ["python", "crowdAI run.py", "rgb-footprint-extract", "run_deeplab.py", "--inference", "--backbone=drn_c42", "--out-stride=8", "--workers=2", "--epochs=1", "--test-batch-size=1", "--gpu-ids=0", "--resume=urban3d", "--best-miou", "--window-size=512", "--stride=512", "--input-filename='train_image_011_new.npy'", "--output-filename='output3.png'"]