## Sends OpenCV output to STDOUT

#### This is sample code for local viewing of the output of OpenCV when the video is being processed remotely

To run the sample feed

`docker --context remote-server run --gpus all opencv_to_stdout-detection | ffplay -f rawvideo -pix_fmt bgr24 -s 240x160 -framerate 24 -i -`

Reading the stdout of docker compose doesn't work correctly yet. This command still produces scrambled video. 

`docker --context remote-server compose up | ffplay -f rawvideo -pix_fmt bgr24 -s 240x160 -framerate 24 -i -`
