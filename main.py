from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

def element_to_text(element):
    return element.text

if len(sys.argv) < 2:
    print("No linked provided")
    exit(1)

link = sys.argv[1]

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get(f'https://youtubetranscript.com/?v={link}')
time.sleep(10)

elements = driver.find_elements(By.CLASS_NAME, 'youtube-marker')

text = list(map(element_to_text, elements))

words = []
for line in text:
    for word in line.split():
        if word[0] != '[':
            words.append(word)

word_map = dict()
for word in words:
    if word not in word_map:
        word_map[word] = 1
    else:
        word_map[word] += 1

word_list = sorted(word_map.items(), key=lambda x: -x[1])

for word_pair in word_list:
    (word, _count) = word_pair
    print(word)





