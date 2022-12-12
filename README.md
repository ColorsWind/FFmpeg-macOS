# FFmpeg-macOS
FFmpeg shared universal binaries (x86_64 and arm64) for macOS.

## Usage

You may compile it by yourself or download and install prebuild binary.

- **Compile FFmpeg by yourself.**

    By default, our script will compile FFmpeg with `--enable-shared --disable-static`, if you want to use custom flags, you can edit `make_compile.py`.
    
    Available options: `--ffmpeg_dir --target_dir --dir`, use `-h` to see help.
    
    ```bash
    git clone https://github.com/embodyme/FFmpeg-macOS.git build-script
    git clone https://github.com/FFmpeg/FFmpeg.git ffmpeg
    cd ffmpeg
    git checkout n4.4.1
    python ../build-script/make_compile.py 
    python ../build-script/make_universal.py
    python ../build-script/package.py --tag n4.4.1
    ```

- **Install Prebuilt Binary**

  You may download from [release](https://github.com/ColorsWind/FFmpeg-macOS/releases/) and install it by `install.py`.

  ```bash
  wget https://github.com/ColorsWind/FFmpeg-macOS/releases/download/n5.0.1-patch3/FFmpeg-shared-n5.0.1-OSX-universal.zip
  wget https://github.com/ColorsWind/FFmpeg-macOS/releases/download/n5.0.1-patch3/install.py
  python install.py FFmpeg-shared-n5.0.1-OSX-universal.zip ~/ffmpeg-n5.0.1
  ```
  Then, FFmpeg-shared will be installed on `~/ffmpeg-n5.0.1`.

  

## Release

Latest: tag n5.0.1
https://github.com/ColorsWind/FFmpeg-macOS/releases

## License

[FFmpeg](http://ffmpeg.org) licensed under the [LGPLv2](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).  and its source can be downloaded [here](https://github.com/FFmpeg/FFmpeg).

This repository contains FFmpeg build scripts, which licensed under the MIT License.

MIT License

Copyright (c) 2022 ColorsWind

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
