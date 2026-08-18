import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
df = pd.read_csv(url)
df = df.dropna()
brand_fixes = {
    'toyouta': 'toyota',
    'maxda': 'mazda',
    'chevroelt': 'chevrolet',
    'chevy': 'chevrolet',
    'vokswagen': 'volkswagen',
    'vw': 'volkswagen',
    'mercedes': 'mercedes-benz'
}
df['brand'] = df['name'].str.split(' ').str[0]
df['brand'] = df['brand'].replace(brand_fixes)
df['power_to_weight'] = df['horsepower'] / df['weight']
brand_summary = df.groupby('brand')[['mpg', 'power_to_weight']].mean().sort_values(by='mpg', ascending = False)

brand_stats = df.groupby('brand').agg({
    'mpg': 'mean',
    'horsepower': 'max',
    'name' : 'count'
})
reliable_brands = brand_stats[brand_stats['name'] >= 5]
top_efficient_brands = reliable_brands.sort_values(by = 'mpg', ascending = False)
cleaned_cars = (df[['brand', 'name', 'horsepower', 'weight', 'power_to_weight']])

df.to_csv('cleaned_cars.csv', index=False)
top_efficient_brands.to_csv('top_efficient_brands.csv')

print(df)
#print(top_efficient_brands.head(5))
#print(brand_stats)
# print ("New row count:", len(df))
#print(df['brand'].unique())
#print (cleaned_cars)
#print(brand_summary.head(5))