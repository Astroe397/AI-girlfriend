A python script that uses Llama.cpp and any inputed llm that is turned into a girlfriend for any one of your friends to torment with

# how it works

-Python script has pre set rules for the AI
-Uses discord API to stream it to a discord channel (you could fork it to work on any other platform if you try hard enough)
-Listens to local server 8080 that llama.cpp makes

-listens to trigger word mapel "hey mapel" or "mapel" and takes whole message
-message is parsed to llama server
-server sends a repond to server and server uses discord APi to send the response

# how to set up

<h3> PIP INSTALL DISCORD </h3>

-create a folder anywhere inputing the python files. 
-on discord dev portal create a new bot and find the TOKEN
-input the token in engine.py
-on desired discord channel get the channel ID and paste the id in engine.py
-inside engine.py look for (ENTERNAME) and put the persons name to relate to
-download llama.cpp (https://github.com/ggml-org/llama.cpp (for GPU proccesing use cuda 12) ) 
-once extracted in a folder open up cmd  and paste 

"FOLDERLOCATION\llama-server.exe" -m "FOLDERLOCATION\L3-8B-Stheno-v3.2.Q3_K_S.gguf" --n-gpu-layers 33

-(note decrease the number after "--n--gpu--layers" if it tends to crash or is super slow)

-run the pyton script and enjoy
