import random
import string

def generate_shortcode():
  return ''.join(random.choices(string.ascii_letters + string.digits + '_', k=6)) 