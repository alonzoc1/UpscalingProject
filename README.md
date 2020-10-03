# Upscaling Project

To run this project you should have Python 3.6 or later, the [requests library](https://requests.readthedocs.io/en/master/user/install/#install), and [mpv](https://mpv.io/installation/) installed somewhere on your machine. Open up `main.py` with a code editor and set `MPV_PATH` to it's binary/executable file. If not on Windows, you may also have to edit `presets.json` and change the filepath to use forward slashes (i.e. path/to/shader.glsl) instead of the backslashes I included (path\\\to\\\shaders.glsl). You may also have to edit the line `result += shader + ';'` to `result += shader + ':'` since UNIX mpv handles file list parsing differently according to the [documentation](https://mpv.io/manual/master/#list-options). In the future this will probably be updated to not require these extra steps.

Currently the function that calls the API to get pull the video library (`getAvailableVideos()`) is hard coded. Replace the return value of that function with {"your video name", "url to video file"} to get it working.

The `presets.json` file comes with several preset lists of shader files to apply to the video in real time via mpv, feel free to edit in your own combinations.

Finally all credit for the GLSL shader files go to [bloc97](https://github.com/bloc97)'s great project [Anime4k](https://github.com/bloc97/Anime4K), give it a look!
