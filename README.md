# NetworkVisualizer
## Visualization of network data

The purpose of this project is to create an application to visualize network data.

The repo is structured as follows: 
* networkvisualization.ipynb
* app.py
* utils.py
* templates
  * index.html
  * 2d.html
  * 3d.html
* presentation.pdf 
  

In the notebook **networkvisualization.ipynb**, the network is visualized in 2d and 3d. Regarding the 3d visualizations, there are multiple visualizations: one using matplotlib which is plotted as a notebook plot and one with plotly which is opened in a separate html page.

The notebook uses the following libraries:
  * networkx
  * matplotlib
  * json
  * chart_studio.plotly 
  * plotly
  * mpl_toolkits
  * pandas
  * numpy

To install the necessary libraries run ``` pip install -r  requirements_nb.txt ``` from the terminal.


The script **app.py** produces a web based application displaying the plots of the network that runs locally. In this case, the 2d visualization has been produced using the library d3.js though observablehq.com (see source code at https://observablehq.com/@lorenzomauri17/2d-chart), while, the 3d visualization is the one produced with plotly. To create the chart on https://observablehq.com, a txt file with the information of the graph needs to be uploaded in the "File Attachments" section. All the steps to create the following txt can in the noteboook **networkvisualization.ipynb**.

**utils.py** contains an helper function used in **app.py**. 
**templates** contains the html templates of the web app.

The scrips use the following libraries:
 * pandas
 * networkx 
 * json
 * plotly
 * networkx 
 * json
 * numpyencoder
 * flask

To install the necessary libraries run ``` pip install -r  requirements_app.txt ``` from the terminal.

To run the app locally, open the app.py in a python IDE, run the script app.py and go to http://localhost:5000/ to land in the home page.
Alternatively, run ``` python3 app.py ``` **networkvisualization.ipynb** and go to the url appearing in the terminal.

From the home page, you have the possibility to choose the dimensionality of the chart (2d or 3d). Clicking on one of the 2 buttons you will be redirected to a page with the corresponding chart. From the page, you can return to the home page with the home button on the bottom of the page

The same app has been deployed online (see http://maurilo.pythonanywhere.com/).

In order to create the visualization of the network with the notebook and to produce the 3d visualization of the app, the excel file **raan_case_study.xlsx** needs to be in the directory.

Finally, presentation.pdf is a short presentation of the main contents of the repo.


