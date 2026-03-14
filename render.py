import yaml
from jinja2 import Environment, FileSystemLoader

# Generated files: README.md, resume.tex, index.html
# Edit the corresponding .j2 templates and run render.py.

with open('resume_common.yaml', 'r') as yaml_file:
    resume_data: dict = yaml.safe_load(yaml_file)

env = Environment(loader=FileSystemLoader('./'))

render_args = dict(
    common=resume_data,
    experience=resume_data['experience'],
    skills=resume_data['skills'],
    education=resume_data['education'],
)

outputs = {
    'README.md': env.get_template('resume.md.j2'),
    'resume.tex': env.get_template('resume.tex.j2'),
    'index.html': env.get_template('index.html.j2'),
}

for filename, template in outputs.items():
    with open(filename, 'w') as f:
        f.write(template.render(**render_args))
