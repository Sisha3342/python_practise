# Task
- [x] read dataset from 
https://github.com/Sisha3342/pydata-book/tree/2nd-edition/datasets/titanic

- [x] Build final dataframe
    - [x] with genderclassmodel.csv and gendermodel.csv 
        conclude, who (from the last 418 passengers) finally survived / didn't survive
        (in places where **Survived** columns are different i put np.NaN), result in *finally_survived* dataframe
    - [x] merge *finally_survived* with dataframe from test.csv (result in *last_passengers_info* dataframe)
    - [x] concatenate dataframe from train.csv (*start_passengers_info*) and *last_passengers_info*
- [ ] Visualisation
    - [x] Build a pie with **Survived** column (survived, didn't survive and unknown (np.NaN))
    - [x] Build a pie with survived males / females relation
    - [ ] Build a hist where: 
        1) x_axis - **Fare** (0-49; 50-99; 100 and more)
        2) y_axis - **Survived** (how many people with corresponding fare survived)