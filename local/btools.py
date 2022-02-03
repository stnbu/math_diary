import io


def print_svg(plot):
    backend = plot.backend(plot)
    backend.process_series()
    f = io.StringIO()
    backend.fig.savefig(f, format="svg")
    f.seek(0)
    print(f.read())
