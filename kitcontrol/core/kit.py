import yaml

from jinja2 import Environment, FileSystemLoader
from mergedeep import merge
from os.path import exists
from io import StringIO, BytesIO
from config.config import Config

BASEPATH = Config.kits_dir

class Kit:
    def __init__(self, name, values={}):

        self.name = name

        # Load kit config
        self.config = self._load_config()

        # Merge values
        self.values = merge(self.config['values'], values)

        # Set jinja2 environment (templates dir)
        self.env = Environment(loader=FileSystemLoader(f"{BASEPATH}/{self.name}/"))

    def _load_config(self):
        return yaml.load(open(f"{BASEPATH}/{self.name}/{self.name}.yaml", "r"), Loader=yaml.loader.SafeLoader)


    def getFiles(self, osInfo=None):

        files = {}

        for filename in self.config['files']:

            # Distro prefix
            if osInfo and exists(f"{BASEPATH}/{self.name}/{osInfo.id}-{filename}"):
                filename = f"{osInfo.id}-{filename}"

            # Load template
            template = self.env.get_template(filename)
            
            # Add to dict files
            values = merge(self.values, {"osInfo": osInfo}) if osInfo else self.values
            # files[filename] = StringIO(template.render(values))
            # BytesIO to support emojis ;D
            files[filename] = BytesIO(template.render(values).encode('utf-8'))

        return files