from transformers import pipeline
from textblob import TextBlob
import random

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

# Add random SEO keywords for demonstration
def get_random_keywords():
    keyword_pool = ['Python', 'data science', 'machine learning', 'AI', 'automation', 'coding', 'software development']
    return random.sample(keyword_pool, 3)

if __name__ == "__main__":
    # Initialize the GPT-2 model
    generator = initialize_model()

    prompt = input("Enter the content prompt: ")

    seo_keywords = get_random_keywords()

    content = generate_content(generator, prompt, keywords=seo_keywords, max_length=500)

    print("\nGenerated and Refined Content:\n")
    print(content)
