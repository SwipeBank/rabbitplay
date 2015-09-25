## Run Examples  

#### Consumer:  

```sh
python -m examples.receive
```  

#### Producer:  

```sh
python -m examples.send_message 'rabbit1...............'
python -m examples.send_message 'rabbit2..........'
python -m examples.send_message 'rabbit3.....'
```

## Docker:

#### Prepare:
```sh
# build image
docker build -t rabbitplay .
# start rabbitmq
docker-compose up -d
```

### Start consumer:
```sh
docker run \
  --name rabbitplay_receive \
  --rm \
  -it \
  --net host \
  -e PYTHONUNBUFFERED=1 \
  rabbitplay \
  python -m examples.receive
```

### Send a message:
```sh
docker run \
  --name rabbitplay_send \
  --rm \
  -it \
  --net host \
  -e PYTHONUNBUFFERED=1 \
  rabbitplay \
  python -m examples.send_message 'rabbit......'

```
