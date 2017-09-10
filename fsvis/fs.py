import os
import json

suffix = ['js', 'ts', 'css', 'scss', 'html', 'java', 'xml', 'go', 'sh', 'py']

def path_to_dict(path):
    name = os.path.basename(path)
    # size = os.stat(path).st_size
    d = {'name': name,} #'size': size}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = list(filter(lambda d: d is not None, [path_to_dict(os.path.join(path, x))  for x in os.listdir(path)]))
    else:
        file_extension = name.split('.')[-1]
        if file_extension in suffix:
            d['type'] = file_extension
            d['size'] = lines(path)
        else:
            return None
    return d

def lines(path):
    with open(path) as f:
        return sum(1 for _ in f)

root = '/Users/Chao/Dropbox/Projects/youdontknowjs/code'
print(json.dumps(path_to_dict(root)))