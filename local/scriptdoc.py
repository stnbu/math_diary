from subprocess import Popen, PIPE
from docutils import nodes
from docutils.parsers import rst
from docutils.parsers.rst.directives import flag, unchanged


class scriptdoc(nodes.Element):
    pass


class ScriptdocDirective(rst.Directive):
    has_content = False
    final_argument_whitespace = True
    required_arguments = 1
    option_spec = dict(
        output_language=unchanged,
        source_path=unchanged,
        source_language=unchanged,
        source_show=flag,
    )

    def run(self):
        env = self.state.document.settings.env
        node = scriptdoc()
        node.line = self.lineno
        node["source_show"] = "source_show" in self.options
        options = [
            ("output_language", "text"),
            ("source_path", None),
            ("source_language", "text"),
        ]
        for key, default in options:
            node[key] = self.options.get(key, default)
        node["command"] = self.arguments[0]
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
        output_string = out.decode()
        output_node = None
        output_language = node.get("output_language", "text")
        source_language = node.get("source_language", "text")
        source_show = node.get("source_show", False)
        if output_language == "html":
            output_node = nodes.raw("", output_string, format=output_language)
        else:
            output_node = nodes.literal_block(output_string, output_string)
            output_node["language"] = output_language

        if source_show:
            source_path = node.get(
                "source_path", node["command"].split()[0]  # good luck!
            )
            source_string = None
            with open(source_path) as f:
                source_string = f.read()
            source_node = nodes.literal_block(source_string, source_string)
            source_node["language"] = source_language
            output_node.append(source_node)

        node.replace_self(output_node)


def setup(app):
    app.add_directive("scriptdoc", ScriptdocDirective)
    app.connect("doctree-read", run_scripts)
    return {"parallel_read_safe": True}
