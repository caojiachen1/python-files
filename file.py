import shutil
from moviepy.editor import *
import cv2
import os
from tkinter import filedialog
import tkinter.messagebox as msgbox
import ffmpeg
import wave
from moviepy.video.io.VideoFileClip  import VideoFileClip
#from moviepy.video.compositing.concatenate import concatenate_videoclips
import PyPDF2
import requests
import zipfile
import re

filetype_list = {
    'picture' : ['jpg' , 'gif' , 'png' , 'jpeg' , 'bmp'] , 
    'video' : ['avi' , 'mp4' , 'wmv' , 'mpeg' , 'mpga' , 'mov' , '3gp' , 'rmvb' , 'flv'] , 
    'application' : ['exe' , 'com'] , 
    'text' : ['txt'] , 
    'word' : ['doc' , 'docx'] , 
    'audio' : ['mp3' , 'wav' , 'flac' , 'wma' , 'm4a' , 'aac' , 'mid' , 'midi' , 'rm' , 'ram'] , 
    'excel' : ['xlsx' , 'xls'] , 
    'ppt' : ['ppt' , 'pptx'] , 
    'csv chart' : ['csv'] , 
    'pdf' : ['pdf'] , 
    'batch' : ['bat' , 'cmd'] , 
    'source code' : ['h' , 'hpp' , 'cc' , 'c' , 'cpp' , 'py' , 'pyc' , 'pyi' , 'py3' , 'pyo' , 'pyd' , 'pyx' , 'pyz' , 'pywz' , 'rpy' , 'pyde' , 'pyp' , 'pyt' , 'java'] , 
    'wolfram file' : ['nb'] , 
    'html' : ['html' , 'htm'] , 
    'photoshop file' : ['psd'] , 
    'zip' : ['zip' , 'rar' , '7z' , 'apz' , 'ar' , '.bz' , 'car' , 'dar' , 'cpgz' , 'f' , 'ha' , 'hbc' , 'hbc2' , 'hbe' , 'hpk' , 'hyp' , 'lzh' , 'cab' , 'jar'] , 
    'log' : ['log'] , 
    'system file' : ['sys'] , 
    'registry file' : ['reg'] , 
    'temporal' : ['tmp'] , 
    'data' : ['dat'] , 
    'font' : ['fon' , 'fot'] , 
    'record' : ['rec'] , 
    'group' : ['grp'] , 
    'initiation' : ['ini'] , 
    'card' : ['crd'] , 
    'calendar' : ['cal'] , 
    'write' : ['wri'] , 
    'pascal' : ['pas'] , 
    'basic' : ['bas'] , 
    'fortran' : ['for'] , 
    'assembly language' : ['asm'] , 
    'help' : ['hlp'] , 
    'password' : ['psl'] , 
    'driver' : ['drv'] , 
    'clipboard' : ['clp'] , 
    'wps' : ['wps'] , 
    'flash' : ['swf' , 'flv'] , 
    'markdown' : ['md']
}

def splitname(path):
    global name , suffix
    name , suffix = os.path.splitext(os.path.basename(path))
    suffix = suffix[1:]
    return name , suffix

class file():
    def __init__(self , file_path) -> None:
        if not os.path.exists(file_path):
            f = open(file_path , mode = 'x')
            f.close()
        self.path = file_path
        self.size = int(os.path.getsize(self.path)/1024)
        self.name = os.path.basename(self.path)
        self.type = ''
        self.parent = os.path.split(self.path)[0]
        s = splitname(self.path)[1]
        for eachtype in filetype_list.keys():
            if s in filetype_list[eachtype]:
                self.type = eachtype
                break
        self.info = {'path':self.path , 'size':self.size , 'name':self.name , 'type':self.type}

    def rename(self , new_name):
        dir = os.path.split(self.path)[0]
        dir_ = os.path.join(dir , new_name)
        try:
            os.rename(self.path , os.path.join(dir_))
            self.path = dir_
        except Exception as e:
            print(e)
            return 

    def move(self , new_directory):
        try:
            shutil.move(self.path , new_directory)
            self.path = os.path.join(new_directory , self.name)
        except Exception as e:
            print(e)
            return

    def copy(self , new_directory):
        try:
            shutil.copy(self.path , new_directory)
        except Exception as e:
            print(e)
            return

    def delete(self):
        delete = msgbox.askokcancel('确认' , '确实要将此文件彻底删除吗?')
        if not delete:
            return
        try:
            os.unlink(self.path)
        except Exception as e:
            print(e)
            return

    def open_in_explorer(self) -> None:
        os.startfile(self.parent)

    def run(self):
        os.system(self.path)

class audio(file):
    def __init__(self , path) -> None:
        super().__init__(path)
        with wave.open(path , mode = 'rb') as a:
            info = a.getparams()
            self.channels , self.sampwidth , self.framerate , self.frames = info[:4]
            self.duration = round(self.frames/self.framerate)

