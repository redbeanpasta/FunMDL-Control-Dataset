from datasets import load_dataset
import numpy as np
import os
from noise_generation import add_noise


BASE_DATASET = load_dataset("grosenthal/latin_english_translation")

def create_noisy_dataset():
    """Create a noisy dataset based on the original dataset."""
    
    noise_types = ['char_substitution', 'char_deletion', 'char_insertion', 'char_swap']
    noise_levels = [0.1, 0.2, 0.3, 0.4, 0.5]

    output_dir = "toy_datasets"
    os.makedirs(output_dir, exist_ok=True)

    for noise_type in noise_types:
        for noise_level in noise_levels:
            noisy_data = []
            for item in BASE_DATASET['train']:
                latin_text = item['la']
                noisy_latin = add_noise(latin_text, noise_type, noise_level)
                noisy_data.append({'id': item['id'], 'la': noisy_latin, 'en': item['en']})
            
            output_path = os.path.join(output_dir, f"latin_english_{noise_type}_{int(noise_level*100)}.json")
            with open(output_path, 'w') as f:
                import json
                json.dump(noisy_data, f, ensure_ascii=False, indent=4)
            print(f"Saved noisy dataset with {noise_type} at {noise_level} to {output_path}")

if __name__ == "__main__":
    create_noisy_dataset()