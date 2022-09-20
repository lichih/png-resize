# png-resize

### Command line tool to resize PNG images
```
Usage: python -m png-resize.c [OPTIONS] [SRCPATHS]... DSTPATH

  png-resize

Options:
  -d, --dry / -r, --run  Dry Run.  [required]
  -f, --force            Dry Run.
  -n, --first INTEGER    First N Files To Resize
  --help                 Show this message and exit.
```
### Installation
```bash
pip install git+https://github.com/lichih/png-resize.git@master
```
### Usage

```bash
python -m png-resize.c `wslpath 'D:\rsync\eir\resource'`
```

### todo
- pngcrush  
https://pypi.org/project/pyguetzli/
- UnityPy  
https://pypi.org/project/UnityPy/

```python
import pyguetzli
from PIL import Image

image = Image.open("./test/image.jpg")
optimized_jpeg = pyguetzli.process_pil_image(image)
```
