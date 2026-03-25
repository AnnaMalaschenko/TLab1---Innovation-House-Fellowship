1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

# Phase 1 was the most active period because both the median and average heartrate are the highest of all the phases.
Average heartrate was 87.3, and the median heartrate was 88.5.

# For this person's age, their target heart rate is 95-162 bpm. In Phase 1 the median is below this target, which means that most of the time their heartrate was below the target range. They did have individual heartrate values that went above 95 bpm, meaning that they occasionally hit the range.

2) Which file had the **poorest** data quality? How do you know?

# Phase 0 had the poorest data quality because it had the most missing values (as indicated by the "Number of Removed Values" counter being 3).

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
Range = 180 - 68 = 112


b) Explain how the extreme value affects the range.
# The extreme value would have us think that the numbers are widely varied and can be found between 68 - 180, but all but one are in fact between 68-75. The single outlier results in a calculated range which can make us think there are values above 75 other than the single outlier.

c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?
# The interquartline range can better help us understand the variability because it capctures the middle 50% of the dataset without including the outliers.
