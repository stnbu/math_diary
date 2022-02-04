"""

        if 'caption' in self.options:
            caption = self.options['caption'] or self.arguments[0]
"""

from subprocess import Popen, PIPE
from docutils import nodes
from docutils.parsers import rst
from docutils.parsers.rst.directives import unchanged


class scriptdoc(nodes.Element):
    pass


class ScriptdocDirective(rst.Directive):
    has_content = False
    final_argument_whitespace = True
    required_arguments = 1
    option_spec = dict(format=unchanged)

    def run(self):
        env = self.state.document.settings.env
        node = scriptdoc()
        node.line = self.lineno
        node["command"] = self.arguments[0]
        node["format"] = self.options["format"]
        self.add_name(node)
        return [node]


def run_scripts(app, doctree):
    for node in doctree.traverse(scriptdoc):
        proc = Popen(node["command"].split(" "), stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        if proc.returncode != 0:
            raise Exception(
                "subprocess `%s` died with %s: %s"
                % (node["command"], proc.returncode, err.decode())
            )
        output = out.decode()
        format = node["format"]
        new_node = None
        if format == "html":
            new_node = nodes.raw("", output, format=format)
        elif format == "literal":
            new_node = nodes.literal_block(output, output)
            new_node["language"] = "text"
        else:
            raise Exception("Unsupported format: %s" % format)
        node.replace_self(new_node)


def setup(app):
    app.add_directive("scriptdoc", ScriptdocDirective)
    app.connect("doctree-read", run_scripts)
    return {"parallel_read_safe": True}
