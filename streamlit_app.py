import streamlit

import decipher


streamlit.markdown('''
Is someone making you crack codes in order to read [great caitvi porn](https://archiveofourown.org/works/44904886)?
This app has got you covered.
''')

text = streamlit.text_area(
    'paste the coded text here:',
    help='paste text into the box'
)

if text.strip():

    deciphered_texts = decipher.decipher_text(text)

    if len(deciphered_texts) == 1:
        streamlit.header('success!')
    else:
        streamlit.subheader('hmm, multiple possible matches...')

    for text, key in deciphered_texts:

        streamlit.metric('transition key', key)
        streamlit.markdown(text)
