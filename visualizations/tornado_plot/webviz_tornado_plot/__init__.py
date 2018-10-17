from webviz_plotly import FilteredGraph


class TornadoPlot(FilteredGraph):
    """Tornado plot page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. There are two columns:
        'low' and 'high' describing.
    :param high_text: Optional text
    :param xaxis: Will create a label for the x-axis. Defaults to `None`.
    :param yaxis: Will create a label for the y-axis. Defaults to `None`.
    """
    def __init__(self, data, id='tornado-plot-graph', *args, **kwargs):
        xaxis = kwargs.pop('xaxis') if 'xaxis' in kwargs else None
        yaxis = kwargs.pop('yaxis') if 'yaxis' in kwargs else None
        super(TornadoPlot, self).__init__(
            *args,
            id=id,
            data=data,
            layout={
                'barmode': 'relative',
                'showlegend': False,
                'xaxis': {'title': xaxis},
                'yaxis': {'automargin': True, 'title': yaxis}
                },
            config={},
            **kwargs)

    def process_data(self, data):
        low_bars = {
            'type': 'bar',
            'name': 'low',
            'x': [],
            'y': [],
            'base': [],
            'orientation': 'h',
            'marker': {
                'color': 'rgba(210, 15, 140, 0.7)',
                'line': {
                    'width': 2,
                    'color': 'rgba(210, 15, 140, 1)'
                }
            }
        }
        high_bars = {
            'type': 'bar',
            'name': 'high',
            'x': [],
            'y': [],
            'base': [],
            'orientation': 'h',
            'marker': {
                'color': 'rgba(64, 83, 125,0.5)',
                'line': {
                    'width': 2,
                    'color': 'rgba(64, 83, 125, 1)'
                }
            }
        }

        for index, row in data.iterrows():
            high_bars['y'].append(index)
            low_bars['y'].append(index)
            if row['high'] > 0:
                base = max(0, row['low'])
                high_bars['x'].append(row['high'] - base)
                high_bars['base'].append(base)
            else:
                high_bars['x'].append(0)
                high_bars['base'].append(row['high'])

            if row['low'] < 0:
                base = min(0, row['high'])
                low_bars['x'].append(row['low'] - base)
                low_bars['base'].append(base)
            else:
                low_bars['x'].append(0)
                low_bars['base'].append(row['low'])

        return [low_bars, high_bars]
