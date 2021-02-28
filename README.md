# NetworkVisualizer
## Visualization of network data

The purpose of this project is to create an application to visualize network data.

The repo is structured as follows: 
* networkvisualization.ipynb
* app.py
* utils
* templates
  * index.html
  * 2d.html
  * 3d.html  
  
In the notebook **networkvisualization.ipynb**, the network is visualized in 2d and 3d. Regarding the 3d visualizations, there are multiple visualizations: one using matplotlib which is plotted as a notebook plot and one with plotly which is opened in a separate html page.


The script **app.py** produces a web based application with displaying the plots of the network that runs locally. In this case, the 2d visualization has been produced using the library d3.js though observablehq.com (see source code at https://observablehq.com/@lorenzomauri17/mobile-patent-suits), while, the 3d visualization is the one produced with plotly. **utils.py** contains helper functions used in **app.py**. 
**templates** contains the html templates of the web app.

The same app has been deployed online (see http://maurilo.pythonanywhere.com/).

In order to create the visualization of the network with the notebook and to produce the 3d visualization of the app, the excel file **raan_case_study.xlsx** needs to be in the directory.

The notebook uses the following libraries 
  * networkx
  * matplotlib
  * json
  * chart_studio.plotly 
  * plotly
  * mpl_toolkits
  * pandas
  * numpy

