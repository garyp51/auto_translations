import pandas as pd
import googletrans
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# ask user to choose search file
file_path = filedialog.askopenfilename()

txt = open(file_path)
words = txt.read()

# calls translator module to run
translator = Translator()

# convert original terms into a dataframe
origlist = words.splitlines()
orig_df = pd.DataFrame(origlist, columns=['Original'])

print('Please enter the original language code: (if unknown type in auto, to use googles auto-recognition)')
user_src = input()
source_lang = user_src

print('Please enter the language code you want to translate to:')
user_dest = input()
lang_code = str(user_dest)

# translates text and formats as a list
result = translator.translate(words, dest=lang_code, src=source_lang)
converted = result.text
converted = converted.splitlines()

# change converted list to dataframe and merge with original dataframe
cnv_df = pd.DataFrame(converted, columns=['Translated'])
full_df = orig_df.join(cnv_df)

# write final dataframe
full_df.to_excel('translated_' + lang_code + '.xlsx', index=False)
print('Your translated term file is now ready')