import sherpa_onnx, wave, numpy as np, json
d='sherpa-onnx-whisper-small/'
import glob
enc=glob.glob(d+'*encoder*int8*.onnx')[0]; dec=glob.glob(d+'*decoder*int8*.onnx')[0]; tok=glob.glob(d+'*tokens.txt')[0]
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=enc,decoder=dec,tokens=tok,language='pt',task='transcribe',num_threads=4)
w=wave.open('/home/claude/ref/audio.wav'); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
cfg=sherpa_onnx.VadModelConfig(); cfg.silero_vad.model='silero_vad.onnx'; cfg.silero_vad.min_silence_duration=0.35; cfg.silero_vad.max_speech_duration=12; cfg.sample_rate=sr
vad=sherpa_onnx.VoiceActivityDetector(cfg,buffer_size_in_seconds=60)
segs=[]
ws=cfg.silero_vad.window_size
def flush():
    while not vad.empty():
        s=vad.front; vad.pop(); st=s.start/sr; samples=np.array(s.samples,dtype=np.float32)
        r=rec.create_stream(); r.accept_waveform(sr,samples); rec.decode_stream(r)
        segs.append(dict(start=st,end=st+len(samples)/sr,text=r.result.text.strip())); print(segs[-1],flush=True)
for i in range(0,len(x),ws):
    vad.accept_waveform(x[i:i+ws]); flush()
vad.flush(); flush()
json.dump(segs,open('segs.json','w'),ensure_ascii=False)
