import pandas as pd

df = pd.read_csv('data/owid_covid_data.csv')

df = df[(df.iso_code != 'OWID_AFR') & (df.iso_code != 'OWID_ASI') & (df.iso_code != 'OWID_EUN')
        & (df.iso_code != 'OWID_EUR') & (df.iso_code != 'OWID_HIC') & (df.iso_code != 'OWID_INT')
        & (df.iso_code != 'OWID_KOS') & (df.iso_code != 'OWID_LIC') & (df.iso_code != 'OWID_LMC')
        & (df.iso_code != 'OWID_CYN') & (df.iso_code != 'OWID_NAM') & (df.iso_code != 'OWID_OCE')
        & (df.iso_code != 'OWID_SAM') & (df.iso_code != 'OWID_UMC') & (df.iso_code != 'OWID_WRL')]
df = df.drop(['reproduction_rate', 'icu_patients', 'icu_patients_per_million', 'hosp_patients', 'new_cases_smoothed',
              'hosp_patients_per_million', 'weekly_icu_admissions', 'weekly_icu_admissions_per_million',
              'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million', 'stringency_index', 'aged_65_older',
              'aged_70_older', 'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers',
              'handwashing_facilities', 'extreme_poverty', 'excess_mortality_cumulative_per_million',
              'excess_mortality', 'excess_mortality_cumulative', 'excess_mortality_cumulative_absolute',
              'hospital_beds_per_thousand', 'new_people_vaccinated_smoothed_per_hundred', 'tests_per_case',
              'new_people_vaccinated_smoothed', 'new_vaccinations_smoothed_per_million', 'new_vaccinations_smoothed',
              'tests_units', 'new_tests_smoothed_per_thousand', 'new_tests_smoothed', 'life_expectancy',
              'new_deaths_smoothed_per_million', 'new_cases_smoothed_per_million', 'new_deaths_smoothed'], axis=1)

df.to_csv('data/owid_covid_data_cleaned.csv')

df = pd.read_csv('data/eu_vaccinations.csv')

df = df[df['Region'].isin(['AT', 'BE', 'BG', 'CY', 'CZ', 'DE', 'DK', 'EE', 'EL', 'ES', 'FI', 'FR', 'UNK', 'HR',
                           'HU', 'IE', 'IS', 'IT', 'LI', 'LT', 'LU', 'LV', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO',
                           'SE', 'SI', 'SK'])]
df['ReportingCountry'] = df['ReportingCountry'].replace({'EL': 'GR'})
df = df.drop(['FirstDoseRefused'], axis=1)

df.to_csv('data/eu_vaccinations_cleaned.csv')