class video(file):
    def __init__(self , video_path) -> None:
        super().__init__(video_path)
        global v , probe
        self.isvideo = True
        try:
            v = cv2.VideoCapture(self.path)
            probe = ffmpeg.probe(self.path)
            self.codec = probe['streams'][0]['codec_name']
            self.bitrate = int(int(probe['format']['bit_rate'])/1024)
            self.resolution = int(v.get(cv2.CAP_PROP_FRAME_WIDTH)) , int(v.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.fps = v.get(cv2.CAP_PROP_FPS)
            self.frames = v.get(cv2.CAP_PROP_FRAME_COUNT)
            self.duration = self.frames/self.fps
            self.fullinfo = probe
        except Exception:
            self.codec = 'Unknown'
            probe = {}
            self.bitrate = 0
            self.resolution = 0 , 0
            self.fps = 0
            self.frames = 0
            self.duration = 0
            self.fullinfo = probe
            self.isvideo = False
        self.audio_path = ''
        self.newpath = ''

    def to_audio(self):
        if not self.isvideo:
            print('Not a video file!')
            return
        a = AudioFileClip(self.path)
        b = splitname(self.path)[0] + '.wav'
        self.audio_path = os.path.join(self.parent , b)
        a.write_audiofile(self.audio_path)
        return audio(self.audio_path)

    def remove_audio(self):
        if not self.isvideo:
            print('Not a video file!')
            return
        a = VideoFileClip(self.path)
        b = splitname(self.path)[0] + '_noaudio.mp4'
        v = a.without_audio()
        self.newpath = os.path.join(self.parent , b)
        v.write_videofile(self.newpath)
        return video(self.newpath)

    '''def Bitrate_modification(self , output_path , target_bitrate) -> None:
        a = VideoFileClip(self.path)
        a.write_videofile(output_path , bitrate = target_bitrate)'''

class folder(file):
    def __init__(self , dir) -> None:
        super().__init__(dir)
        self.files = []
        self.subfolder = []
        for i in os.scandir(self.path):
            if i.is_file():
                self.files.append(i.path)
            else:
                self.subfolder.append(i.path)

class picture(file):
    def __init__(self , pic_path) -> None:
        super().__init__(pic_path)
        global img , info
        self.isimage = True
        try:
            img = cv2.imread(self.path)
            info = img.shape
            self.height = info[0]
            self.width = info[1]
            self.channels = info[2]
        except Exception:
            self.height = 0
            self.width = 0
            self.channels = 0
            self.isimage = False

    def be_gray(self):
        if not self.isimage:
            print('Not a picture!')
            return
        img2 = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        return img2

    def show(self):
        if not self.isimage:
            print('Not a picture!')
            return
        cv2.imshow(self.name , img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

class text(file):
    def __init__(self , file_path) -> None:
        super().__init__(file_path)
        self.text = ''
        self.texts = ''
        self._updatetext()

    def _updatetext(self):
        with open(self.path) as f:
            f.seek(0)
            self.text = f.read()
            f.seek(0)
            self.texts = f.readlines()
            f.seek(0)

    def additional_write(self , content):
        with open(file = self.path , mode = 'a') as f:
            f.write(content)
        self._updatetext()

    def overwrite(self , content):
        with open(file = self.path , mode = 'w') as f:
            f.write(content)
        self._updatetext()

    def clear(self):
        with open(file = self.path , mode = 'w') as f:
            f.write('')
        self._updatetext()

class pdf(file):
    def __init__(self , file_path) -> None:
        super().__init__(file_path)
        self.ispdf = True
        try:
            pdfreader = PyPDF2.PdfFileReader(self.path)
            self.pages = pdfreader.numPages
        except Exception:
            self.paget = 0
            self.ispdf = False

class html():
    def __init__(self , path) -> None:
        self.path = path
        source = requests.get(self.path).text
        self.source = source.encode('utf-8')

class zip(file):
    def __init__(self ,  file_path) -> None:
        super().__init__(file_path)
        self.compress_type = {}
        self.original_size = {}
        self.compress_size = {}
        self.last_modified_time = {}
        self.compression_rate = {}
        with zipfile.ZipFile(self.path , mode = 'r') as z:
            self.names = z.namelist()
            self.fullinfo = z.infolist()
        for files in self.fullinfo:
            compress_type = re.search(r'compress_type=(.*?) ' , str(files))
            if compress_type is None:
                self.compress_type[files.filename] = None
            else:
                self.compress_type[files.filename] = compress_type.group(1)
            self.last_modified_time[files.filename] = files.date_time
            self.compress_size[files.filename] = round(files.compress_size/1024 , 1)
            self.original_size[files.filename] = round(files.file_size/1024 , 1)
            if files.file_size == 0:
                self.compression_rate[files.filename] = 0
            else:
                self.compression_rate[files.filename] = round(files.compress_size/files.file_size , 2)

    def add(self , path):
        with zipfile.ZipFile(self.path , mode = 'a') as z:
            z.write(path)

    def extractall(self):
        folder_name = os.path.join(self.parent , splitname(self.path)[0]  +  '_')
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name)
        f = file(self.path)
        f.copy(folder_name + '.' + splitname(self.path)[1])
        z = zipfile.ZipFile(self.path)
        for name in z.namelist():
            z.extract(name , folder_name)
        z.close()
        '''with zipfile.ZipFile(self.path , mode = 'w') as z:
            try:
                z.extractall(folder_name + '/')
            except:
                raise'''

    def extract(self , name , path):
        with zipfile.ZipFile(self.path , mode = 'w') as z:
            try:
                z.extract(name , path)
            except:
                raise

class exe(file):
    def __init__(self , file_path) -> None:
        super().__init__(file_path)

def Get_file():
    path = ''
    null = True
    while null:
        path = filedialog.askopenfilename()
        path = path.replace('/' , '\\')
        if path != '':
            null = False
    return path

def Get_directory():
    path = ''
    null = True
    while null:
        path = filedialog.askdirectory()
        path = path.replace('/' , '\\')
        if path != '':
            null = False
    return path

'''def combine(a:video , b:video , savepath = 'D:/'):
    a1 = VideoFileClip(a.path)
    b1 = VideoFileClip(b.path)
    vlist = [a1 , b1]
    combined = concatenate_videoclips(vlist)
    combined.write_videofile(savepath)'''
