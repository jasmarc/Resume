import yaml
from jinja2 import Environment, FileSystemLoader

# Load the YAML data
with open('resume_common.yaml', 'r') as yaml_file:
    resume_data = yaml.safe_load(yaml_file)

# Load the Jinja2 templates
env = Environment(loader=FileSystemLoader('./'))
markdown_template = env.get_template('resume.md.j2')
latex_template = env.get_template('resume.tex.j2')

# Render the templates with the data
markdown_output = markdown_template.render(
    common=resume_data,
    experience=resume_data['experience'],
    skills=resume_data['skills'],
    education=resume_data['education']  # Include education data
)
latex_output = latex_template.render(
    common=resume_data,
    experience=resume_data['experience'],
    skills=resume_data['skills'],
    education=resume_data['education']  # Include education data
)

# Save the rendered templates to files
with open('README.markdown', 'w') as md_file:
    md_file.write(markdown_output)

with open('resume.tex', 'w') as tex_file:
    tex_file.write(latex_output)
