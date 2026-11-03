import json,subprocess,os
d=json.load(open('/home/claude/v2/durs.json')); n=len(d)
aud=[x for x in os.listdir('/mnt/user-data/uploads') if x.startswith('5426973f')][0]
ins=[];
for k in range(n): ins+=['-i',f'/home/claude/v2/seg3/{k:02d}.mp4']
ins+=['-i','/mnt/user-data/uploads/'+aud]
fc='';prev='[0:v]';cum=0
for k in range(1,n):
    cum+=d[k-1]; out=f'[x{k}]'
    fc+=f"{prev}[{k}:v]xfade=transition=fade:duration=0.3:offset={cum:.3f}{out};"; prev=out
fc+=f"{prev}subtitles=/home/claude/v2/subs3.ass:fontsdir=/home/claude/fonts/ttf[v]"
cmd=['ffmpeg','-v','error']+ins+['-filter_complex',fc,'-map','[v]','-map',f'{n}:a','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-af','afade=t=out:st=118:d=2','-t','120','/home/claude/v2/jj_beneficios_v3.mp4','-y']
r=subprocess.run(cmd,capture_output=True,text=True); print(r.returncode,r.stderr[-800:])
