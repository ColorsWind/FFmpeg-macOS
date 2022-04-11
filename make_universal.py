from argparse import ArgumentParser
import shutil
import sys
import os
import pathlib

if __name__ == "__main__":
    parser = ArgumentParser(description="Use lipo tool to turn into universal binaries.")
    parser.add_argument("--dir", type=str, default=os.getcwd(), help='indicate FFmpeg dir.')
    args = parser.parse_args()
    ffmpeg_dir = pathlib.Path(args.dir).absolute()
    print(f"Make universal binaries... {ffmpeg_dir}")

    install_intel_dir = ffmpeg_dir / "install_x86_64"
    install_apple_dir = ffmpeg_dir / "install_arm64"
    install_universal_dir = ffmpeg_dir / "install_universal"
    if install_universal_dir.exists():
        shutil.rmtree(install_universal_dir)
    install_universal_dir.mkdir()

    for f in install_apple_dir.rglob("*"):
        relative = f.relative_to(install_apple_dir)
        target = install_universal_dir / relative
        if f.is_dir():
            target = install_universal_dir / relative
            target.mkdir(exist_ok=True, parents=True)
        else:
            if f.is_symlink():
                real = f.resolve()
                os.symlink(real.name, target)
            elif target.suffix in {'.dylib', '.a'} or len(target.suffix) == 0 and os.access(f, os.X_OK):
                command = f"lipo -create -arch arm64 {install_apple_dir / relative} -arch x86_64 {install_intel_dir / relative} -output {target} "
                print(f"Execute: {command}")
                os.system(command)
            else:
                shutil.copy2(f, target, follow_symlinks=False)
