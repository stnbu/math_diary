import io


def print_svg(plot):
    backend = plot.backend(plot)
    backend.process_series()
    f = io.StringIO()
    backend.fig.savefig(f, format="svg")
    f.seek(0)
    return f

def write_to_file(plot, path):
    f = print_svg(plot)
    f.readline()
    f.readline()
    f.readline()
    with open(path, 'w') as g:
        g.write(f.read())
