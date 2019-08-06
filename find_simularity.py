import os
from keras.utils import get_file
import subprocess
import gensim

MODEL = 'GoogleNews-vectors-negative300.bin'
path = get_file(MODEL + '.gz', 'https://deeplearning4jblob.blob.core.windows.net/resources/wordvectors/%s.gz' % MODEL)
if not os.path.isdir('generated'):
    os.mkdir('generated')

unzipped = os.path.join('generated', MODEL)
if not os.path.isfile(unzipped):
    with open(unzipped, 'wb') as fout:
        zcat = subprocess.Popen(['zcat'],
                          stdin=open(path),
                          stdout=fout
                         )
        zcat.wait()

model = gensim.models.KeyedVectors.load_word2vec_format(unzipped, binary=True)

while 1:
    print('\n\n##### Data model successfully loaded!\n')
    word = input('Enter a word to find similarities: ')
    try:
        print(model.most_similar(positive=[word]))
    except KeyError as e:
        print (e)