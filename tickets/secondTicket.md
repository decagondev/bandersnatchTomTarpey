# Build Sprint 2: Dynamic Visualizations

To begin work on this ticket, make sure you have finished:
- Getting locally setup.
- Completed the onboarding module in your course.
- Finished Build Sprint 1.

## Objective

Dynamic Visualizations

- Notebook exploration
- Chart function
- API integration

To see what your final output should be, navigate to `/view` on the [deployed site](https://bandersnatch.herokuapp.com/).

## Relevant Files

Access `app/graph.py`, where you will add your code for this ticket. 

## Deliverables

Submit the following in your course:

- Link to your forked repo with the added code for the landing page
- Link to a Loom video answering the prompt in the `Submit Your Deliverables` Assignment in your course

Stuck? Post in `labs-ds` or open a support ticket in the Hub!

## Guidance

### A. Notebook Exploration
- [ ] Create a notebook for visualization experimentation
- [ ] Create some charts based on the data you generated in Sprint 1
- [ ] Check the Altair documentation for ideas

### B. Implement Chart Function
- Starter File: `app/graph.py`
- Suggested Graphing Library: Altair
- Function Signature: `chart(df: DataFrame, x: str, y: str, target: str) -> Chart`

- [ ] Is the function definition correct, including the correct parameters of a DataFrame, two strings for x and y, and a string for target? 
- [ ] Is the properties dictionary complete, including four keys and their corresponding values for width, height, background, and padding? 
- [ ] Is the Chart object created using the correct syntax and parameters, including the df, title, and mark_circle? Are the correct encodings used for x, y, color, and tooltip? Are the properties and configure dictionaries applied correctly using the correct syntax? 
- [ ] Does the function return the correct object, a Chart?
- [ ] Does the code follow the PEP style guide?

### C. API Graph Integration
- [ ] Make sure the graph is being serialized correctly using the `.to_json()` method
- [ ] The display of the graph should be fairly automatic, double check by running the web app locally
- [ ] Does the graph look good in the context of the Bandersnatch dark web theme?

#### Example Chart
```python
from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    )
    return graph

```
Properties and configuration need to be added such that, the chart looks good on Bandersnatch. This is totally subjective, and in the end - you will be the judge.
