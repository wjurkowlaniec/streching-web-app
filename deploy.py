#!/usr/bin/env python3
import json
import os
import shutil
from pathlib import Path

def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return json.load(f)

def generate_html(config: dict, template_path: str, output_path: str, images_dir: str = None):
    with open(template_path, 'r') as f:
        template = f.read()
    
    html = template.replace('{{TITLE}}', config['name'])
    html = html.replace('{{CONFIG}}', json.dumps(config))
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(html)
    
    if images_dir and os.path.exists(images_dir):
        output_images_dir = os.path.join(os.path.dirname(output_path), 'images')
        if os.path.exists(output_images_dir):
            shutil.rmtree(output_images_dir)
        shutil.copytree(images_dir, output_images_dir)

def main():
    base_dir = Path(__file__).parent
    template_path = base_dir / 'template.html'
    configs_dir = base_dir / 'configs'
    images_dir = base_dir / 'images'
    release_dir = base_dir / '_release'
    
    if release_dir.exists():
        shutil.rmtree(release_dir)
    
    for config_file in configs_dir.glob('*.json'):
        config_name = config_file.stem
        config = load_config(config_file)
        
        output_dir = release_dir / config_name
        output_file = output_dir / 'index.html'

        config_images_dir = images_dir / config_name if (images_dir / config_name).exists() else None
        
        generate_html(config, template_path, output_file, config_images_dir)
        print(f"Generated {output_file}")
    
    print(f"\nDeployment complete! Files in {release_dir}")
    print("Each directory contains a single index.html file ready for deployment.")

if __name__ == '__main__':
    main()
