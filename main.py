
import subprocess
import requests
import json

API_URL = "https://postman-echo.com/basic-auth"
API_UNAME = "postman"
API_PWORD = "password"
MPV_PATH = "C:\\Users\\Alonzo\\Downloads\\mpv.exe"
PRESETS = "presets.json"

def main():
    video_library = getAvailableVideos()
    video_url = askVideoSelection(video_library)
    upscaling_settings = askUpscalingSettings()
    playRequestedVideo(video_url, upscaling_settings)

def getAvailableVideos():
    """Ping API for video library"""
    """ Wait for API to get implemented
    response = requests.get(API_URL, auth=(API_UNAME, API_PWORD))
    result = response.json()
    print(result)
    return result
    """
    # Not yet implemented
    return ({"video name": "http://video-url.com/video.mp4"})

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
        result += shader + ';'
    return result + '"'

def playRequestedVideo(video_url, upscaling_settings):
    """Run mpv with video url and upscaling settings"""
    upscaling_options = parseUpscalingSettings(upscaling_settings)
    command = MPV_PATH + " " + video_url + " " + upscaling_options
    print(command)
    subprocess.run(command)

if __name__ == "__main__":
    main()
