# GPT-2 Content Generator

This repository contains a Python script that uses the GPT-2 model to generate content based on a user-provided prompt. The script also incorporates SEO keywords to enhance the generated content.

## Prerequisites

- Python 3.6 or higher
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/zimkk/gpt2-content-generator.git
    cd gpt2-content-generator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. Enter the content prompt when prompted:
    ```sh
    Enter the content prompt: <your prompt here>
    ```

3. The script will generate content based on the provided prompt and output it to the console.

## Code Explanation

The main functionality of the script is contained within the [`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fviper%2FDocuments%2FWork%2FScripts%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%2231b9d5e2-6d43-4173-b0e5-68af762e5fdd%22%5D "c:\Users\viper\Documents\Work\Scripts\main.py") file. Below is a brief explanation of the key parts of the code:

```python
from transformers import pipeline
from textblob import TextBlob
from rake_nltk import Rake

# Initialize the GPT-2 text generation pipeline
def initialize_model():
    print("Loading GPT-2 model...")
    generator = pipeline('text-generation', model='gpt2', temperature=0.7, top_p=0.9)
    print("Model loaded successfully.")
    return generator

def correct_grammar(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()  # Correct the grammar and spelling
    return str(corrected_text)

def get_seo_keywords(prompt):
    rake = Rake()
    rake.extract_keywords_from_text(prompt)
    keywords = rake.get_ranked_phrases()
    return keywords[:5]  # Return top 5 keywords

def generate_content(generator, prompt, keywords=[], max_length=300):
    # Build the structured prompt with keywords
    keyword_text = " ".join(keywords) if keywords else ""
    structured_prompt = f"{prompt}\n\nKeywords to include: {keyword_text}\n\n"
    
    print(f"Generating content for the prompt: {prompt}")
    result = generator(structured_prompt, max_length=max_length, num_return_sequences=1)
    
    # Fetch generated text and perform grammar check
    generated_text = result[0]['generated_text']
    refined_text = correct_grammar(generated_text)
    
    return refined_text

if __name__ == "__main__":
    generator = initialize_model()

    prompt = input("Enter the content prompt: ")

    seo_keywords = get_seo_keywords(prompt)

    content = generate_content(generator, prompt, keywords=seo_keywords, max_length=300)

    print("\nGenerated and Refined Content:\n")
    print(content)
```

- **Model Initialization**: The GPT-2 model is initialized using the [`initialize_model()`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fviper%2FDocuments%2FWork%2FScripts%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A4%7D%7D%5D%2C%2231b9d5e2-6d43-4173-b0e5-68af762e5fdd%22%5D "Go to definition") function.
- **Prompt Input**: The user is prompted to enter the content prompt.
- **SEO Keywords**: SEO keywords are fetched using the [`get_seo_keywords()`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fviper%2FDocuments%2FWork%2FScripts%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A16%2C%22character%22%3A4%7D%7D%5D%2C%2231b9d5e2-6d43-4173-b0e5-68af762e5fdd%22%5D "Go to definition") function, which uses RAKE (Rapid Automatic Keyword Extraction) to extract keywords from the prompt.
- **Content Generation**: The content is generated using the [`generate_content()`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fviper%2FDocuments%2FWork%2FScripts%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A22%2C%22character%22%3A4%7D%7D%5D%2C%2231b9d5e2-6d43-4173-b0e5-68af762e5fdd%22%5D "Go to definition") function, which takes the model, prompt, keywords, and maximum length as parameters.
- **Output**: The generated content is printed to the console.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for the [`transformers`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fviper%2FDocuments%2FWork%2FScripts%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A5%7D%7D%5D%2C%2231b9d5e2-6d43-4173-b0e5-68af762e5fdd%22%5D "Go to definition") library.
- [TextBlob](https://textblob.readthedocs.io/en/dev/) for text processing.
- [RAKE-NLTK](https://github.com/csurfer/rake-nltk) for keyword extraction.

---

Feel free to customize this README file as per your project's specific details and requirements.
