from argparse import ArgumentParser
import shutil
import sys
import os
import pathlib


def execute(command):
    print(command, file=sys.stderr)
    os.system(command)

library_list = ["libavcodec", "libavdevice", "libavfilter", "libavformat", "libavutil", "libswresample", "libswscale", "libvpx", "libvorbis", "libvorbisenc", "libvorbisfile", "libogg"]
def change_dylib_path(file_path):

    execute(f"install_name_tool -id {os.path.join('@rpath',os.path.basename(file_path))} {file_path} ")
    with os.popen(f"otool -L {file_path}") as p:
        query_out = p.readlines()
    for line in query_out:
        line = line.strip().split(" ")[0]

        if os.path.basename(line).split('.')[0] in library_list:
            execute(f"install_name_tool -change {line} {os.path.join('@rpath', os.path.basename(line))} {file_path}")
    execute(f"otool -L {file_path}")

def create_universal_binary(x86_path, arm_path, universal_path):
    execute(f"lipo -create -arch arm64 {arm_path} -arch x86_64 {x86_path} -output {universal_path}")

    # with os.popen(f"otool -L {arm_path}") as p:
    #     query_out = p.readlines()
    # execute(f"install_name_tool {universal_path} -id {universal_path}")
    # for line in query_out:
    #     line = line.strip().split(" ")[0]
    #     if "install_arm64" in line:
    #         execute(
    #             f"install_name_tool {universal_path} "
    #             f"-change {line} {line.replace('install_arm64', 'install_universal')}"
    #         )
    #
    # with os.popen(f"otool -L {x86_path}") as p:
    #     query_out = p.readlines()
    # for line in query_out:
    #     line = line.strip().split(" ")[0]
    #     if "install_x86_64" in line:
    #         execute(
    #             f"install_name_tool {universal_path} "
    #             f"-change {line} {line.replace('install_x86_64', 'install_universal')}"
    #         )


if __name__ == "__main__":
    parser = ArgumentParser(description="Use lipo tool to turn into universal binaries.")
    parser.add_argument("--dir", type=str, default=os.getcwd(), help='indicate target dir.')
    args = parser.parse_args()
    target_dir = pathlib.Path(args.dir).absolute()

    target_folders = ["install_x86_64", "install_arm64", "install_universal"]
    target_folders_new = ["install_x86_64_new", "install_arm64_new", "install_universal_new"]
    # install_intel_dir = target_dir / "install_x86_64"
    # install_apple_dir = target_dir / "install_arm64"
    # install_intel_dir_new = target_dir / "install_x86_64_new"
    # install_apple_dir_new = target_dir / "install_arm64_new"
    # if install_intel_dir.exists():
    #     if install_intel_dir_new.exists():
    #         shutil.rmtree(install_intel_dir_new)
    #     install_intel_dir_new.mkdir()
    # if install_apple_dir.exists():
    #     if install_apple_dir_new.exists():
    #         shutil.rmtree(install_apple_dir_new)
    #     install_apple_dir_new.mkdir()

    for target_folder, target_folder_new in zip(target_folders, target_folders_new):
        install_dir = target_dir / target_folder
        install_dir_new = target_dir / target_folder_new
        if install_dir.exists():
            if install_dir_new.exists():
                shutil.rmtree(install_dir_new)
            install_dir_new.mkdir()
            for f in install_dir.rglob("*"):
                relative = f.relative_to(install_dir)
                target = install_dir_new / relative
                if f.is_dir():
                    target = install_dir_new / relative
                    target.mkdir(exist_ok=True, parents=True)
                else:
                    if f.is_symlink():
                        real = f.resolve()
                        os.symlink(real.name, target)
                    elif target.suffix in {'.dylib'} or len(target.suffix) == 0 and os.access(f, os.X_OK):
                        print(f)
                        print(target)
                        shutil.copy2(f, target, follow_symlinks=False)
                        change_dylib_path(target)
                        # create_universal_binary(install_intel_dir / relative, install_apple_dir / relative, target)
                    else:
                        shutil.copy2(f, target, follow_symlinks=False)