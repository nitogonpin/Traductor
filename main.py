# Use a pipeline as a high-level helper
from transformers import pipeline

generador_respuesta = pipeline("translation", model="robertrengel/autotrain-traductor-en-es-2023-3608896666")
#generador_respuesta = pipeline("translation", model="robertrengel/autotrain-traductor-en-es-2023-3608896666", device=0)

def traducir(texto):
    """
    This function takes a string of text and uses the robertrengel/autotrain-traductor-en-es-2023-3608896666 model
    to translate it from English to Spanish. The translated text is then returned.
    """
    # Use the pipeline to generate a translation of the input text
    respuesta = generador_respuesta(texto, max_length=30)
    # The response is a list of dictionaries, so we need to extract the translation text from it
    respuesta = respuesta[0]['translation_text']
    # Return the translated text
    return respuesta


pregunta = "Hello, how are you?"
respuesta = traducir(pregunta)
print(respuesta)        




