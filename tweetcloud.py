import os
from wordcloud import WordCloud

tweets_file = open(os.path.join('output', 'tweets_python.txt'))
text = tweets_file.read()
tweets_file.close()

#Generate wordcloud image
wordcloud = WordCloud().generate(text)

image = wordcloud.to_image()
image.save(os.path.join('output', 'python_cloud.png'))