# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

#Get text from website or database??
text = """

"""
#placeholder/test text
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT) #store in document object

response = client.classify_text(document)
categories = response.categories #categories
for category in categories:
    print(u'=' * 20)
    print(u'{:<16}: {}'.format('category', category.name))
    print(u'{:<16}: {}'.format('confidence', category.confidence))

