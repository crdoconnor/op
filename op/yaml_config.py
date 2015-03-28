import os, yaml, edi_command, parent_checker



class OpConfig(object):
    """Represents an op YAML config file containing OpCommands. See /example_configs for examples."""
    rules = None

    def __init__(self):
        """Look for a .op.yml file in every directory above the current one. If found, read it."""
        opyml_filename = parent_checker.parent_checker(".op.yml")

        if not opyml_filename:
            self.rules = []
        else:
            with open(opyml_filename, 'r') as opyml_handle:
                self.rules = yaml.safe_load(opyml_handle.read())

    def no_config(self):
        """Poor user is going to get whatever his system thinks his favorite text editor is."""
        return len(self.rules) == 0

    def get_commands(self, trigger):
        """Get a list of commands - either default command(s) (if no trigger hit), or the specified command(s) (if there is a hit)."""
        commands = [op_command.OpCommand(x) for x in self.rules if "trigger" in x and x.get('trigger', '') == trigger]
        return (False, [op_command.OpCommand(x) for x in self.rules if "trigger" not in x]) if len(commands) == 0 else (True, commands)
