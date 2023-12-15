import subprocess

def change_video_codec(input_file, output_file, codec='libx264', audio_codec='aac'):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', codec,
        '-c:a', audio_codec,
        output_file
    ]
    subprocess.run(command)

file_name = "static/videos/fern_side_by_side_website.mp4"
output_file_path = "static/videos/fern_side_by_side_website_web.mp4"

change_video_codec(file_name, output_file_path)