from argparse import ArgumentParser
import shutil
import sys
import os
import pathlib


def execute(command):
    print(command, file=sys.stderr)
    os.system(command)


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
    print(f"Make universal binaries... {target_dir}")

    install_intel_dir = target_dir / "install_x86_64"
    install_apple_dir = target_dir / "install_arm64"
    install_universal_dir = target_dir / "install_universal"
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
                create_universal_binary(install_intel_dir / relative, install_apple_dir / relative, target)
            else:
                shutil.copy2(f, target, follow_symlinks=False)
