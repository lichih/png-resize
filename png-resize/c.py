from distutils.command.build_scripts import first_line_re
import os, glob
from posixpath import abspath
from typing import List
from tqdm import tqdm
from PIL import Image
import click
from .u import perr

@click.command(help='png-resize')
@click.option('-d/-r', '--dry/--run', 'dry_run', is_flag=True, default=None, required=True, help='Dry Run.')
@click.option('-f', '--force', 'force_write', is_flag=True, default=False, help='Dry Run.')
@click.option('-n', '--first', 'first_n', default=50, help='First N Files To Resize')
@click.argument('srcpaths', nargs=-1, type=click.Path(exists=True, file_okay=False))
@click.argument('dstpath', nargs=1, type=click.Path(exists=True, file_okay=False, writable=True))
def png_resize_c(dry_run: bool, srcpaths: List[str], dstpath: str, first_n: int, force_write: bool):
    dstpath = abspath(dstpath)
    perr(f'{first_n=} {dry_run=} {srcpaths=} {dstpath=}')
    fnDirs = set()
    pngs = []
    for src in srcpaths:
        src = abspath(src)
        perr(f'{src=}')
        for fnSrc in tqdm(glob.iglob(os.path.join(src, '**', '*.png'), recursive=True)):
            fnDst = os.path.join(dstpath, fnSrc[len(src)+1:])
            fnDir = os.path.dirname(fnDst)
            pngs.append([0, fnSrc, fnDst, fnDir])
            # if fnDir not in fnDirs:
            #     fnDirs.add(fnDir)
            #     perr(fnDir)
    perr(f'{len(pngs)=}')
    for _ in tqdm(pngs):
        _[0] = os.path.getsize(_[1])

    pngs = sorted(pngs, key=lambda x: x[0], reverse=True)
    for size, fnSrc, fnDst, fnDir in tqdm(pngs[:first_n]):
        if not force_write and os.path.exists(fnDst):
            continue
        im = Image.open(fnSrc)
        im = im.resize((im.width//2, im.height//2), Image.LANCZOS)
        if not dry_run:
            if fnDir not in fnDirs:
                os.makedirs(fnDir, mode=0o775, exist_ok=True)
                fnDirs.add(fnDir)
            im.save(fnDst, optimize=True, quality=95)

if __name__ == '__main__':
    png_resize_c()
