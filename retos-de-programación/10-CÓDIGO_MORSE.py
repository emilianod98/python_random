# CÓDIGO MORSE
#
#------------------------------------------------------------------
#
# Crea un programa que sea capaz de transformar texto natural a código
# morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar
#   la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#   o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en
#   https://es.wikipedia.org/wiki/Código_morse.
#
#------------------------------------------------------------------

# Diccionario de conversión de texto a código morse
TEXT_TO_MORSE = {
    'A': '•-', 'B': '-•••', 'C': '-•-•', 'D': '-••', 'E': '•', 'F': '••-•',
    'G': '--•', 'H': '••••', 'I': '••', 'J': '•---', 'K': '-•-', 'L': '•-••',
    'M': '--', 'N': '-•', 'O': '---', 'P': '•--•', 'Q': '--•-', 'R': '•-•',
    'S': '•••', 'T': '-', 'U': '••-', 'V': '•••-', 'W': '•--', 'X': '-••-',
    'Y': '-•--', 'Z': '--••',
    '0': '-----', '1': '•----', '2': '••---', '3': '•••--', '4': '••••-', '5': '•••••',
    '6': '-••••', '7': '--•••', '8': '---••', '9': '----•',
    '.': '•-•-•-', ',': '--••--', '?': '••--••', '\'': '•----•', '!': '-•-•--',
    '/': '-••-•', '(': '-•--•', ')': '-•--•-', '&': '•-•••', ':': '---•••',
    ';': '-•-•-•', '=': '-•••-', '+': '•-•-•', '-': '-••••-', '_': '••--•-',
    '"': '•-••-•', '$': '•••-••-', '@': '•--•-•'
}

# Diccionario de conversión de código morse a texto
MORSE_TO_TEXT = {v: k for k, v in TEXT_TO_MORSE.items()}

def is_morse_code(text):
    """Detecta si el texto proporcionado es código morse."""
    return all(char in ['•', '-', ' ', ''] for char in text)

def text_to_morse(text):
    """Convierte texto natural a código morse."""
    text = text.upper()
    morse_code = []
    for word in text.split(' '):
        morse_word = ' '.join(TEXT_TO_MORSE.get(char, '') for char in word)
        morse_code.append(morse_word)
    return '  '.join(morse_code)

def morse_to_text(morse):
    """Convierte código morse a texto natural."""
    words = morse.split('  ')
    decoded_words = []
    for word in words:
        decoded_letters = [MORSE_TO_TEXT.get(letter, '') for letter in word.split()]
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)

def convert(input_text):
    """Convierte automáticamente entre texto y código morse."""
    if is_morse_code(input_text):
        return morse_to_text(input_text)
    else:
        return text_to_morse(input_text)

# Ejemplo de uso
input_text1 = "Hola Mundo"
input_text2 = "•••• --- •-•• •-  -- ••- -• -•• --- -•-•--"
print("Texto a Morse:", convert(input_text1))
print("Morse a Texto:", convert(input_text2))
