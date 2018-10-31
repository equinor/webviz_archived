from webviz_plotly import FilteredPlotly


class HeatMap(FilteredPlotly):
    """Line chart page element.

    :param data: Either a file path to a `csv` file or a
        :class:`pandas.DataFrame`. Each column of the dataframe becomes one
        line in the chart. Similarly for the `csv` file, but a special column
        ``index`` will be used as the horizontal value.
    """
    def __init__(self, data, *args, **kwargs):

        super(HeatMap, self).__init__(
            data,
            *args,
            layout={
                'showlegend': True,
                'yaxis': {'autorange': 'reversed', 'automargin': True}
            },
            config={},
            **kwargs)

    def process_data(self, data):
        return [{
            'z': data.values.tolist(),
            'x': list(data.columns),
            'y': list(data.index),
            'type': 'heatmap'}]
