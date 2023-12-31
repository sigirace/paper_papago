import re
import requests
import json
from googletrans import Translator


CLIENT_ID='CLIENT_ID'
CLIENT_SECRET='CLIENT_SECRET'


class PaperTranslate():

    def __init__(self, source='en', target='ko', file_path='text.txt'):
        self.url = 'https://openapi.naver.com/v1/papago/n2mt'
        self.headers = {
            'Content-Type': 'application/json',
            'X-Naver-Client-Id': CLIENT_ID,
            'X-Naver-Client-Secret': CLIENT_SECRET
        }
        self.source=source
        self.target=target
        self.file_path=file_path

    def get_text(self):
        # 텍스트 파일 읽기
        with open(self.file_path, 'r') as file:
            text = file.read()
        
        return text

    def split_into_sentences(self):
        text = self.get_text()
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return sentences


    def clean_text(self):
        sentences = self.split_into_sentences()
        cleaned_sentences = [sentence.replace('\n', ' ').strip() for sentence in sentences if sentence.strip()]        

        return cleaned_sentences
    
    def ptran(self):
        sentences = self.clean_text()

        for sentence in sentences:
            print(sentence)
            data = {'source': self.source, 'target': self.target, 'text': sentence}
            response = requests.post(self.url, json.dumps(data), headers=self.headers) 
            translatedText = response.json()['message']['result']['translatedText']
            print(translatedText)
            print("*"*20)
    
    def gtran(self):
        sentences = self.clean_text()
        translator = Translator()

        for sentence in sentences:
            print(sentence)
            translation = translator.translate(sentence, dest=self.target)
            print(translation.text)
            print()
    
    def word_trans(self, word):
        translator = Translator()
        trans_word = translator.translate(word, dest=self.target)
        print(trans_word.text)