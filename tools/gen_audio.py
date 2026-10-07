"""產生預錄音檔（edge-tts，雲哲男聲）。只補新增或文字有改的。
用法：~/.venvs/tts/bin/python tools/gen_audio.py
音檔：audio/{概念卡id}.mp3、audio/{題目id}.mp3、audio/W{週}.mp3；audio/index.json 記錄文字雜湊"""
import asyncio, hashlib, json, os
import edge_tts
VOICE, RATE = 'zh-TW-YunJheNeural', '-5%'
concepts = json.load(open('concepts.json')); quiz = json.load(open('quiz.json')); weeks = json.load(open('weeks.json'))
items = {}
for c in concepts: items[c['id']] = f"{c['term']}。{c['def']}。例如：{c['example']}"
for q in quiz: items[q['id']] = q['why']
for w in weeks:
    if w['points']: items[f"W{w['week']}"] = f"第{w['week']}週，{w['title']}。" + '。'.join(w['points'])
idx = json.load(open('audio/index.json')) if os.path.exists('audio/index.json') else {}
async def main():
    n = 0
    for k, t in items.items():
        h = hashlib.md5((VOICE + t).encode()).hexdigest()
        if idx.get(k) == h and os.path.exists(f'audio/{k}.mp3'): continue
        await edge_tts.Communicate(t, VOICE, rate=RATE).save(f'audio/{k}.mp3')
        idx[k] = h; n += 1
    for k in list(idx):
        if k not in items: idx.pop(k); 
    json.dump(idx, open('audio/index.json', 'w'), indent=0)
    print(f'產生 {n} 個，共 {len(items)} 個')
asyncio.run(main())
