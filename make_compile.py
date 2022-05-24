from argparse import ArgumentParser
from multiprocessing import cpu_count
import pathlib
import sys
import os


def execute(command: str):
    print(f"Execute: {command}.")
    os.system(command)


if __name__ == "__main__":
    parser = ArgumentParser(description="Configure & Make & Install FFmpeg.")
    parser.add_argument("--dir", type=str, default=os.getcwd(), help='indicate FFmpeg dir.')
    args = parser.parse_args()
    ffmpeg_dir = pathlib.Path(args.dir).absolute()
    print(f"Compile... {ffmpeg_dir}")


    def clean():
        print("Clean project.")
        execute(f"cd {ffmpeg_dir} && make clean && make distclean")


    def make(arch: str):
        n_cpu = cpu_count()
        print("Configure project.")
        execute(
            f"cd {ffmpeg_dir} && ./configure --enable-cross-compile --prefix={ffmpeg_dir / ('install_' + arch + '/')} --enable-shared --disable-static --arch={arch} --cc='clang -arch {arch}'")
        print(f"Make project ({n_cpu} threads).")
        execute(f"cd {ffmpeg_dir} && make -j{n_cpu}")
        print(f"Install project.")
        execute(f"cd {ffmpeg_dir} && make install")


    print("----------arm64----------")
    clean()
    make("arm64")
    print("----------x86_64----------")
    clean()
    make("x86_64")
