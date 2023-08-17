import getopt
import sys
import os
import uuid

links = {
    'english-pop': 'https://open.spotify.com/playlist/5d92vg5dnI2kHvj2RHfnzs',
    'hindi': 'https://open.spotify.com/playlist/2BrlCIH69Dyb75sByC7lbv',
    'english-rap': 'https://open.spotify.com/playlist/322ommZjOoKbHaNSQLaE98',
    'hindi-rap': 'https://open.spotify.com/playlist/5coFLWaBAPzQRGjnSukvI6',
    'punjabi': 'https://open.spotify.com/playlist/6XxeGdayOztgxKaAXom8AC',
    'fottyseven': 'https://open.spotify.com/playlist/3Vs0BsFg7JLdeBV4ZfkilJ',
}

argsList = sys.argv[1:]
options = 'l:u:hf'
long_options = ['link_name=', 'url=', 'help', 'ffmpeg']


try:
    opts, vals = getopt.getopt(argsList, options, long_options)
    for (opt, arg) in opts:
      if opt in ['-l', '--link_name']:
        name = links[str(arg)]
        try:
          os.mkdir(str(arg))
        except FileExistsError: 
          pass
        finally:
          os.chdir(str(arg))
        os.system(f"python -m spotdl {name}  --output {{title}}.{{output-ext}} --overwrite skip --threads 5")
      elif opt in ['-h', '--help']:
        print('''
          -l, --link: Specify the link from available options.
              options:
                english-pop
                hindi
                english-rap
                hindi-rap
                punjabi
                fottyseven
          -a, --all: Download all the songs from a custom link.
          -f, --ffmpeg: Download ffmpeg.
          -h, --help: Display help.
        ''')
      elif opt in ['-u', '--url']:
        name = uuid.uuid4()
        os.mkdir(name)
        os.chdir(name)
        os.system(f"spodl {arg} --output {{title}}.{{output-ext}} --overwrite skip --threads 5")
      elif opt in ['-f', '--ffmpeg']:
        os.system('python -m spotdl --download-ffmpeg')
         
except getopt.error as e:
    print(str(e))