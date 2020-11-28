import subprocess
import requests
import json
from pathlib import PurePath

API_URL = "hidden :)"
AUTH_KEY = "hidden :)"
MPV_PATH = "path/to/mpv_binary_or_exe"
PRESETS = "presets.json"

def main():
    video_library = getAvailableVideos()
    video_url = askVideoSelection(video_library)
    upscaling_settings = askUpscalingSettings()
    playRequestedVideo(video_url['url'], upscaling_settings)

def getAvailableVideos():
    """Ping API for video library"""
    response = requests.get(API_URL, headers={"Authorization" : AUTH_KEY})
    result = response.json()
    return result

def askVideoSelection(video_library):
    """Ask user for video selection, return URL of video"""
    print("Video Library:")
    ticker = 1
    video_names = list(video_library.keys())
    for video in video_names:
        print(" ({0}) ".format(ticker) + video)
        ticker += 1
    chosen_video = int(input("Enter video name to select: "))
    return video_library[video_names[chosen_video - 1]]

def askUpscalingSettings():
    """Ask user for which set of upscaling presets to use for playback"""
    with open(PRESETS, "r") as presets_file:
        presets = json.load(presets_file)
    print("Upscaling Presets:")
    ticker = 1
    preset_names = list(presets.keys())
    for preset in preset_names:
        print (" ({0}) ".format(ticker) + preset)
        ticker += 1
    print(" ({0}) ".format(ticker) + "none")
    chosen_preset = int(input("Enter preset number to select: "))
    if (chosen_preset == ticker):
        return False
    return (preset_names[chosen_preset - 1], presets[preset_names[chosen_preset - 1]])

def parseUpscalingSettings(upscaling_settings):
    """Parse shader file list to command options string"""
    if (upscaling_settings == False):
        return ""
    result = '--glsl-shaders="'
    for shader in upscaling_settings[1]:
        # Using PurePath since windows hates forward slashes...
        result += str(PurePath(shader)) + ';'
    return result + '"'

def playRequestedVideo(video_url, upscaling_settings):
    """Run mpv with video url and upscaling settings"""
    upscaling_options = parseUpscalingSettings(upscaling_settings)
    command = MPV_PATH + " " + video_url + " " + upscaling_options
    print(command)
    subprocess.run(command)

if __name__ == "__main__":
    main()
