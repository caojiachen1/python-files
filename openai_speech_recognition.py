from transformers import pipeline
import torch
import tkinter.filedialog , os , translate_baiduapi

paths = tkinter.filedialog.askopenfilenames()
a = pipeline('automatic-speech-recognition',
                model = 'openai/whisper-large-v2',
                device = 'cuda:0',
                chunk_length_s = 20,
                framework = 'pt',
                torch_dtype = torch.float16)
for path in paths:
    name = os.path.basename(path)[:-4]
    dir = os.path.dirname(path)
    new_dir = os.path.join(dir , f'{name}.txt')
    prediction = a(path)['text']
    prediction.replace('.' , '.\n')
    with open(new_dir , mode = 'w') as f:
        f.write(prediction)
    with open(new_dir , mode = 'a+') as f:
        for i in f.readlines():
            f.write(translate_baiduapi.translate(i))
            f.write("\n")
    print(f'{path}  finish')