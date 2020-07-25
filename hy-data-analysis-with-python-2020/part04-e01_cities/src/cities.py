#!/usr/bin/env python3

import pandas as pd

def cities():
    populations = [643272, 279044, 231853, 223027, 201810]
    areas = [715.48, 528.03, 689.59, 240.35, 3817.52]
    columns = ["Population", "Total area"]
    indices = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    df = pd.DataFrame(list(zip(populations, areas)), columns=columns, index=indices)
    return df

def main():
    print(cities())

if __name__ == "__main__":
    main()
