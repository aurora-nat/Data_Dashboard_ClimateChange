import pandas as pd
import plotly.graph_objects as go

def cleandata(dataset):
    """
        Clean the data from the world development indicators
        Args:
            dataset(str): name of the csv data file
        Reutnrs:
            a clean dataset(str)
    """
    df = pd.read_csv(dataset)
    #Rename the columns to be clearer
    df = df.rename(columns={"Series Name":"Title", "Country Name": "Country","1990 [YR1990]": "1990", "2000 [YR2000]": "2000", "2012 [YR2012]":"2012","2013 [YR2013]": "2013",
                  "2014 [YR2014]":"2014", "2015 [YR2015]": "2015", "2016 [YR2016]": "2016", "2017 [YR2017]":"2017",
                  "2018 [YR2018]": "2018", "2019 [YR2019]":"2019"})
    
    #Remove all other columns but the Country Name and the 
    keepcolumns=['Title','Country', '1990', '2000', '2012', '2013', '2014','2015', '2016', '2018']
    df = df[keepcolumns]

    #retrieve the "Title of the Data"
    data_title = df['Title'][0]
    df = df.drop(columns=['Title'], axis=1)
    #We will transpose our data to make it useful for the plotly x,y values by melting the dataframe
    df = df.melt(id_vars='Country', var_name='Year', value_name=data_title)
    #Sort the graph by Country
    df = df.sort_values(by=['Country'])
    return df


def create_plotlist(df):
    """
        This functions modularizes our code, by creating the plotly graph go list
        Args:
            df: the dataframe that has be cleaned to be used for go plotly
        Returns:
            list(go.Scatter) to be used for our plotly visualizations
    """
    ploty_graph = []
    #Get the variable of interest
    column_variable = df.columns.values[2]
    #Organize data into a list:
    countryList = df.Country.unique().tolist()

    #Create the graph go plots based on country
    for country in countryList:
        x_val = df[df['Country'] == country]['Year'].tolist()
        y_val = df[df['Country'] == country][column_variable].tolist()
        ploty_graph.append(
            go.Scatter(
                x= x_val,
                y = y_val,
                mode = 'markers',
                name = country
            )
        )
    return ploty_graph


def return_figures():
    """
        Creates four plotly visualizations

        Args:
            None
        Returns: 
            list(dict): list containing the four plotly visualizations
    """
    
    #First Chart deals with CO2 Emissions for the 6 highest producing countries of GDP
    graph_one = []
    #Clean our data
    df_one = cleandata('data/graph_one.csv')
    #Prepare data for go:
    graph_one = create_plotlist(df_one)
    
    #Create our layout:
    layout_one = dict(title="CO2 Emissions (Metric tons per capita)",
                      xaxis=dict(title='Country'), 
                      yaxis=dict(title='CO2 Emmissions'),
                      )
      
    #Second Chart deals with GreenHouse Emissions for the 6 highest producing countries of GDP
    graph_two = []
    #Clean our data
    df_two = cleandata('data/graph_two.csv')
    #Prepare data for go:
    graph_two = create_plotlist(df_two)
    
    #Create our layout:
    layout_two = dict(title="Total Greenhouse Gas Emissions",
                      xaxis=dict(title='Country'), 
                      yaxis=dict(title='Greenhouse Emmissions'),
                      )
    
    #Third Chart deals with Forested Area for the 6 highest producing countries of GDP
    graph_three = []
    #Clean our data
    df_three = cleandata('data/graph_three.csv')
    #Prepare data for go:
    graph_three = create_plotlist(df_three)
    #Create our layout:
    layout_three = dict(title="Forest Area (percent of land area)",
                      xaxis=dict(title='Country'), 
                      yaxis=dict(title='Forest Area'),
                      )
    
    #Fourth Chart deals with Population Growth for the 6 highest producing countries of GDP
    graph_four = []
    #Clean our data
    df_four = cleandata('data/graph_four.csv')
    #Prepare data for go:
    graph_four = create_plotlist(df_four)
    
    #Create our layout:
    layout_four = dict(title="Population Growth (annual percent)",
                      xaxis=dict(title='Country'), 
                      yaxis=dict(title='Population Growth'),
                      )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
  

    return figures