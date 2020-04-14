#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    fractions = pd.read_csv('src/who_suicide_statistics.csv')
    fractions['fraction'] = fractions['suicides_no'] / fractions['population']
    fractions = fractions.groupby('country').mean()
    return fractions['fraction']

def suicide_weather():
    wh = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col=0, header=0)[0]
    wh.rename(columns={"Average yearly temperature (1961–1990, degrees Celsius)": "avg_temp"}, inplace=True)
    wh['avg_temp'] = wh['avg_temp'].str.replace("\u2212", "-")
    wh['avg_temp'] = wh['avg_temp'].astype('float')
    wh.sort_index(inplace=True)
    su = suicide_fractions()
    su.sort_index(inplace=True)
    common = wh.merge(right=su, left_index=True, right_index=True)
    correlation = common['fraction'].corr(common['avg_temp'], method='spearman')
    return (len(su), len(wh), len(common), correlation)

def main():
    su, wh, common, correlation = suicide_weather()
    print(f'Suicide DataFrame has {su} rows')
    print(f'Temperature DataFrame has {wh} rows')
    print(f'Common DataFrame has {common} rows')
    print(f'Spearman correlation: {correlation:.1f}')

if __name__ == "__main__":
    main()
