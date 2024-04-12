#!/usr/bin/bash

# 1. get a clean EmotiVoice with `git clone https://github.com/hgneng/EmotiVoice.git`
# 2. get sentense vector model to folder WangZeJun (refer to README.md of EmotiVoice)
# 3. download pre-trained model to folder outputs:
#    git clone https://www.modelscope.cn/syq163/outputs.git

rm -rf EmotiVoice-1.0
mkdir EmotiVoice-1.0
cd EmotiVoice-1.0
cp -r ../EmotiVoice ./
cp -r ../WangZeJun ./
cp -r ../outputs ./
cp -r ../nltk_data ./
cp -r ../deploy.sh ./
cp -r ../pack.sh ./
cd ..
tar cvf EmotiVoice-1.0.tar --exclude=.git EmotiVoice-1.0