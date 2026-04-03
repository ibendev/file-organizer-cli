import argparse
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--source-dir', dest='source_dir', required=True)
parser.add_argument('--target-dir', dest='target_dir', required=True)

args = parser.parse_args()
source_dir = os.path.expanduser(args.source_dir)
target_dir = os.path.expanduser(args.target_dir)

if not os.path.isdir(source_dir):
    parser.error('source-dir is not a valid directory')

if not os.path.isdir(target_dir):
    os.makedirs(target_dir)

print(f'source-dir: {source_dir}')
print(f'target-dir: {target_dir}')

categories = {
    'pdfs': {'.pdf'},
    'images': {'.jpg', '.jpeg', '.png'},
    'text': {'.txt'},
    'music': {'.mp3', '.mp4'}
}

for category in categories:
    os.makedirs(os.path.join(target_dir, category), exist_ok=True)

other_dir = os.path.join(target_dir, 'other')
os.makedirs(other_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    if not os.path.isfile(file_path):
        continue

    _, extension = os.path.splitext(filename)
    extension = extension.lower()

    moved = False

    for category, extensions in categories.items():
        if extension in extensions:
            dest_path = os.path.join(target_dir, category, filename)

            if os.path.exists(dest_path):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dest_path):
                    new_name = f"{base}_{counter}{ext}"
                    dest_path = os.path.join(target_dir, category, new_name)
                    counter += 1

            shutil.move(file_path, dest_path)
            moved = True
            break

    if not moved:
        dest_path = os.path.join(other_dir, filename)

        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(dest_path):
                new_name = f"{base}_{counter}{ext}"
                dest_path = os.path.join(other_dir, new_name)
                counter += 1

        shutil.move(file_path, dest_path)
