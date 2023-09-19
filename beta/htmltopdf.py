import pdfkit as pdf
import psutil
import streamlit as st
import time

st.write('''Title: "The Magical Adventure of Sammy and the Talking Animals"

Once upon a time, in a small village nestled between rolling hills and a sparkling river, lived a curious and kind-hearted boy named Sammy. Sammy was known for his adventurous spirit and his love for exploring the beautiful forest that bordered his village.

One sunny morning, Sammy decided to embark on a new adventure. Armed with his backpack and a pocketful of snacks, he ventured into the depths of the forest. As he walked along the winding paths, he noticed something extraordinary: the animals of the forest were talking!

At first, Sammy couldn't believe his ears. He thought he might be imagining things, but as he listened more closely, he realized that the animals were indeed having conversations. Birds were sharing stories about their recent travels, squirrels were discussing their favorite acorn recipes, and even the wise old owl was imparting its wisdom.

Sammy approached a friendly-looking rabbit and asked, "How is it possible that you can talk?"

The rabbit, named Rosie, replied with a chuckle, "We've always been able to talk, Sammy, but we keep it a secret from humans like you."

Sammy's eyes widened with amazement. He felt like he had stumbled upon a magical world hidden within the forest. He spent the entire day talking to the animals, hearing their stories, and making new friends.

As the sun began to set, Sammy reluctantly said his goodbyes and headed back home. He couldn't wait to share his incredible discovery with his family and friends.

The next day, Sammy returned to the forest, and from that day forward, he and the talking animals became inseparable friends. They had picnics together, went on exciting adventures, and even helped each other solve problems.

Sammy's village soon learned of his newfound friendships, and instead of being afraid, they were filled with wonder and awe. The talking animals became beloved members of the community, and the village flourished with happiness.

And so, Sammy's life was forever changed by the magical world hidden in the forest. He learned that sometimes, the most extraordinary adventures are right in our own backyard, waiting to be discovered. Sammy and his talking animal friends lived happily ever after, reminding everyone that friendship knows no boundaries, and the world is full of enchanting surprises for those with open hearts and curious minds.





''')

path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

url = 'http://localhost:8502/' 

# Output file name for the PDF
output_pdf = "output.pdf"

config = pdf.configuration(wkhtmltopdf=path)

# Convert the URL to PDF
pdf.from_url(url, output_pdf, configuration=config)

print(f"PDF saved as {output_pdf}")
