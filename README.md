# CodeJam 2019: Home Insurance Photo Analyzer

Built by Albert Kragl, Celine Huang, Emma Eagles and Paul Hooley :)

## Backend

Set up a Python virtual environment for the backend:
```
python3 -m venv env

source env/bin/activate 
```

Once the environment is activated, install dependencies:

```
pip install -r /path/to/requirements.txt
```

You will also need to install the [RetinaNet model file](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5) that will be used for object detection.

If any packages are missing when you run `app.py`, install them with `pip install`. To run the backend from the `backend` folder:

```
python app.py
```

## Frontend

To run the frontend, you will need to install the [Quasar CLI](https://quasar.dev/quasar-cli/installation) and **version 3 or higher** of the [Vue CLI](https://cli.vuejs.org/guide/installation.html). If you have an older version of Vue CLI installed, you will need to uninstall it and re-install the latest version.

To install dependencies, run `npm install` or `yarn install` in the `frontend` folder. To run the frontend from the `frontend folder`:

```
quasar dev
```