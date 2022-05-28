import shutil
import pathlib
import sys
import os
from argparse import ArgumentParser


def execute(command):
    print(command, file=sys.stderr)
    os.system(command)


def rename_dylib_reference(base_dir: pathlib.Path, file: pathlib.Path):
    with os.popen(f"otool -L {file}") as p:
        query_out = p.readlines()
    execute(f"install_name_tool {file} -id {file}")
    for line in query_out:
        line = line.strip().split(" ")[0]
        for prefix in ["install_arm64", "install_x86_64", "install_universal"]:
            begin = line.find(prefix)
            if begin < 0:
                continue
            execute(f"install_name_tool {file} -change {line} {(base_dir / line[begin + len(prefix) + 1:]).absolute()}")
            break


if __name__ == "__main__":
    parser = ArgumentParser(description="Package the generated files into ZIP.")
    parser.add_argument("ffmpeg_path", type=str, help='indicate FFmpeg dir or archive.')
    parser.add_argument("target_dir", type=str, help='indicate target.')
    args = parser.parse_args()
    ffmpeg_path = pathlib.Path(args.ffmpeg_path)
    target_dir = pathlib.Path(args.target_dir)
    if ffmpeg_path.is_file():
        shutil.unpack_archive(ffmpeg_path, target_dir)
    else:
        shutil.copytree(ffmpeg_path, target_dir)
    for f in target_dir.rglob("*"):
        if f.is_file() and (f.suffix in {'.dylib', '.a'} or len(f.suffix) == 0 and os.access(f, os.X_OK)):
            rename_dylib_reference(target_dir, f)
