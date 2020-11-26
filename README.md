# Todolist

A simple todo list server, created with fast API

## create virtual environment (recommended)

```
conda create -n todolist python=3.9 pip -y

conda activate todolist
```

## install requirements

```
pip install requirements.txt

```

## run mongoDB

```
mongo
```

**Using Docker**

```
docker run -d -p 27017-27019:27017-27019 --name mongodb mongo
```

## start application

```
uvicorn main:app --reload
```

## Test the API

Got to localhost:8000/docs to see the docs and make requests
