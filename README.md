# fastapi-quickstart

This is a quickstart of [FastAPI](https://fastapi.tiangolo.com).
- Python 3.10
- Use [peewee](https://github.com/coleifer/peewee) as ORM.

## Set up
- Open [config file](app/config/config_local.toml) and set up your own MySQL config.

## Start up

### Run with python
1. Install dependencies
    ```shell
    $ pip install -r requirements.txt
    ```
   
2. Run server
    ```shell
    $ python server.py
    ```

### Run with docker
 
1. Build docker image
    ```shell
    $ ./deploy.sh [env] [tag]
    ```

2. Run docker container
    ```shell
    $ docker run -d -p 8000:8000 --name fastapi-quickstart fastapi-quickstart:[tag] server.py
    ```

3. Check logs
    ```shell
    $ docker logs -f fastapi-quickstart
    ```


## API

Open [http://127.0.0.1:8000/fastapi/docs](http://127.0.0.1:8000/fastapi/docs) to check the API doc.
