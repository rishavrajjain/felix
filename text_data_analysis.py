
import streamlit as st 
import requests 
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os






def analysis():
    
    data = st.text_input('Paste text to be analysed')
    st.write(data)

    if data is not None:

        summary = requests.post('https://api.deepai.org/api/summarization',data={
            'text':data
        },headers={
            'api-key':os.environ['DEEP_AI_KEY']
        })
        st.write('Summary')
        st.write(json.loads(summary.content)['output'])

        keyPhrases = requests.post('https://text-analysis-hackathon.cognitiveservices.azure.com/text/analytics/v3.1-preview.4/keyPhrases',data=json.dumps({ "documents": [{ "id": "1", "text":data}]}),headers={
            'Ocp-Apim-Subscription-Key':os.environ['AZURE_KEY'],
            'Ocp-Apim-Subscription-Region':'westus2',
            'Content-Type':'application/json'
        })
        
        st.write('Key Phrases');
        st.write(json.loads(keyPhrases.content)['documents'][0]['keyPhrases']);

        st.write('Entities/Topics')
        topics = requests.post('https://text-analysis-hackathon.cognitiveservices.azure.com/text/analytics/v3.0/entities/recognition/general',data=json.dumps({ "documents": [{ "id": "1", "text":data}]}),headers={
            'Ocp-Apim-Subscription-Key':os.environ['AZURE_KEY'],
            'Ocp-Apim-Subscription-Region':'westus2',
            'Content-Type':'application/json'
        })

        topics = json.loads(topics.content)['documents'][0]['entities']
        st.write(topics)

        wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(data)
        st.write('Word Cloud');
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

            

        

