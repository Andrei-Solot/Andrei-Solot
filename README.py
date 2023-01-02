def generate_short_readme(name, specialization):
    readme = f"# {name} - Machine Learning Engineer (Specialization in {specialization})\n\n"
    readme += "I am a Masters graduate from Goldsmiths University of London. I am a competent and committed person looking for a rewarding career in computational neuroscience and AI engineering."
    return readme

name = "Andrei Solot"
specialization = "Neuroscience"

print(generate_short_readme(name, specialization))
