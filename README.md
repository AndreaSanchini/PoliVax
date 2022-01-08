# PoliVax

## Index

- Datasets
- Group components

## Datasets

You can find the datasets in the <code>data</code> folder. Please follow the steps below to generate the elasticsearch
indexes:
- from kibana homepage, select <code>owid_covid_data_cleaned.csv</code> and start the guided procedure. Override the
analysis settings, change 'column1' name to 'index' and set 'number of lines to sample' to 10'000 so that all fields 
can be correctly mapped. Once the analysis is complete, press 'import' and move to the next page. Name the index <code>owid_covid_data</code>
and start the importing process.
- from kibana homepage, select <code>eu_vaccinations_cleaned.csv</code> and start the guided procedure. Override the
analysis settings, change 'column1' name to 'RecordNumber' and press 'import' to move to the next page. Select 'Advanced' and 
modify the mapping as follows:
<br/><br/>
change
    ```sh
         "YearWeekISO": {
          "type": "keyword"
        },
    ```
    to
    ```sh
         "YearWeekISO": {
          "type": "date",
          "format": "weekyear_week"
        },
    ```
  Name the index <code>vaccinations_europe</code> and start the importing process.
## Group Components

| Cognome    | Nome       | e-mail                             | Matricola | Codice Persona |
|------------|------------|------------------------------------|-----------|----------------|
| Musumeci   | Margherita | margherita.musumeci@mail.polimi.it | 991549    | 10600069       |
| Nunziante  | Matteo     | matteo.nunziante@mail.polimi.it    | 992518    | 10670132       |
| Rendina    | Piero      | piero.rendina@mail.polimi.it       | 991437    | 10629696       |
| Sanchini   | Andrea     | andrea.sanchini@mail.polimi.it     | 992072    | 10675541       |
| Zuccolotto | Enrico     | enrico.zuccolotto@mail.polimi.it   | 993209    | 10666354       |