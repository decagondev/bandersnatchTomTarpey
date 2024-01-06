from altair import Chart


def chart(df, x, y, target) -> Chart:
    """
    Generates an interactive chart with configurable appearance and interaction controls.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing the data to be plotted.
    - x (str): The column name in 'df' to be used for the x-axis of the plot.
    - y (str): The column name in 'df' to be used for the y-axis of the plot.
    - target (str): The column name in 'df' to be used for coloring the scatter plot points.

    Returns:
    - Chart: An Altair chart object representing the interactive scatter plot.

    Features:
    - The chart's title is dynamically generated based on the 'y', 'x', and 'target' values.
    - The chart's background is gray and padding is added around the chart.
    - The chart has interactive zoom and pan functionality:
      - Zoom: Users can drag to create a rectangle to zoom into a specific area.
      - Pan: Users can hold the 'alt' key and drag to pan across the chart.
    - Axes and titles have customized font sizes and appearances.
    - The chart's view size is set to a fixed width and height with a gray fill and no stroke.
    """
    pass
