import io


def print_svg(plot):
    backend = plot.backend(plot)
    backend.process_series()
    f = io.StringIO()
    backend.fig.savefig(f, format="svg")
    f.seek(0)
    return f

def write_svg_to_file(plot, path):
    f = print_svg(plot)
    f.readline()
    f.readline()
    f.readline()
    with open(path, 'w') as g:
        g.write(f.read())

def write_out_to_file(out, path):
    with open(path, 'w') as f:
        f.write(out)

# this mess
if False:
    from sympy import *
    from sympy.plotting import plot_implicit, plot
    from sympy.plotting.plot import Plot, Parametric2DLineSeries, LineOver1DRangeSeries
    from sympy.plotting.plot_implicit import *
    x, y, t = symbols("x y t")
    f_series = ImplicitSeries(
        Eq(x**2 + y + 4, 0),
        var_start_end_x=(x, -5, 5),
        var_start_end_y=(y, -8, 2),
        has_equality=True,
        use_interval_math=True,
        depth=0,
        nb_of_points=300,
        line_color='blue')
    plot_expr = [(2*t + 1, t - 5, (t, -10, 10))]
    l_series = [Parametric2DLineSeries(*arg) for arg in plot_expr]
    plot_expr = [(4*t**2 + 5*t, (t, -10, 10))]
    g_series = [LineOver1DRangeSeries(*arg) for arg in plot_expr]
    p = Plot(f_series, *l_series, *g_series, xlim=(-5, 5), ylim=(-8, 2), labels=True)

# also nope
if False:
    import os
    from subprocess import Popen, PIPE
    def capture_output(script):
        proc = Popen(["python3", script], stdout=PIPE)
        out, _ = proc.communicate()
        print(dir(proc))
        if proc.returncode != 0:
            raise Exception
        ext = os.path.splitext(os.path.splitext(script)[0])[1]
        #import ipdb; ipdb.set_trace()
        with open(script + ext,"wb") as f:
            f.write(out)
    
    if __name__ == "__main__":
        import sys
        capture_output(sys.argv[1])
