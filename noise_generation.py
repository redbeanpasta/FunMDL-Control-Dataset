import numpy as np

def char_substitution_noise(text, noise_level=0.1):
    """Introduce character substitution noise into the text."""
    noisy_text = []
    for char in text:
        if char.isalpha() and np.random.rand() < noise_level:
            noisy_char = chr(np.random.randint(97, 123)) 
            noisy_text.append(noisy_char)
        else:
            noisy_text.append(char)
    return ''.join(noisy_text)

def char_deletion_noise(text, noise_level=0.1):
    """Introduce character deletion noise into the text."""
    noisy_text = []
    for char in text:
        if char.isalpha() and np.random.rand() < noise_level:
            continue  # Skip this character
        else:
            noisy_text.append(char)
    return ''.join(noisy_text)

def char_insertion_noise(text, noise_level=0.1):
    """Introduce character insertion noise into the text."""
    noisy_text = []
    for char in text:
        noisy_text.append(char)
        if char.isalpha() and np.random.rand() < noise_level:
            noisy_char = chr(np.random.randint(97, 123)) 
            noisy_text.append(noisy_char)
    return ''.join(noisy_text)

def char_swap_noise(text, noise_level=0.1):
    """Introduce character swap noise into the text."""
    noisy_text = list(text)
    for i in range(len(noisy_text) - 1):
        if noisy_text[i].isalpha() and noisy_text[i+1].isalpha() and np.random.rand() < noise_level:
            noisy_text[i], noisy_text[i+1] = noisy_text[i+1], noisy_text[i]  # Swap characters
            i += 2  # Skip the next character to avoid multiple swaps
    return ''.join(noisy_text)

# def word_deletion_noise(text, noise_level=0.1):
#     """Introduce word deletion noise into the text."""
#     words = text.split()
#     noisy_words = [word for word in words if np.random.rand() >= noise_level]
#     return ' '.join(noisy_words)

# def word_swap_noise(text, noise_level=0.1):
#     """Introduce word swap noise into the text."""
#     words = text.split()
#     for i in range(len(words) - 1):
#         if np.random.rand() < noise_level:
#             words[i], words[i+1] = words[i+1], words[i]  # Swap words
#             i += 2  # Skip the next word to avoid multiple swaps
#     return ' '.join(words)

def add_noise(text, noise_type, noise_level):
    """Add specified noise to the text."""
    if noise_type == 'char_substitution':
        return char_substitution_noise(text, noise_level)
    elif noise_type == 'char_deletion':
        return char_deletion_noise(text, noise_level)
    elif noise_type == 'char_insertion':
        return char_insertion_noise(text, noise_level)
    elif noise_type == 'char_swap':
        return char_swap_noise(text, noise_level)
    # elif noise_type == 'word_deletion':
    #     return word_deletion_noise(text, noise_level)
    # elif noise_type == 'word_swap':
    #     return word_swap_noise(text, noise_level)
    else:
        raise ValueError(f"Unknown noise type: {noise_type}")