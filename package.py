from argparse import ArgumentParser
import os
import pathlib
import shutil


if __name__ == "__main__":
    parser = ArgumentParser(description="Package the generated files into ZIP.")
    parser.add_argument("--dir", type=str, default=os.getcwd(), help='indicate target dir.')
    parser.add_argument("--tag", type=str, default="UNKNOWN", help='indicate FFmpeg tag.')
    args = parser.parse_args()
    target_dir = pathlib.Path(args.dir).absolute()
    tag = args.tag
    print(f"Packaging... {target_dir} {tag}")
    install_intel_dir = target_dir / "install_x86_64"
    install_apple_dir = target_dir / "install_arm64"
    install_universal_dir = target_dir / "install_universal"

    shutil.make_archive(f"FFmpeg-shared-{tag}-OSX-arm64", "zip", install_apple_dir)
    print("Finished arm64.")
    shutil.make_archive(f"FFmpeg_shared-{tag}-OSX-x86_64", "zip", install_intel_dir)
    print("Finished x86_64.")
    shutil.make_archive(f"FFmpeg-shared-{tag}-OSX-universal", "zip", install_universal_dir)
    print("Finished universal.")
