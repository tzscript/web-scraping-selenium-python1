import googletrans
from googletrans import Translator

article = '''
Turbulent flights
Budget airlines have requested that the Finance Ministry reduce the excise tax on jet fuel because carriers are floundering as tourism sags, costs surge and the baht strengthens.

'''

LAM  = Translator()
result = LAM.translate(article,dest='th')
print(result.text)