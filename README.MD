# PPKWU - ZADANIE 3 - MOBILNY KALENDARZ WEEIA

## Details

The API generates (for the current or selected month) a calendar in ICS/iCal format for data from `http://www.weeia.p.lodz.pl`

## Endpoints

### Request

`GET /events`

### Response

iCalendar file containing events from actual month

### Request

`GET /events/<year>/<month>`

- `<year>` is numeric value relates to year of selected month
- `<month>` is numeric value relates to selected month

### Response

iCalendar file containing events from selected month

### Example

`GET /events/2020/03`
