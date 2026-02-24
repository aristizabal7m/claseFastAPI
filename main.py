from fastapi import FastAPI

app = FastAPI()


@app.get("/llm{pregunta}")
async def read_root(pregunta):
    # Crear una logica que me permita comunicarme con un LLM
    from google import genai

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client(api_key = "AIzaSyDGzlRsxv2-r9x1j495VWp5DIVWdkfVwuA")

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=pregunta
    )
    print(response.text)

    return {"Hello": response.text}


