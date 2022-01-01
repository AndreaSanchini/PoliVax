import pandas as pd

data = pd.read_csv('data/owid_covid_data.csv')

data = data[(data.iso_code != 'OWID_AFR') & (data.iso_code != 'OWID_ASI') & (data.iso_code != 'OWID_EUN')
            & (data.iso_code != 'OWID_EUR') & (data.iso_code != 'OWID_HIC') & (data.iso_code != 'OWID_INT')
            & (data.iso_code != 'OWID_KOS') & (data.iso_code != 'OWID_LIC') & (data.iso_code != 'OWID_LMC')
            & (data.iso_code != 'OWID_CYN') & (data.iso_code != 'OWID_NAM') & (data.iso_code != 'OWID_OCE')
            & (data.iso_code != 'OWID_SAM') & (data.iso_code != 'OWID_UMC') & (data.iso_code != 'OWID_WRL')]

data.to_csv('data/owid_covid_data_cleaned.csv')

data = pd.read_csv('data/eu_vaccinations.csv')

data = data[data['Region'].isin(['AT', 'BE', 'BG', 'CY', 'CZ', 'DE', 'DK', 'EE', 'EL', 'ES', 'FI', 'FR', 'UNK', 'HR',
                                 'HU', 'IE', 'IS', 'IT', 'LI', 'LT', 'LU', 'LV', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO',
                                 'SE', 'SI', 'SK'])]
data['ReportingCountry'] = data['ReportingCountry'].replace({'EL': 'GR'})

data.to_csv('data/eu_vaccinations_cleaned.csv')
