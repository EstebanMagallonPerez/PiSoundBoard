import wave
import pyaudio

chunk = 1024

def playAudioThread(file):
	p = pyaudio.PyAudio()

	wf = wave.open(file)
	args = {	'format':p.get_format_from_width(wf.getsampwidth()),
				'channels':wf.getnchannels(),
				'rate' : wf.getframerate(),
				'output' : True
	}

	
	args["output_device_index"] = 11

	stream = p.open(**args)
	data = wf.readframes(chunk)
	
	while data != b'':
		stream.write(data)
		data = wf.readframes(chunk)
	stream.close()    
	p.terminate()