# flying-with-raspberry
Usign a Raspberry Pi Zero 2 for controlling a rocket or a RC plane

## flight software

The flight software designed to run on an embeded raspberry in a plane or a rocket.

Present in the 'flight' folder.

### Launching
#### On Windows

Creating the Python virtual environment

```
python.exe -m pip install --upgrade pip
python -m venv .venv
.\.venv\Scripts\activate
```

Activating the Python virtual environment

```
.\.venv\Scripts\activate
```

Launching

```
python main.py
```

#### On Linux

Creating the Python virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install fastapi
pip3 install uvicorn
```

Activating the Python virtual environment

```
source .venv/bin/activate
```

Launching

```
python3 main.py
```
