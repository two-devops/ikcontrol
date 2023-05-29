import sys

from click import echo, style
from cmds.system import System
from cmds.config import Config

class Show:
    """Class to show kits, targets and pipelines"""

    config = Config()

    def __init__(self, entity, file=None, system=System()) -> None:

        self.entity = entity
        self.system = system
        self.file = file
        self.config.check_config()
        self.kits, self.targets, self.pipelines = self.config.load_config()
        if not self.file:
            self.show_entity()
        else:
            self.edit_entity()

    def show_entity(self):
        """show kits"""
        if self.entity == "kits":
            values = self.system.mkls(self.kits)
        elif self.entity == "targets":
            values = self.system.mkls(self.targets)
        else:
            values = self.system.mkls(self.pipelines)

        echo(style(f"\n{self.entity}\n", fg="blue"))
        echo(style(f'{values}', fg='green', italic=True))
    
    def edit_entity(self):
        """edit kits, targets or pipelines"""

        # Check if exits entity
        self.check_exist_entities()

        if self.entity == "kits":
            file = self.kits + "/" + self.file + "/" + self.file+".yaml"
        elif self.entity == "targets":
            file = self.targets + "/" + self.file + ".yaml"
        else:
            file = self.pipelines + "/" + self.file + ".yaml"
        self.system.mkedit(file)

    def check_exist_entities(self):
        """Check exist"""
        if self.entity == "kits":
            if not self.system.search(self.kits + "/" + self.file):
                echo(style(f"\nInfo: {self.file} not found in {self.entity}\n", fg="yellow"))
                sys.exit()
        elif self.entity == "targets":
            if not self.system.search(self.targets + "/" + self.file + ".yaml"):
                echo(style(f"\nInfo: {self.file} not found in {self.entity}\n", fg="yellow"))
                sys.exit()
        else:
            if not self.system.search(self.pipelines + "/" + self.file + ".yaml"):
                echo(style(f"\nInfo: {self.file} not found in {self.entity}\n", fg="yellow"))
                sys.exit()
