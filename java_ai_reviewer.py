import os
from google import genai

def askLlm(question):
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        config=types.GenerateContentConfig(
            system_instruction=
            f'''
                Eres un arquitecto de software Java senior con más de 15 años de experiencia.
                Responde siempre en español, de forma clara, estructurada y profesional.
                Usa ejemplos de código cuando sea útil.
            '''
        ),
        contents='Pregunta: {question}'
    )

    print(response.text)
    
print("🤖 Java AI Reviewer listo. Escribe 'salir' para terminar.\n")
while True:
    user_input = input("Pega tu código, error o pregunta de arquitectura:\n> ")
    if user_input.lower() == "salir":
        break
    answer = askLlm(user_input)
    print("\n✅ Respuesta del LLM:\n")
    print(answer)
    print("\n" + "="*80 + "\n")