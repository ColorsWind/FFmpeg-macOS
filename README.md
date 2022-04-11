# FFmpeg-macOS
FFmpeg shared universal binaries (x86_64 and arm64) for macOS.

## Usage
```bash
git clone git@github.com:ColorsWind/FFmpeg-macOS.git build-script
git clone git@github.com:FFmpeg/FFmpeg.git ffmpeg
cd ffmpeg
git checkout n5.0.1
python ../build-script/make_compile.py 
python ../build-script/make_universal.py
python ../build-script/package.py --tag n5.0.1
```

## Download prebuild 
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
