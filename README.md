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

### Usage

```bash
python -m png-resize.c `wslpath 'D:\rsync\eir\resource'`
```
