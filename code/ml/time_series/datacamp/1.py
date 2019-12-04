# Based on the data gathered in the previous exercise, you can see that you have data for 2 different areas, area1 and area2. To easily compare and analyze this data, you should bring each device into its own column.

# To load the data, you specify your own column names, since you did not save these with the data. After loading the data, you need to convert the timestamp. The timestamp is in milliseconds, which we need to tell to_datetime by specifying unit="ms".

# You pivot the data and resample the data to 1-minute intervals since for this dataset, a more detailed analysis would not make sense.


# Replace the timestamp with the parsed timestamp
df["ts"] = pd.to_datetime(df["ts"], unit="ms")
print(df.head())

# Pivot the DataFrame
df2 = pd.pivot_table(df, columns="device", values="val", index="ts")
print(df2.head())

# Resample DataFrame to 1min
df3 = df2.resample("1min").max().dropna()
print(df3.head())

df3.to_csv(TARGET_FILE)

# ---------------------------------

# Get difference between values
df_diff = df.diff()

# Plot the DataFrame
df_diff.plot()
plt.show()


# Resample df to 30 minutes
df_res = df.resample("30min").max()

# Get difference between values
df_diff = df_res.diff()

# Get the percent changed
df_pct = df_diff.pct_change()

# Plot the DataFrame
df_pct.plot()
plt.show()

"""
Well done. Notice that after the first Section we saw a huge spike. 
This is because there is some data missing. 
By resampling the data to 30 minute intervals, we can clearly see that area2 has a much higher energy consumption than area. 
After visualizing the percentage change, the differences become clearer 
    and we can see that area1 has higher fluctuations, however we cannot see which one has a higher overall consumption.
"""


### Combining datasources for further analysis  ###
### ------------------------------------------- ###

# Rename the columns
temperature.columns = ["temperature"]
humidity.columns = ["humidity"]
windspeed.columns = ["windspeed"]

# Create list of dataframes
df_list = [temperature, humidity, windspeed]

# Concatenate files
environment = pd.concat(df_list, axis=1)

# Print dataframe
print(environment.head())

# Combine the dataframes
environ_traffic = pd.concat([environ, traffic], axis=1)

# Print first 5 rows
print(environ_traffic.head())

# Create agg logic
agg_dict = {
    "temperature": "max",
    "humidity": "max",
    "sunshine": "sum",
    "light_veh": "sum",
    "heavy_veh": "sum",
}

# Resample the dataframe
environ_traffic_resampled = environ_traffic.resample("1h").agg(agg_dict)
print(environ_traffic_resampled.head())

##-----------------------------------------------------------------------
## Correlation

# Calculate correlation
corr = data.corr()

# Print correlation
print(corr)

# Create a heatmap
sns.heatmap(corr, annot=True)

# Show plot
plt.show()


# Import required modules
import seaborn as sns

# Create a pairplot
sns.pairplot(data)

# Show plot
plt.show()


##-----------------------------------------------------------------------
## Outliers
# Calculate mean
data["mean"] = data["temperature"].mean()

# Calculate upper and lower limits
data["upper_limit"] = data["mean"] + (data["temperature"].std() * 3)
data["lower_limit"] = data["mean"] - (data["temperature"].std() * 3)

# Plot the dataframe
data.plot()

plt.show()

##---------------------------------------

# Plot traffic dataset
traffic[:"2018-11-10"].plot()

# Show plot
plt.show()

# Import tsaplots
from statsmodels.graphics import tsaplots

# Plot autocorrelation
tsaplots.plot_acf(traffic["vehicles"], lags=50)

# Show the plot
plt.show()


## --------------------------

# Import modules
import statsmodels.api as sm

# Perform decompositon
res = sm.tsa.seasonal_decompose(traffic["vehicles"])

# Print the seasonal component
print(res.seasonal.head())

# Plot the result
res.plot()

# Show the plot
plt.show()


## --------------------------


# Resample dataframe to 1h
df_seas = df.resample("1h").max()

# Run seasonal decompose
decomp = sm.tsa.seasonal_decompose(df_seas)

# Plot the timeseries
plt.title("Temperature")
plt.plot(df_seas["temperature"], label="temperature")

# Plot trend and seasonality
plt.plot(decomp.trend["temperature"], label="trend")
plt.plot(decomp.seasonal["temperature"], label="seasonal")
plt.legend()
plt.show()


# -----------------------------------------------------------------------
# Prepare data for machine learning
# Define the split day
limit_day = "2018-10-27"

# Split the data
train_env = environment[:limit_day]
test_env = environment[limit_day:]

# Print start and end dates
print(show_start_end(train_env))
print(show_start_end(test_env))

# Split the data into X and y
X_train = train_env.drop("target", axis=1)
y_train = train_env["target"]
X_test = test_env.drop("target", axis=1)
y_test = test_env["target"]


# Import LogisticRegression
from sklearn.linear_model import LogisticRegression

# Initialize the model
logreg = LogisticRegression()

# Fit the model
logreg.fit(X_train, y_train)

# Predict classes
print(logreg.predict(X_test))


# -----------------------------------------------------------------------
# Model Evaluation

# Create LogisticRegression model
logreg = LogisticRegression()

# Fit the model
logreg.fit(X_train, y_train)

# Score the model
print(logreg.score(X_train, y_train))
print(logreg.score(X_test, y_test))


############## SCALING  #################

# Import StandardScaler
from sklearn.preprocessing import StandardScaler

# Initialize StandardScaler
sc = StandardScaler()

# Fit the scaler
sc.fit(environment)

# Print mean and variance
print(sc.mean_)
print(sc.var_)


# Transform the data
environ_scaled = sc.transform(environment)

# Convert scaled data to DataFrame
environ_scaled = pd.DataFrame(
    environ_scaled, columns=environment.columns, index=environment.index
)
print(environ_scaled.head())
plot_unscaled_scaled(environment, environ_scaled)


############## Develop machine learning pipeline  #################

# Import pipeline
from sklearn.pipeline import Pipeline

# Create Scaler and Regression objects
sc = StandardScaler()
logreg = LogisticRegression()

# Create Pipeline
pl = Pipeline([("scale", sc), ("logreg", logreg)])

# Fit the pipeline and print predictions
pl.fit(X_train, y_train)
print(pl.predict(X_test))

######################### 

# Create Pipeline
pl = Pipeline([
        ("scale", StandardScaler()),
        ("logreg", LogisticRegression())
    ])

# Fit the pipeline
pl.fit(X_train, y_train)

# Store the model
with Path("pipeline.pkl").open('bw') as f:
	pickle.dump(pl, f)
  
# Load the pipeline
with Path("pipeline.pkl").open('br') as f:
	pl_loaded = pickle.load(f)

print(pl_loaded)